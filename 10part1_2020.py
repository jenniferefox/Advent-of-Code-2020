from collections import Counter
import sys

def adaptorArray(l):
    # 0 added to list to represent initial plug point
    l = l + [0]
    l.sort()

    index = 0
    diffs = Counter()
    tail = iter(l); next(tail)
    for before, after in zip(l, tail):
        diffs[after - before] += 1
    
    # add 1 to diffs[3] to account for device's built-in adaptor 
    return diffs[1] * (diffs[3] + 1)

print(adaptorArray([int(w) for w in sys.stdin if w.strip() != ""]))