import sys

def sumTo2020(l):
    visited = [False] * 2021
    for i in range(len(l)):
        for j in range(i + 1, len(l)):
            z = 2020 - l[i] - l[j]
            if z > 0 and visited[z]:
                return l[i], l[j], z
        visited[l[i]] = True

l = [int(w) for w in sys.stdin.read().split()]
x, y, z = sumTo2020(l)
print(x * y * z)


