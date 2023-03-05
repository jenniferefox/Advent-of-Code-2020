import re
import sys

def sumMappedValues(l):
    mem = {}
    for item in l:
        if item.startswith('mask = '):
            mask = list(item.strip('mask = '))
            xs = []
            ones = []
            for index, maskBit in enumerate(mask):
                if maskBit == 'X':
                    xs.append(index)
                if maskBit == '1':
                    ones.append(index)
        if item.startswith('mem['):
            m = re.match(r'mem\[(\d+)\] = (\d+)', item)
            bnum = list(format(int(m.group(1)),'036b'))
            for one in ones:
                bnum[one] = '1'
            for x in range(2**len(xs)):
                for position, bit in zip(xs, f'{x:0{len(xs)}b}'):
                    bnum[position] = bit
                mem[''.join(bnum)] = int(m.group(2))
    return sum(mem.values())

print(sumMappedValues([w.strip('\n') for w in sys.stdin]))
    