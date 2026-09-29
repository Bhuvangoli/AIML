import pandas as pd
import matplotlib.pyplot as plt
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.preprocessing import LabelEncoder

data = pd.read_csv("salaries.csv")

X = data.iloc[:, :-1]
y = data.iloc[:, -1]

encoders = {}

for column in X.columns:
    encoder = LabelEncoder()
    X[column] = encoder.fit_transform(X[column])
    encoders[column] = encoder

model = DecisionTreeClassifier(criterion="entropy", random_state=42)

model.fit(X, y)

print("Accuracy:", model.score(X, y))

plt.figure(figsize=(15, 10))

plot_tree(
    model,
    feature_names=X.columns,
    class_names=["0", "1"],
    filled=True
)

plt.show()