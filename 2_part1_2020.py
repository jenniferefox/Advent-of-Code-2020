import re
import sys

def countValidPassword(f):
        counter = 0
        for item in f:
            match = re.search("(\d+)-(\d+)\s(\w):\s(\w+)", item)
            print(item)
            min = match.group(1) 
            max = match.group(2)
            character = match.group(3)
            phrase = match.group(4)
            
            findMatch = re.findall(character, phrase)
            if (len(findMatch) >= int(min) and len(findMatch) <= int(max)):
                counter += 1
                print(len(findMatch))
                print(min)
                print(max)    
                print(counter)
            
        print(counter)

countValidPassword(sys.stdin)