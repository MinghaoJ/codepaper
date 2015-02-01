def seekInputNodes(node)
    inputNodes = []
    if len(node.inputs) == 0:
        inputNodes.append(node)
    else:
        map(seekInputs, node.inputs)
    return inputNodes

def setInputs(inputs)
    for i in range(len(inputs)):
        inputNodes[i].value = inputs[i]

def evaluate(node):
    if len(node.inputs) == 0:
        return node.value
    else:
        return node.function(map(evaluate, node.inputs))