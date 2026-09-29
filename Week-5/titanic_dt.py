import pandas as pd
import matplotlib.pyplot as plt
from sklearn.tree import DecisionTreeClassifier, plot_tree

data = pd.read_csv("titanic.csv")

data = data.dropna()

data = data.drop(
    columns=["PassengerId", "Name", "Ticket", "Cabin"],
    errors="ignore"
)

X = data.drop("Survived", axis=1)
y = data["Survived"]

X = pd.get_dummies(X, dtype=int)

model = DecisionTreeClassifier(
    criterion="entropy",
    random_state=42
)

model.fit(X, y)

print("Accuracy:", model.score(X, y))

plt.figure(figsize=(20, 12))

plot_tree(
    model,
    feature_names=X.columns,
    class_names=["Not Survived", "Survived"],
    filled=True
)

plt.show()