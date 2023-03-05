import re
import sys

def checkPassport(l):
    count = 0
    a = ["byr:", "cid:", "ecl:", "eyr:", "hcl:", "hgt:", "iyr:", "pid:"]
    b = ["byr:", "ecl:", "eyr:", "hcl:", "hgt:", "iyr:", "pid:"]
    for passport in l:
        match = re.findall("(\w\w\w:)", passport)
        print(sorted(match))
        if sorted(match) == a or sorted(match) == b:
            count += 1
    print(count)

checkPassport([w for w in sys.stdin.read().split("\n\n")])