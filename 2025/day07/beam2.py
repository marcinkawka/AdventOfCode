import numpy as np

conv_dict = {'.': 0, 
             '^': 1,
             'S':2,
             '|':2}

inv_dict = {v: k for k, v in conv_dict.items()}

def check_size(filename='input.txt')-> tuple[int,int]:
    with open(filename) as f:
        lines = f.readlines()
    return len(lines), len(lines[0].strip())

def count_timelines(mm, starting_col=0):
    prev_beam_locations = set()
    curr_beam_locations = set()
    paths= 1
    # print(f"Starting new timeline count on sub-matrix of shape {mm.shape}")
    for row in range(mm.shape[0]):
        for col in range(starting_col, mm.shape[1]):
            match mm[row, col]:
                case 0:
                    if col in prev_beam_locations:
                        mm[row, col] = 2
                        curr_beam_locations.add(col)
                case 2:
                    curr_beam_locations.add(col)
                case 1:
                    if col in prev_beam_locations:
                        # Here we split into two sub-problems
                        mm[row,col]=0
                        
                        mm_child=mm.copy()
                        mm_child[row,col-1]=2
                        paths +=count_timelines(mm_child[row:, :], starting_col=col-1)
                        
                        mm_child=mm.copy()
                        mm_child[row,col+1]=2
                        paths +=count_timelines(mm_child[row:, :], starting_col=col+1)
                        paths -=1  # remove double count of current path
                        # print(f"Split at row {row}, col {col}. Total paths so far: {paths}")
                        break
                case _:
                    pass
        prev_beam_locations = curr_beam_locations
        curr_beam_locations = set()
    return paths


dimensions = check_size()
print(f"Dimensions: {dimensions}")
converter = {i: lambda s: conv_dict[s] for i in range(dimensions[1])}

mm = np.genfromtxt('input.txt', 
                delimiter=1,
                converters=converter,
                usecols=np.arange(dimensions[1]),
                dtype=int)

total_timeline_count = count_timelines(mm)

print(f"Paths: {total_timeline_count}")