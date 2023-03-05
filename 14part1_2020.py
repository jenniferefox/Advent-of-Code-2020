import re
import sys

def sumMappedValues(l):
    mem = {}
    for item in l:
        if item.startswith('mask = '):
            item = item.strip('mask = ')
            mask = [w for w in item]
            print(mask)
        if item.startswith('mem['):
            #exec(item)
            m = re.match(r'mem\[(\d+)\] = (\d+)', item)
            bnum = format(int(m.group(2)),'b')
            bnum = [y for y in bnum]
            while len(bnum) != 36:
                bnum.insert(0, '0')
            print(bnum)
            counter = 0
            for bit in mask:
                if bit == '0' or bit == '1':
                    bnum[counter] = bit
                counter += 1
            bnum = ''.join(bnum)
            mem[m.group(1)] = int(bnum, 2)
    return sum(mem.values())

print(sumMappedValues([w.strip('\n') for w in sys.stdin]))
    