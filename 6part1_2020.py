import sys

def yesQs(l):
    count = 0
    for group in l:
       replaceN = set(group.replace("\n", ""))
       count += len(replaceN)      
    print(count)

l = [w for w in sys.stdin.read().split("\n\n")]
yesQs(l)
