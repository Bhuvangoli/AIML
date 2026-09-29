import pandas as pd
import numpy as np

def calculate_entropy(target_col):
    elements, counts = np.unique(target_col, return_counts=True)
    probabilities = counts / counts.sum()
    entropy = -np.sum(probabilities * np.log2(probabilities))
    return entropy

def calculate_information_gain(data, split_attribute_name, target_name):
    total_entropy = calculate_entropy(data[target_name])
    vals, counts = np.unique(data[split_attribute_name], return_counts=True)
    weighted_entropy = 0
    for i in range(len(vals)):
        subset = data[data[split_attribute_name] == vals[i]]
        subset_entropy = calculate_entropy(subset[target_name])
        weighted_entropy += (counts[i] / np.sum(counts)) * subset_entropy
    information_gain = total_entropy - weighted_entropy
    return information_gain

def build_decision_tree(data, original_data, features,
                        target_attribute_name, parent_node_class=None):
    if len(np.unique(data[target_attribute_name])) <= 1:
        return np.unique(data[target_attribute_name])[0]
    elif len(data) == 0:
        return np.unique(original_data[target_attribute_name])[
            np.argmax(np.unique(original_data[target_attribute_name],
                                return_counts=True)[1])]
    elif len(features) == 0:
        return parent_node_class
    else:
        np.unique(original_data[target_attribute_name])[
            np.argmax(np.unique(original_data[target_attribute_name],
                                return_counts=True)[1])]
        item_values = [
            calculate_information_gain(data, feature, target_attribute_name)
            for feature in features
        ]
        best_feature_index = np.argmax(item_values)

        best_feature = features[best_feature_index]
        tree = {best_feature: {}}
        features = [i for i in features if i != best_feature]

        for value in np.unique(data[best_feature]):
            subset_data = data.where(data[best_feature] == value).dropna()
            subtree = build_decision_tree(
                subset_data,
                original_data,
                features,
                target_attribute_name,
                parent_node_class
            )
            tree[best_feature][value] = subtree

        return tree

def print_tree(tree, indent=0):
    for key, value in tree.items():
        print(' ' * indent + str(key))
        if isinstance(value, dict):
            print_tree(value, indent + 1)
        else:
            print(' ' * (indent + 1) + 'Prediction: ' + str(value))

file_path = "/content/Day Ski AirTemp Humidity Wind Nate..."
df = pd.read_csv("enjoysport.csv")
features = df.columns[:-1].tolist()
target_col = df.columns[-1]
decision_tree = build_decision_tree(df, df, features, target_col)
print_tree(decision_tree)
