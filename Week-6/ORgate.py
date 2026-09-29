import pandas as pd
data = [
    [1, 1, 1],
    [1, 0, 1],
    [0, 1, 1],
    [0, 0, 0]
]
w1 = float(input("Enter Weight 1: "))
w2 = float(input("Enter Weight 2: "))
b = -0.5
learning_rate = 0.1
rows = []
for x1, x2, gt in data:
    z = (x1 * w1) + (x2 * w2) + b
    py = 1 if z >= 0 else 0
    error = gt - py
    dw1 = learning_rate * error * x1
    dw2 = learning_rate * error * x2
    dw = abs(dw1) + abs(dw2)
    rows.append([
        x1, x2, gt, py, error,
        learning_rate, dw, w1, w2
    ])
table = pd.DataFrame(
    rows,
    columns=["X1", "X2", "GT", "PY", "E", "L", "ΔW", "W1", "W2"]
)
print("\nOR GATE - ANN")
print("=" * 70)
print(table.to_string(index=False))
print("=" * 70)