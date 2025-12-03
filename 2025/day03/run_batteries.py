
import numpy as np

total = 0
with open('input.txt', 'r') as f:
    batteries = f.readlines()
    for battery in batteries:
        batt =  np.array([int(d) for d in battery[:-2]])
        tens = np.max(batt)
        i_tens = np.argmax(batt)
        ones = max(battery[i_tens +1:]) 
        print(f"In: {battery[:-1]} -> {tens}{ones} ")
        total+= int(tens)*10 + int(ones)

print(f"Total battery value: {total}")