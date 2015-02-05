def negate(args):
    args = map(int, args)
    return -1 * args[0]

def add(args):
    args = map(int, args)
    return args[0] + args[1]

def sub(args):
    args = map(int, args)
    return args[0] - args[1]

def mul(args):
    args = map(int, args)
    return args[0] * args[1]

def div(args):
    args = map(int, args)
    return args[0] / args[1]

def fact(args):
    args = map(int, args)
    out = 1
    for i in range(1,args[0]+1):
        out *= i
    return out

fun_dict = {
    "neg": negate,
    "add": add,
    "sub": sub,
    "mul": mul,
    "div": div,
    "fact": fact
}
