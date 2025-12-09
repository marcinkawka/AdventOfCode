"""
Ugly brutforce solution for puzzle2
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

max_x = np.max(red_points[:, 0])+1
max_y = np.max(red_points[:, 1])+1

grid = np.zeros((max_x + 1, max_y + 1), dtype=int)


# filling green points between red points
for i in range(len(red_points)):
    for j in range(i + 1, len(red_points)):
        x1, y1 = red_points[i]
        x2, y2 = red_points[j]
        if x1 == x2:
            for y in range(min(y1, y2), max(y1, y2) + 1):
                grid[x1, y] = 3  # Mark green points with a different value
        elif y1 == y2:
            for x in range(min(x1, x2), max(x1, x2) + 1):
                grid[x, y1] = 3  # Mark green points with a different value

for point in red_points:
    grid[point[0], point[1]] = 1

#filling internals
for i in range(max_x + 1):
    inside = False
    for j in range(max_y + 1):
        if grid[i, j] > 0 and not inside:
            # enetering internals
            inside = not inside
        elif inside and grid[i, j] == 0:
            grid[i, j] = 4  # Mark internal points with a different value
        elif grid[i, j] > 0 and np.sum(grid[i, j+1:]) == 0 and inside:
            # exiting internals
            inside = not inside

print("Initial Grid:")
print(grid.T)

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

# Iterate over pairs
for i, j, distance in pairs_with_distances:
    point1 = red_points[i]
    point2 = red_points[j]
    # print(f"Points {i} and {j}: {point1} to {point2}, distance: {distance}")
    x1, y1 = point1
    x2, y2 = point2
    x_min, x_max = min(x1, x2), max(x1, x2)
    y_min, y_max = min(y1, y2), max(y1, y2)
    
    rectangle_region = grid[x_min:x_max+1, y_min:y_max+1]
    has_zeros = np.any(rectangle_region == 0)
    
    if has_zeros:
        print(f"Rectangle between {point1} and {point2} contains zeros")
    else:
        print('__'*20)
        print(f"Rectangle between {point1} and {point2} is fully filled")
        print(f"I have found a final Rectangle with Area {x2-x1} x {y2-y1} = {(abs(x2 - x1)+1) * (abs(y2 - y1)+1)}")
        break