def seekInputNodes(node)
    inputNodes = []
    inputNames = ['A','B','C','D','E','F','G']
    if len(node.inputs) == 0:
        inputNodes.append(node)
    else:
        map(seekInputs, node.inputs)
    for i in range(len(inputNodes)):
        inputNodes[i].name = inputNames[i]
    return inputNodes

def setInputs(inputs, inputsNodes)
    for i in range(len(inputs)):
        inputNodes[i].value = inputs[i]

def evaluate(node):
    if len(node.inputs) == 0:
        return node.value
    else:
        return node.function(map(evaluate, node.inputs))