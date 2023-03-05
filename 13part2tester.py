def findt():
    start = 17
    t = 0
    while True:
        t += start
        print(t)
        if (t+2) % 13 == 0 and (t+3) % 19 == 0:
            return t

def findt2(sched):
    offset, longest_interval = max(enumerate(sched), key=lambda kvp: kvp[1])

    t = longest_interval - offset
    while any((t + off) % bus != 0 for off, bus in enumerate(sched)):
        t += longest_interval
    return t

print(findt2([67, 1, 7, 59, 61]))
print(findt2([67, 7, 1, 59, 61]))
print(findt2([1789, 37, 47, 1889]))
