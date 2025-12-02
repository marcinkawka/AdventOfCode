
import csv

def detect_duplicates(number):
    digits = str(number)
    l_digists = len(digits)
    for l_substr in range(1, l_digists//2 + 1):
        substr= digits[0:l_substr]
        repetitions= 0
        for i in range(l_substr, l_digists, l_substr):
            if digits[i:i+l_substr] != substr:
                repetitions= 0
                break # not a repeating sequence of length l_substr 
            else:
                repetitions += 1
        if repetitions>0:
            print(f"Detected sequence: {number} = {substr} * {repetitions + 1}")
            return number
    return 0

duplicates = 0
# Read from file
with open('input.txt', 'r') as f:
    line = f.read().strip()  # Read entire content as one string
    
# Parse the single line
reader = csv.reader([line])  # Wrap in a list
for row in line.split(','):
    start,end = map(int, row.split('-'))
    for number in range(start, end + 1):
        duplicates += detect_duplicates(number)

print(f"Total duplicates found: {duplicates}")