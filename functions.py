def my_i(n):
    if n == "1":
        return 1
    if n == "2":
        return 2
    if n == "3":
        return 3
    if n == "4":
        return 4
    if n == "5":
        return 5
    if n == "6":
        return 6
    if n == "7":
        return 7
    if n == "8":
        return 8
    if n == "9":
        return 9
    return n


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
