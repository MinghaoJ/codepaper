def seekInputNodes(node):
    global inputNodes
    try:
        inputNodes
    except NameError:
        inputNodes = []
    inputNames = ['A','B','C','D','E','F','G']
    if len(node.inputs) == 0:
        inputNodes.append(node)
    else:
        map(seekInputNodes, node.inputs)
    for i in range(len(inputNodes)):
        inputNodes[i].name = inputNames[i]
    return inputNodes

def setInputs(inputs):
    global inputNodes
    for i in range(len(inputs)):
        inputNodes[i].value = inputs[i]
    return inputNodes

def evaluate(node, inp):
    if len(node.inputs) == 0:
        for n in inp:
            if n.name == node.name:
                return n.value
    else:
        return add(map(lambda x: evaluate(x, inp), node.inputs))

def add(args):
    if len(args) == 1:
        return args[0] * -1
    else:
        return args[0] + args[1]
