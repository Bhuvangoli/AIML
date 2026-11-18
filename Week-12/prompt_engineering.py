!pip install -q transformers torch torchvision pillow requests opencv-python-headless matplotlib

import torch
import requests
import numpy as np
import cv2
import matplotlib.pyplot as plt

from PIL import Image
from io import BytesIO
from transformers import (
    BlipProcessor,
    BlipForQuestionAnswering,
    DetrImageProcessor,
    DetrForObjectDetection,
    AutoModelForQuestionAnswering,
    AutoTokenizer,
    pipeline
)

print("\n========== A. IMAGE QUESTION ANSWERING (BLIP) ==========\n")
img_url = "http://images.cocodataset.org/val2017/000000039769.jpg"
raw_image = Image.open(
    BytesIO(requests.get(img_url).content)
).convert("RGB")
processor_blip = BlipProcessor.from_pretrained(
    "Salesforce/blip-vqa-base"
)
model_blip = BlipForQuestionAnswering.from_pretrained(
    "Salesforce/blip-vqa-base"
)
question = "What objects are visible in the image?"

inputs = processor_blip(
    raw_image,
    question,
    return_tensors="pt"
)
out = model_blip.generate(**inputs)

print("Question:", question)
print("Answer:", processor_blip.decode(
    out[0], skip_special_tokens=True
))

print("\n========== B. OBJECT DETECTION USING DETR ==========\n")

url = "http://images.cocodataset.org/val2017/000000039769.jpg"

image = Image.open(
    BytesIO(requests.get(url).content)
).convert("RGB")
processor = DetrImageProcessor.from_pretrained(
    "facebook/detr-resnet-50",
    revision="no_timm"
)

model = DetrForObjectDetection.from_pretrained(
    "facebook/detr-resnet-50",
    revision="no_timm"
)
inputs = processor(
    images=image,
    return_tensors="pt"
)
outputs = model(**inputs)
target_sizes = torch.tensor([image.size[::-1]])

results = processor.post_process_object_detection(
    outputs,
    target_sizes=target_sizes,
    threshold=0.9
)[0]
for score, label, box in zip(
    results["scores"],
    results["labels"],
    results["boxes"]
):
    box = [round(i, 2) for i in box.tolist()]

    print(
        f"Detected {model.config.id2label[label.item()]} "
        f"with confidence {round(score.item(), 3)} "
        f"at location {box}"
    )

print("\n========== C. IMAGE DETECTION WITH BOUNDING BOXES ==========\n")

url = "http://images.cocodataset.org/val2017/000000039769.jpg"

image_pil = Image.open(
    BytesIO(requests.get(url).content)
).convert("RGB")

image_np = np.array(image_pil)

processor = DetrImageProcessor.from_pretrained(
    "facebook/detr-resnet-50",
    revision="no_timm"
)

model = DetrForObjectDetection.from_pretrained(
    "facebook/detr-resnet-50",
    revision="no_timm"
)

inputs = processor(
    images=image_pil,
    return_tensors="pt"
)

outputs = model(**inputs)

target_sizes = torch.tensor([image_pil.size[::-1]])

results = processor.post_process_object_detection(
    outputs,
    target_sizes=target_sizes,
    threshold=0.9
)[0]

for score, label, box in zip(
    results["scores"],
    results["labels"],
    results["boxes"]
):
    box = [int(i) for i in box.tolist()]

    color = (0, 255, 0)
    thickness = 2

    cv2.rectangle(
        image_np,
        (box[0], box[1]),
        (box[2], box[3]),
        color,
        thickness
    )

plt.figure(figsize=(10, 10))
plt.imshow(image_np)
plt.axis("off")
plt.title("Object Detection with Bounding Boxes")
plt.show()

print("\n========== D. IMAGE DETECTION WITH LABELS ==========\n")

image_url = "http://images.cocodataset.org/val2017/000000039769.jpg"

image_pil = Image.open(
    BytesIO(requests.get(image_url).content)
).convert("RGB")

image_np = np.array(image_pil)

processor = DetrImageProcessor.from_pretrained(
    "facebook/detr-resnet-50",
    revision="no_timm"
)

model = DetrForObjectDetection.from_pretrained(
    "facebook/detr-resnet-50",
    revision="no_timm"
)

inputs = processor(
    images=image_pil,
    return_tensors="pt"
)

outputs = model(**inputs)

target_sizes = torch.tensor([image_pil.size[::-1]])

results = processor.post_process_object_detection(
    outputs,
    target_sizes=target_sizes,
    threshold=0.9
)[0]

for score, label, box in zip(
    results["scores"],
    results["labels"],
    results["boxes"]
):
    box = [int(i) for i in box.tolist()]

    label_text = model.config.id2label[label.item()]

    color = (0, 255, 0)
    thickness = 2

    cv2.rectangle(
        image_np,
        (box[0], box[1]),
        (box[2], box[3]),
        color,
        thickness
    )

    text = f"{label_text}: {round(score.item(), 3)}"

    cv2.putText(
        image_np,
        text,
        (box[0], max(box[1] - 10, 15)),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.5,
        color,
        2
    )

image_rgb = cv2.cvtColor(
    image_np,
    cv2.COLOR_BGR2RGB
)

plt.figure(figsize=(10, 10))
plt.imshow(image_rgb)
plt.axis("off")
plt.title("Object Detection with Labels")
plt.show()

print("\n========== E. TEXT QUESTION ANSWERING ==========\n")

model_name = "deepset/roberta-base-squad2"

nlp = pipeline(
    "question-answering",
    model=model_name,
    tokenizer=model_name
)

QA_input = {
    "question": "Why is model conversion important?",
    "context": (
        "The option to convert models between FAH and "
        "transformers gives freedom to the user and lets "
        "people easily switch between frameworks."
    )
}

# Get prediction
res = nlp(QA_input)

print("Question:", QA_input["question"])
print("Answer:", res["answer"])


# ------------------------------------------------------------
# SECOND TEXT QUESTION ANSWERING EXAMPLE
# ------------------------------------------------------------

question_answerer = pipeline(
    "question-answering",
    model="distilbert-base-uncased-distilled-squad"
)

context = """
There once was a boy who grew bored while watching over
the village sheep.
He wanted to make things more exciting.
"""

result = question_answerer(
    question="Who cried?",
    context=context
)

print("\nSecond Question:", "Who cried?")
print("Answer:", result["answer"])


print("\n========== ALL EXPERIMENTS COMPLETED ==========")
