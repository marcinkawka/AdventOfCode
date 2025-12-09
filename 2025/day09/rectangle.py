import csv
import numpy as np
from scipy.spatial.distance import pdist, squareform

array = []
with open('input.txt', mode='r') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        array.append(row)

X = np.array(array, dtype=int)

distance_matrix = squareform(pdist(X, metric='cityblock'))

max_distance = np.max(distance_matrix)
max_indices = np.where(distance_matrix == max_distance)
point1_idx, point2_idx = max_indices[0][0], max_indices[1][0]

print(f"Maximum distance: {max_distance}")
print(f"Between points {point1_idx} and {point2_idx}")
print(f"Point 1: {X[point1_idx]}")
print(f"Point 2: {X[point2_idx]}")
rectangle_area = (np.abs(X[point1_idx][0] - X[point2_idx][0])+1) * (np.abs(X[point1_idx][1] - X[point2_idx][1])+1)
print(f"Rectangle area formed by these points: {rectangle_area}")