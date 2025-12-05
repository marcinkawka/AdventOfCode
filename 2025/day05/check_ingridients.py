
import portion as P

intervals = P.empty()
fresh_count = 0

with open('input.txt', 'r') as f:

    # loading intervals
    while True:
        range = f.readline().strip()
        if '-' not in range:
            break

        start, end = range.split('-')        
        intervals = intervals | P.closed(int(start), int(end))

    # checking values
    while True:
        value = f.readline().strip()
        if not value:
            break

        value = int(value)
        if value in intervals:
            print(f"{value} is in the ingredients list")
            fresh_count += 1
        else:
            print(f"{value} is NOT in the ingredients list")

print(f"Total fresh ingredients: {fresh_count}")