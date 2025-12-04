import numpy as np
from scipy.signal import convolve2d

def print_array(arr)->None:
    for row in arr:
        print(''.join('@' if cell == 1 else '.' for cell in row))
    print()


list = []
with open('input.txt', 'r') as f:
    while True:
        rolls = f.readline()
        if not rolls:
            break
        else:
            rolls = rolls.strip()

        row = [1 if c == '@' else 0 for c in rolls]
        list.append(row)

array = np.array(list)
mask = np.ones([3,3])
mask[1,1] = 0
total = 0

while True:
    y = convolve2d(array, mask, mode='same',boundary='fill', fillvalue=0)
    result = (y<4) & (array==1)

    removed = np.sum(result)
    if removed == 0:
        break
    else:
        total += removed
    array = np.where(result, 0, array)

    print_array(array)

print(f"Total moved rolls: {total}")