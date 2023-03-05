import sys
from collections import namedtuple
from timeit import timeit

class Grid:
    def __init__(self, width, height, content):
        #need to do this at start?
        self.width = width
        self.height = height
        self.content = content

    def __getitem__(self, key):
        x, y = key
        if 0 <= x < self.width and 0 <= y < self.height:
            return self.content[y * self.width + x]
        else:
            return None
    
    def __setitem__(self, key, value):
        x, y = key
        if 0 <= x < self.width and 0 <= y < self.height:
            self.content[y * self.width + x] = value
        else:
            raise IndexError("Grid index out of range")

    def copy(self):
        return Grid(self.width, self.height, self.content[:])

    def occupied_neighbours(self, x, y):
        occupied = 0
        for j in range(-1, 2):
            for i in range(-1, 2):
                if i == 0 and j == 0:
                    continue
                if self[(x + i, y + j)] == '#':
                    occupied += 1
        return occupied

    def occupied(self):
        return self.content.count('#')

def step(front, back):
    changed = False
    for y in range(front.height):
        for x in range(front.width):
            if front[(x, y)] == '.':
                continue

            nbrs = front.occupied_neighbours(x, y)
            if front[(x, y)] == 'L' and nbrs == 0:
                back[(x, y)] = '#'
                changed = True
            elif front[(x, y)] == '#' and nbrs >= 4:
                back[(x, y)] = 'L'
                changed = True
            else:
                back[(x, y)] = front[(x, y)]
    return changed

def countOccupiedSeats(grid):
    front = grid.copy()
    back  = grid.copy()

    generation = 0
    while step(front, back):
        front, back = back, front
        generation += 1
    
    print(f"Generations: {generation}")
    return front.occupied()

lines = [l.strip() for l in sys.stdin]
height = len(lines)
width  = len(lines[0])
grid = Grid(width, height, [c for l in lines for c in l])

env = {'countOccupiedSeats': countOccupiedSeats,'grid': grid}
print(f"{timeit('countOccupiedSeats(grid)', number=10, globals=env)}")
print(countOccupiedSeats(grid))
