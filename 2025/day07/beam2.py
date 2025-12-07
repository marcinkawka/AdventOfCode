import numpy as np

conv_dict = {'.': 0, 
             '^': -9,
             'S':-99,
             '|':2}


def check_size(filename='input.txt'):
    with open(filename) as f:
        lines = f.readlines()
    return len(lines), len(lines[0].strip())

dimensions = check_size()

converter = {i: lambda s: conv_dict[s] for i in range(dimensions[1])}

mm = np.genfromtxt('input.txt', 
                delimiter=1,
                converters=converter,
                usecols=np.arange(dimensions[1]),
                dtype=int)

prev_beam_locations = set()
curr_beam_locations = set()
splits= 0

for row in range(mm.shape[0]):
    for col in range(mm.shape[1]):
        match mm[row, col]:
            case -99:
                curr_beam_locations.add(col)
                mm[row, col] = 1 #starting point
                break
            case -9:
                if col in prev_beam_locations:
                    mm[row, col-1] += mm[row-1, col]
                    mm[row, col+1] += mm[row-1, col]
                    curr_beam_locations.add(col-1)
                    curr_beam_locations.add(col+1)
                    splits += 1
            case _:
                if col in prev_beam_locations:
                    mm[row, col] += mm[row-1, col]
                    curr_beam_locations.add(col)
    prev_beam_locations = curr_beam_locations
    curr_beam_locations = set()

print(mm)
print(f"Sum of last row (total number of paths : {np.sum(mm[-1, :])}")
print(f"Splits: {splits}")