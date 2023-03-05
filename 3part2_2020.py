import sys

def isItATree(l, x, y):
    counterTree = 0
    counterPositionX = 0
    counterPositionY = 0

    while counterPositionY < len(l):
        counterPositionX %= len(l[counterPositionY])
        if (l[counterPositionY][counterPositionX] == "#"):
            counterTree += 1
        counterPositionX += x
        counterPositionY += y
    return counterTree

l = [w for w in sys.stdin.read().split()]
print(isItATree(l, 3, 1) * isItATree(l, 1, 1) * isItATree(l, 5, 1) * isItATree(l, 7, 1) * isItATree(l, 1, 2))
    