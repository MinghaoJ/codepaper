import numpy as np
import cv2

def seekInputNodes(node):
    global inputNodes
    try:
        inputNodes
    except NameError:
        inputNodes = []
    inputNames = ['A','B','C','D','E','M','N','X']
    if len(node.inputs) == 0:
        inputNodes.append(node)
        return
    else:
        map(seekInputNodes, node.inputs)
    for i in range(len(inputNodes)):
        inputNodes[i].name = inputNames[i]
    return inputNodes
    
def seekFunctionNodes(node):
    global functionNodes
    try:
        functionNodes
    except NameError:
        functionNodes = []
    functionNames = ['F','G','H','I','Y','Z']
    if len(node.inputs) == 0:
        return
    else:
        functionNodes.append(node)
        map(seekFunctionNodes, node.inputs)
    for i in range(len(functionNodes)):
        functionNodes[i].name = functionNames[i]
    return functionNodes

def setInputs(inputs):
    global inputNodes
    for i in range(len(inputs)):
        inputNodes[i].value = inputs[i]
    return inputNodes

def setFunctions(functions):
    global functionNodes
    for i in range(len(functions)):
        functionNodes[i].value = functions[i]
    return functionNodes

def evaluate(node, inp):
    if len(node.inputs) == 0:
        for n in inp:
            if n.name == node.name:
                return n.value
    else:
        return node.function(map(lambda x: evaluate(x, inp), node.inputs))
