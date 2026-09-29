import torch
x = torch.tensor([[1.0, 1.0]])
target = torch.tensor([[0.5]])
learning_rate = 1.0
epochs = 5
w1 = torch.tensor([
    [0.5, 0.5],
    [0.5, 0.5]
], requires_grad=True)
b1 = torch.tensor([[0.0, 0.0]], requires_grad=True)
w2 = torch.tensor([
    [0.5],
    [0.5]
], requires_grad=True)
b2 = torch.tensor([[0.0]], requires_grad=True)
results = []
for epoch in range(1, epochs + 1):
    hidden = torch.sigmoid(x @ w1 + b1)
    output = torch.sigmoid(hidden @ w2 + b2)
    loss = 0.5 * (target - output) ** 2
    loss.backward()
    with torch.no_grad():
        w1 -= learning_rate * w1.grad
        b1 -= learning_rate * b1.grad
        w2 -= learning_rate * w2.grad
        b2 -= learning_rate * b2.grad
    results.append([
        epoch,
        output.item(),
        target.item(),
        loss.item(),
        w1[0, 0].item(),
        w1[0, 1].item(),
        w1[1, 0].item(),
        w1[1, 1].item(),
        w2[0, 0].item(),
        w2[1, 0].item()
    ])
    w1.grad.zero_()
    b1.grad.zero_()
    w2.grad.zero_()
    b2.grad.zero_()
print("\nMLP USING BACKPROPAGATION")
print("Architecture: 2-2-1")
print("=" * 125)
print(
    f"{'Epoch':^7}"
    f"{'Actual Output':^16}"
    f"{'Target':^12}"
    f"{'Loss':^14}"
    f"{'W1(1,1)':^12}"
    f"{'W1(1,2)':^12}"
    f"{'W1(2,1)':^12}"
    f"{'W1(2,2)':^12}"
    f"{'W2(1)':^12}"
    f"{'W2(2)':^12}"
)
print("-" * 125)
for row in results:
    print(
        f"{row[0]:^7}"
        f"{row[1]:^16.6f}"
        f"{row[2]:^12.2f}"
        f"{row[3]:^14.6f}"
        f"{row[4]:^12.6f}"
        f"{row[5]:^12.6f}"
        f"{row[6]:^12.6f}"
        f"{row[7]:^12.6f}"
        f"{row[8]:^12.6f}"
        f"{row[9]:^12.6f}"
    )
print("=" * 125)