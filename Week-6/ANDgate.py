import pandas as pd
inputs = [
    (1, 1, 1),
    (1, 0, 0),
    (0, 1, 0),
    (0, 0, 0)
]
w1 = float(input("Enter Weight 1: "))
w2 = float(input("Enter Weight 2: "))
b = -1.5
L = 0.1
results = []
for x1, x2, gt in inputs:
    z = (x1 * w1) + (x2 * w2) + b
    if z >= 0:
        py = 1
    else:
        py = 0
    E = gt - py

    dw1 = L * E * x1
    dw2 = L * E * x2
    results.append([
        x1, x2, w1, w2, b, z, gt, py, E, L, dw1, dw2
    ])
columns = [
    "X1", "X2", "W1", "W2", "Bias",
    "Z", "GT", "PY", "E", "L",
    "ΔW1", "ΔW2"
]
df = pd.DataFrame(results, columns=columns)
print("\nAND GATE ANN")
print("=" * 100)
print(df.to_string(index=False))
print("=" * 100)