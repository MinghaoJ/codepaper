def negate(args):
    return -1 * args[0]

def add(args):
    return args[0] + args[1]

def sub(args):
    return args[0] - args[1]

def mul(args):
    return args[0] * args[1]

def div(args):
    return args[0] / args[1]

def fact(args):
    out = 1
    for i in range(1,args[0]+1):
        out *= i
    return out