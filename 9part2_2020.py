import sys

def findSum(l):
    total = 14144619
    sum = 0
    lo = 0
    hi = 0
    while (hi < len(l) and sum < total) or sum > total:
        if sum < total:
            sum += l[hi]
            hi += 1
        else:
            sum -=l[lo]
            lo += 1
    if sum == total:
        window = l[lo:hi]
        return max(window) + min(window)

print(findSum([int(w) for w in sys.stdin.read().strip().split("\n")]))
