import sys

def parseSeatID(string):
    table = str.maketrans("BFRL", "1010")
    x = string.translate(table)
    seatNum = int(x, 2)
    return seatNum

print(max(parseSeatID(line) for line in sys.stdin))
