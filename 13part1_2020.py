import sys

def minWaitBus(list):
    timestamp = int(list[0][0])
    busLines = list[1]

    busWaitTimes = {}
    waitTimeList = []

    minWait = timestamp

    for bus in busLines:
        if bus == 'x':
            continue
        else:
            bus = int(bus)
            waitTime = bus -(timestamp % bus) #incorrect calculation
            if waitTime < minWait:
                minWait = waitTime
                minBusWaitName = bus
    return minBusWaitName * minWait

print(minWaitBus([w.strip('\n').split(',') for w in sys.stdin]))

