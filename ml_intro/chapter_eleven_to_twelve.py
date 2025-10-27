import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import scale
from sklearn.datasets import load_digits
from sklearn.cluster import KMeans
from sklearn import metrics
from sklearn.decomposition import PCA

# Load and scale data
digits = load_digits()
data = scale(digits.data)
y = digits.target

k = 10  # number of clusters
samples, features = data.shape


def bench_k_means(estimator, name, data):
    estimator.fit(data)
    print('%-9s\t%i\t%.3f\t%.3f\t%.3f\t%.3f\t%.3f\t%.3f'
          % (name, estimator.inertia_,
             metrics.homogeneity_score(y, estimator.labels_),
             metrics.completeness_score(y, estimator.labels_),
             metrics.v_measure_score(y, estimator.labels_),
             metrics.adjusted_rand_score(y, estimator.labels_),
             metrics.adjusted_mutual_info_score(y, estimator.labels_),
             metrics.silhouette_score(data, estimator.labels_,
                                      metric='euclidean')))


# Create and fit KMeans
clf = KMeans(n_clusters=k, init='k-means++', n_init=10, max_iter=300, random_state=42)
bench_k_means(clf, "KMeans", data)

# Reduce dimensions for visualization
pca = PCA(2)
reduced_data = pca.fit_transform(data)
reduced_centroids = pca.transform(clf.cluster_centers_)

# Plot clusters and centroids
plt.figure(figsize=(10, 8))
scatter = plt.scatter(reduced_data[:, 0], reduced_data[:, 1], c=clf.labels_, s=20, cmap='tab10', alpha=0.6)
plt.scatter(reduced_centroids[:, 0], reduced_centroids[:, 1], marker='x', s=200, linewidths=3, color='black',
            label='Centroids')
plt.title("KMeans Clustering of Digits Dataset (PCA-reduced to 2D)")
plt.xlabel("PCA Component 1")
plt.ylabel("PCA Component 2")
plt.legend()
plt.colorbar(scatter, label='Cluster Label')
plt.show()
