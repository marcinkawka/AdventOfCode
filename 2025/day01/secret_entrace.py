
position = 50
number_of_zeros = 0
number_of_zeros_crossed = 0

with open("input.txt") as file:
    lines = file.readlines()    
    for line in lines:
        direction = line[0]
        value = int(line[1:])
        zeros_crossed = 0

        if direction == "R":
            new_position = (position + value) % 100
            zeros_crossed = (position + value) // 100
                
        elif direction == "L":
            flipped_position = (100-position)%100 
            zeros_crossed = (flipped_position + value)//100
        
            new_position = (position - value) % 100
            
        else:
            raise ValueError("Unknown direction")

        number_of_zeros_crossed += zeros_crossed
        position = new_position
        
        if position == 0:
            number_of_zeros += 1
        
print(f"Number of times final position is zero (task1): {number_of_zeros}")
print(f"Number of zeros crossed (task2): {number_of_zeros_crossed}")
