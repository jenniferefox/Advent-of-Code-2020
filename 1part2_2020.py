import itertools
import sys

def pairwise(iterable):
    a, b = itertools.tee(iterable)
    next(b, None)
    return zip(a, b)

    l = [int(w) for w in sys.stdin]

list = [
    sum(itertools.islice(l, i, i+3))
    for i in range(len(l) - 3 + 1)
]
count = sum(1 for i, j in pairwise(list) if i < j)
print(count)