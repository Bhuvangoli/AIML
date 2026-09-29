import pandas as pd

data = pd.read_csv("data.csv")

attributes = data.iloc[:, :-1].values
target = data.iloc[:, -1].values

hypothesis = []

for i in range(len(attributes[0])):
    hypothesis.append("0")

for i in range(len(attributes)):
    if target[i] == "Yes" or target[i] == 1:
        for j in range(len(attributes[i])):
            if hypothesis[j] == "0":
                hypothesis[j] = attributes[i][j]
            elif hypothesis[j] != attributes[i][j]:
                hypothesis[j] = "?"

print("Final Hypothesis:")
print(hypothesis)