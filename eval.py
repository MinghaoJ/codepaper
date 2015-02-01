def evaluate(node):
    if len(node.inputs) == 0:
        if !node.value
            self.value = input("Enter a value for " + node.name + " ")
        return self.value
    else:
        return node.function(map(evaluate, node.inputs))
