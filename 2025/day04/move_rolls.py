import numpy as np
from scipy.signal import convolve2d

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
        print(f"{rolls}")


array = np.array(list)

mask = np.ones([3,3])
mask[1,1] = 0

y = convolve2d(array, mask, mode='same',boundary='fill', fillvalue=0)

result = (y<4) & (array==1)

total = np.sum(result)
print(f"Total moved rolls: {total}")