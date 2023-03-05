import re
import sys
from typing import NamedTuple

class Point(NamedTuple):
    x: int
    y: int

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Point(self.x - other.x, self.y - other.y)


def rotateWaypoint(direction, angle, currentWaypoint):
    #rotate coords right or left by given angle
    if angle == 0:
        return currentWaypoint
    newWaypoint = currentWaypoint
    adjAngle = angle % 360
    if adjAngle == 180:
        newWaypoint = Point(-newWaypoint[0], -newWaypoint[1])
    if direction == 'R':
        if adjAngle == 90:
            newWaypoint = Point(newWaypoint[1], -newWaypoint[0])
        if adjAngle == 270:
            newWaypoint = Point(-newWaypoint[1], newWaypoint[0])
    if direction == 'L':
        if adjAngle == 90:
            newWaypoint = Point(-newWaypoint[1], newWaypoint[0])
        if adjAngle == 270:
            newWaypoint = Point(newWaypoint[1], -newWaypoint[0])
    return newWaypoint

def calculateManhattenDistance(list):
    currentPoint = Point(0, 0)
    currentWaypoint = Point(10, 1)

    for element in list:
        print(element)
        instruction = element[0]
        distance = int(element[1:])
        if instruction == 'F':
            currentPoint += Point((distance * currentWaypoint[0]), (distance * currentWaypoint[1])) # does += work?
        elif instruction == 'L' or instruction == 'R':
            currentWaypoint = rotateWaypoint(instruction, distance, currentWaypoint)
        elif instruction == 'N':
            currentWaypoint += Point(0, distance)
        elif instruction == 'E':
            currentWaypoint += Point(distance, 0)
        elif instruction == 'S':
            currentWaypoint -= Point(0, distance)
        elif instruction == 'W':
            currentWaypoint -= Point(distance, 0)
        print(currentPoint)
        print(currentWaypoint)
    return abs(currentPoint[0]) + abs(currentPoint[1])

print(calculateManhattenDistance([w.strip('\n') for w in sys.stdin]))