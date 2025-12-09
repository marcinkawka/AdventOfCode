"""
Ugly brutforce solution for puzzle2
This is part1, part 2 is in SQL file
"""

import csv
import numpy as np
from scipy.spatial.distance import pdist, squareform

array = []
with open('input.txt', mode='r') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        array.append(row)

red_points = np.array(array, dtype=int)

distance_matrix = squareform(pdist(red_points, metric='cityblock'))

# Get indices of upper triangle (to avoid duplicates)
indices = np.triu_indices(len(distance_matrix), k=1)

# Create pairs with their distances
pairs_with_distances = []
for idx in range(len(indices[0])):
    i, j = indices[0][idx], indices[1][idx]
    distance = distance_matrix[i, j]
    pairs_with_distances.append((i, j, distance))

# Sort by distance in descending order
pairs_with_distances.sort(key=lambda x: x[2], reverse=True)
print("Possible rectangles sorted by distance")

with open('output_rectangles.csv', mode='w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    # Iterate over pairs
    for i, j, distance in pairs_with_distances:
        point1 = red_points[i]
        point2 = red_points[j]
        # print(f"Points {i} and {j}: {point1} to {point2}, distance: {distance}")
        
        x1, y1 = point1
        x2, y2 = point2
        x_min, x_max = min(x1, x2), max(x1, x2)
        y_min, y_max = min(y1, y2), max(y1, y2)
        
        area = (abs(x_max - x_min)+1) * (abs(y_max - y_min)+1)
        # print(f"{i+1},{j+1},{int(distance)},{area}")
        writer.writerow([i+1, j+1, int(distance), area])