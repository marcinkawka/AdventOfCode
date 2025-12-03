
import numpy as np

total = 0
with open('input.txt', 'r') as f:
    batteries = f.readlines()
    for battery in batteries:
        digits = 12
        number = 0
        i_digit = 0
        while digits > 0:
            # print(f" Looking at {battery[i_digit:-(digits+1)]} ")
            batt =  np.array([int(d) for d in battery[i_digit:-(digits)]])
            digit = np.max(batt)
            i_digit += np.argmax(batt)+1
            # print(f"Digit: {digit} from {batt} at index {i_digit}")
            number += digit * (10 ** (digits-1))
            digits -= 1
        print(f"In: {battery[:-1]} -> {number} ")
        total+= number

print(f"Total battery value: {total}")