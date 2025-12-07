
import numpy as np

i=0
el=[]

def check_numbers_size(filename='input.txt'):
    with open(filename, 'r') as f:
        while True:
            line = f.readline().strip()
            if not line:
                break
            elements = line.split(' ')
            if str(elements[0]).isnumeric():
                el.append(list(filter(lambda x: x>0, [len(e) for e in elements])))
    aa= np.array(el)
    sizes = np.max(aa, axis=0)
    return sizes

def line_splitter(line,dimensions)->list:
    elements = []
    current_element = ''
    pointer = 0    
    for el_len in dimensions:
        current_element = line[pointer:pointer+el_len]
        elements.append(current_element)
        pointer += el_len + 1  # +1 to skip the space
    return elements

dimensions = check_numbers_size()
all_rows = []
with open('input.txt', 'r') as f:
    while True:
        line = f.readline().rstrip('\n')
        if not line:
            break
        elements = line_splitter(line, dimensions)
        all_rows.append(elements)

actions=all_rows.pop(-1)
actions = list(map(lambda x: x.strip(), actions))

final_total=0
for col in range(dimensions.__len__()):
    if actions[col]=='*' :
        col_total = 1
    else:
        col_total = 0
    for digit in range(dimensions[col]):
        col_sum = 0
        for row in range(len(all_rows)) :
            if all_rows[row][col][digit].strip().isnumeric():
                col_sum = col_sum*10+int(all_rows[row][col][digit])
        match actions[col] :
            case '+':
                col_total += col_sum
            case '*':
                col_total *= col_sum
            case _:
                raise ValueError(f'Unknown operation: {actions[col]}')
    final_total += col_total
    
print(f"Final total is: {final_total}")