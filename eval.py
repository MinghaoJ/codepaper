def evaluate(node):
    if len(node.inputs) == 0:
        if (not node.value):
            node.value = input("Enter a value for " + node.text + " ")
        return node.value
    else:
        return node.function(map(evaluate, node.inputs))
