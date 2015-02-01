def evaluate(node):
    if len(node.inputs) == 0:
        return input("Enter a value for " + node.name + " ")
    else:
        return node.function(map(evaluate, node.inputs))
