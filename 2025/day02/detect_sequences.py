
import csv

def detect_duplicates(number):
    digits = str(number)
    l_digists = len(digits)
    if l_digists % 2 != 0:
        return 0
    half1 = int(digits[:l_digists//2])
    half2 = int(digits[l_digists//2:])
    if half1 == half2:
        print(f"Detected sequence: {number} = {half1} | {half2}")
        return number
    else:
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