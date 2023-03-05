import sys

def eval(list1):        
    pc = 0
    acc = 0
    while pc < len(list1):
        op, rand = list1[pc]
        list1[pc] = ["trp", 0]
        if op == "trp":
            return "infinite"
        elif op == "nop":
            pc += 1
        elif op == "acc":
            acc += int(rand)
            pc += 1
        elif op == "jmp":
            pc += int(rand)
        else:
            print("unrecognised")
    return acc

def findError(l):
    for num, (op, rand) in enumerate(l):
        if op == "jmp":
            
            cpy = l[:]
            cpy[num]=["nop", rand]
            op = "nop"
            
        elif op == "nop":
            cpy = l[:]
            cpy[num]=["jmp", rand]
        
        else:
            continue
        print(eval(cpy))

print(findError([w.split(" ") for w in sys.stdin.read().strip().split("\n")]))