import sys

def eval(l):
    pc = 0
    acc = 0
    while pc < len(l):
        op, rand = l[pc]
        l[pc] = ("trp", 0)
        if op == "trp":
            return acc
        elif op == "nop":
            pc += 1
        elif op == "acc":
            acc += int(rand)
            pc += 1
        elif op == "jmp":
            pc += int(rand)
        else:
            print("unrecognised")
    return None

print(eval([w.split(" ") for w in sys.stdin.read().split("\n")]))