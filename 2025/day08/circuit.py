import csv
import numpy as np
from sklearn.metrics import pairwise_distances_argmin_min
from scipy.spatial.distance import pdist, squareform

with open('input.txt', mode='r') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        array.append(row)

X = np.array(array, dtype=int)

distance_matrix = squareform(pdist(X, metric='euclidean'))

# Flatten the distance matrix and get indices
n = distance_matrix.shape[0]

# Get upper triangle indices (to avoid duplicates and diagonal)
triu_indices = np.triu_indices(n, k=1)
distances = distance_matrix[triu_indices]

# Get indices of 1000 smallest distances
k = min(1000, len(distances))
smallest_indices = np.argpartition(distances, k-1)[:k]
smallest_indices = smallest_indices[np.argsort(distances[smallest_indices])]

# Convert back to matrix coordinates
point_pairs = [(triu_indices[0][i], triu_indices[1][i]) for i in smallest_indices]
pair_distances = distances[smallest_indices]

res=[]
# collect results
for (i, j), dist in zip(point_pairs, pair_distances):
    res.append((int(i), int(j)))

# Group pairs into larger clusters
# based on a shared junction_box
clusters = []
used_pairs = set()

for idx, (i, j) in enumerate(res):
    if idx in used_pairs:
        continue
    
    # Start a new cluster with this pair
    cluster = {i, j}
    used_pairs.add(idx)
    
    # Keep expanding the cluster by finding pairs that share points
    changed = True
    while changed:
        changed = False
        for other_idx, (a, b) in enumerate(res):
            if other_idx in used_pairs:
                continue
            
            # Check if this pair shares a point with the current cluster
            if a in cluster or b in cluster:
                cluster.add(a)
                cluster.add(b)
                used_pairs.add(other_idx)
                changed = True
    
    clusters.append(sorted(list(cluster)))

# Sort clusters by size (largest first)
clusters.sort(key=len, reverse=True)

print(f"Found {len(clusters)} clusters")
for i, cluster in enumerate(clusters[:10]):  # Print first 10
    print(f"Cluster {i+1}: size={len(cluster)}, points={cluster[:10]}{'...' if len(cluster) > 10 else ''}")
