import sys

def totalDistinctPaths(l):
    # 0 added to list to represent initial plug point
    #l = l + [0]
    l.sort(); maxjolt = l[-1]+3
    P = [0]*(maxjolt+1)
    P[0] = 1
    for item in l:
        P[item]=P[item-1]+P[item-2]+P[item-3]
    return P[l[-1]]

print(totalDistinctPaths([int(w) for w in f if w.strip() != ""]))