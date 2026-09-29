import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split

df = pd.read_csv("tips.csv")

x = df["total_bill"].values
y = df["tip"].values

x_train, x_test, y_train, y_test = train_test_split(
    x, y, test_size=0.2, random_state=42
)

tau = 5.0

x_train = np.column_stack([np.ones(len(x_train)), x_train])

predictions = []

for bill in x_test:
    weights = np.exp(-((x_train[:, 1] - bill) ** 2) / (2 * tau ** 2))
    W = np.diag(weights)
    xTW = np.dot(x_train.T, W)
    A = np.dot(xTW, x_train)
    b = np.dot(xTW, y_train)
    theta = np.dot(np.linalg.inv(A), b)
    prediction = theta[0] + theta[1] * bill
    predictions.append(prediction)

predictions = np.array(predictions)

sorted_indices = np.argsort(x_test)
x_test_sorted = x_test[sorted_indices]
predictions_sorted = predictions[sorted_indices]

plt.scatter(x_train[:, 1], y_train, color="lightblue", label="Training Data", marker="o")
plt.scatter(x_test, y_test, color="darkblue", label="Test Data", marker="o")
plt.plot(x_test_sorted, predictions_sorted, color="red", label="Prediction Line", linewidth=2)

plt.xlabel("Total Bill")
plt.ylabel("Tip")
plt.title("Locally Weighted Regression")
plt.legend()
plt.show()