import sys

def isItATree(f):
    counterPosition = 0
    counterTree = 0
    for item in f:
        if (item[counterPosition] == "#"):
            counterTree += 1
        counterPosition += 3
        counterPosition %= len(item)-1           
    print(counterTree)
    
isItATree(sys.stdin)