import re
import sys

def countValidPassword(f):
        counter = 0
        for item in f:
            match = re.search("(\d+)-(\d+)\s(\w):\s(\w+)", item)
            print(item)
            position1 = match.group(1) 
            position2 = match.group(2)
            character = match.group(3)
            phrase = match.group(4)
            
            if ((phrase[int(position1)-1] == character and not phrase[int(position2)-1] == character) or (phrase[int(position2)-1] == character and not phrase[int(position1)-1] == character)):
                counter += 1

                print(phrase[int(position1)-1])
                print(phrase[int(position2)-1])
                print(counter)
            
        print(counter)

countValidPassword(sys.stdin)