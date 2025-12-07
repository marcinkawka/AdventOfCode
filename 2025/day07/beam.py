import numpy as np

conv_dict = {'.': 0, 
             '^': 1,
             'S':99,
             '|':2}

inv_dict = {v: k for k, v in conv_dict.items()}

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
            case 99:
                curr_beam_locations.add(col)
                break
            case 0:
                if col in prev_beam_locations:
                    mm[row, col] = 2
                    curr_beam_locations.add(col)
            case 1:
                if col in prev_beam_locations:
                    mm[row, col-1] = 2
                    mm[row, col+1] = 2
                    curr_beam_locations.add(col-1)
                    curr_beam_locations.add(col+1)
                    splits += 1
            case _:
                pass
    prev_beam_locations = curr_beam_locations
    curr_beam_locations = set()

#Print like a PRO
s = np.array2string(
    mm,
    formatter={'int_kind': lambda x: inv_dict[int(x)]}
)
print(s)
print(f"Splits: {splits}")