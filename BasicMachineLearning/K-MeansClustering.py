# 1. Import necessary libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.datasets import make_blobs
from sklearn.cluster import KMeans

# 2. Generate synthetic data for clustering
X, y = make_blobs(n_samples=300, centers=4, cluster_std=0.60, random_state=0)

# 3. Visualize the synthetic data
plt.scatter(X[:, 0], X[:, 1], s=30)
plt.title("Synthetic Data for K-Means Clustering")
plt.xlabel("Feature 1")
plt.ylabel("Feature 2")
plt.show()

# 4. Perform K-Means Clustering
kmeans = KMeans(n_clusters=4)  # Specify the number of clusters
kmeans.fit(X)

# 5. Get the cluster labels and centroids
labels = kmeans.labels_
centroids = kmeans.cluster_centers_

# 6. Visualize the clustered data
plt.scatter(X[:, 0], X[:, 1], c=labels, s=30, cmap='viridis')
plt.scatter(centroids[:, 0], centroids[:, 1], c='red', s=200, alpha=0.75, label='Centroids')
plt.title("K-Means Clustering Results")
plt.xlabel("Feature 1")
plt.ylabel("Feature 2")
plt.legend()
plt.show()
