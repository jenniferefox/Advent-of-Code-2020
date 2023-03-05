import sys
from collections import Counter

def yesQs(l):
    yeses = 0
    for group in l:
        people = group.split("\n")
        answers = Counter()
        for person in people:
            answers.update(set(person))
        
        for k, v in answers.most_common():
            if v < len(people): 
                break
            else:
                yeses += 1
    return yeses

my_list = ["fm\nif"]
l = [w for w in sys.stdin.read().split("\n\n")]
print(len(l))
print(yesQs(l))
