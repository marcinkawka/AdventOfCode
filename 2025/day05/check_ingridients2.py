
import portion as P

intervals = P.empty()
fresh_count = 0

with open('input.txt', 'r') as f:

    # loading intervals
    while True:
        igr_range = f.readline().strip()
        if '-' not in igr_range:
            break

        start, end = igr_range.split('-')        
        intervals = intervals | P.closed(int(start), int(end))

# Does not fit in memory
# fresh_count = len(list(P.iterate(intervals, step=1)))

# So we do it manually
for interval in intervals:
    fresh_count += len(range(interval.lower, interval.upper + 1))

print(f"There are  {fresh_count} possible fresh ingredients ")