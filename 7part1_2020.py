
test1 = ["light red bags contain 1 bright white bag, 2 muted yellow bags.", "dark orange bags contain 3 bright white bags, 4 muted yellow bags.", "bright white bags contain 1 shiny gold bag.", "muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.", 
    "shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.", "dark olive bags contain 3 faded blue bags, 4 dotted black bags.", "vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.", "faded blue bags contain no other bags.", "dotted black bags contain no other bags."]

from collections import defaultdict
import re
import sys

def findContainers2(bags):
    nodes_to_visit = ["shiny gold"]
    coloursContainingGold = set()
    while len(nodes_to_visit) > 0:
        current_node = nodes_to_visit.pop()
        for c in bags[current_node]:
            if c not in coloursContainingGold:
                coloursContainingGold.add(c)
                nodes_to_visit.append(c)
    return len(coloursContainingGold)

bags = defaultdict(list)
for l in sys.stdin:
    bag, contains = l.strip(". \n").split(" bags contain ", 1)
    if contains == "no other bags":
        continue
    for bag_and_count in contains.split(", "):
        m = re.match(r'^(\d+) (.+) bags?$', bag_and_count)
        assert m, bag_and_count
        bags[m[2]].append(bag)
print(findContainers2(bags))



    
        



    # = [w.split(" bags contain ") for w in f.read().split("\n")] # also split w by ", "
    #print(l)
    #countgoldBagContainers(l)


