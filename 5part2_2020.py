import sys

def parseSeatID(string):
    table = str.maketrans("BFRL", "1010")
    x = string.translate(table)
    seatNum = int(x, 2)
    return seatNum


l = sorted(parseSeatID(line) for line in sys.stdin)
new_list = range(0, 967)
x = list(set(new_list) - set(l))
x.sort()

for s, seatID in enumerate(l):
    if s == len(l)-1:
        continue
    if l[s+1] - l[s] == 2:
        print(l[s]+1)
