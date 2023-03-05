import re

def subtractTuples(tuple1, tuple2):
    subX = tuple1[0] - tuple2[0]
    subY = tuple1[1] - tuple2[1]
    return (subX, subY)

def addTuples(tuple1, tuple2):
    addX = tuple1[0] + tuple2[0]
    addY = tuple1[1] + tuple2[1]
    return (addX, addY)

def calculateManhattenDistance(list):
    currentPoint = (0, 0)
    currentDirection = 90 #default facing East (this need to never go above 270)
    for element in list:
        match = re.search("(\w)(\d+)", element)
        if match.group(1) == 'F':
            if currentDirection == 0:
                currentPoint = addTuples(currentPoint, (0, int(match.group(2))))
                print(match.group(1))
            if currentDirection == 90:
                currentPoint = addTuples(currentPoint , (int(match.group(2)), 0))
            if currentDirection == 180:
                currentPoint = subtractTuples(currentPoint, (0, int(match.group(2))))
            if currentDirection == 270:
                currentPoint = subtractTuples(currentPoint, (int(match.group(2)), 0))
        if match.group(1) == 'N':
            print(match.group(2))
            currentPoint = addTuples(currentPoint, (0, int(match.group(2))))
        if match.group(1) == 'S':
            currentPoint = subtractTuples(currentPoint, (0, int(match.group(2))))
        if match.group(1) == 'E':
            currentPoint = addTuples(currentPoint, (int(match.group(2)), 0))
        if match.group(1) == 'W':
            currentPoint = subtractTuples(currentPoint, (int(match.group(2)), 0))
        if match.group(1) == 'L':
            currentDirection += -int(match.group(2))
            currentDirection = abs(currentDirection % 360)
        if match.group(1) == 'R':
            currentDirection += int(match.group(2))
            currentDirection = abs(currentDirection % 360)
        print(currentPoint)
        print(currentDirection)
    return abs(currentPoint[0]) + abs(currentPoint[1])

with open("C:/Users/jenni/OneDrive/Documents/Coding/Advent of Code/input12.txt") as f:
    l = [w.strip('\n') for w in f]
    print(l)
    print(calculateManhattenDistance(l))
