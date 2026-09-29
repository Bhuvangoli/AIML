import pandas as pd
import random

data = pd.read_csv("iris.csv", header=None)

data = data.values.tolist()

random.shuffle(data)

X = [row[0:4] for row in data]

train_size = int(0.6 * len(X))

X_train = X[:train_size]
X_test = X[train_size:]

print("Training data:", len(X_train))
print("Testing data:", len(X_test))

def euclidean_distance(point1, point2):
    distance = 0

    for i in range(len(point1)):
        distance = distance + (float(point1[i]) - float(point2[i])) ** 2

    return distance ** 0.5

def calculate_centroid(cluster):
    centroid = []

    for j in range(len(cluster[0])):
        total = 0

        for i in range(len(cluster)):
            total = total + float(cluster[i][j])

        centroid.append(total / len(cluster))

    return centroid

def kmeans(X, k):
    centroids = random.sample(X, k)

    for iteration in range(100):

        clusters = [[] for i in range(k)]

        for point in X:
            distances = []

            for centroid in centroids:
                distance = euclidean_distance(point, centroid)
                distances.append(distance)

            nearest = distances.index(min(distances))

            clusters[nearest].append(point)

        new_centroids = []

        for cluster in clusters:
            if len(cluster) > 0:
                new_centroids.append(calculate_centroid(cluster))
            else:
                new_centroids.append(random.choice(X))

        if new_centroids == centroids:
            break

        centroids = new_centroids

    return centroids

def predict_clusters(X, centroids):
    predictions = []

    for point in X:
        distances = []

        for centroid in centroids:
            distance = euclidean_distance(point, centroid)
            distances.append(distance)

        cluster = distances.index(min(distances))
        predictions.append(cluster)

    return predictions

k = 3

centroids = kmeans(X_train, k)

print("\nFinal Centroids:")

for i in range(len(centroids)):
    print("Cluster", i + 1, ":", centroids[i])

train_clusters = predict_clusters(X_train, centroids)

test_clusters = predict_clusters(X_test, centroids)

print("\nTraining Cluster Assignments:")
print(train_clusters)

print("\nTesting Cluster Assignments:")
print(test_clusters)

print("\nNumber of Testing Data Points in Each Cluster:")

for i in range(k):
    count = test_clusters.count(i)
    print("Cluster", i + 1, ":", count)