import sys

def findCyberWeakness(l):
    index = 25
    for item in l[25:]:
        index += 1
        counter = 0
        potentials = set()
        preamble = l[(index-26):index]
        for i in preamble:
            if i < item:
                potentials.add(i)
            #print(potentials)
        for potential in sorted(potentials):
            if (item - potential) in sorted(potentials): # think about duplicates? how would these be treated
                #print(item)
                break
            else:
                counter += 1
            if counter == len(potentials):
                return item

print(findCyberWeakness([int(w) for w in sys.stdin.read().strip().split("\n")]))
