import numpy as np
import cv2

inputNodes = []
def seekInputNodes(node):
    if len(node.inputs) == 0:
        inputNodes.append(node)
        return
    else:
        for n in node.inputs:
            seekInputNodes(n)
        return inputNodes

def setInputs(inputs, inputsNodes):
    for i in range(len(inputs)):
        inputNodes[i].value = inputs[i]

def evaluate(node):
    if len(node.inputs) == 0:
        return node.value
    else:
        return node.function(map(evaluate, node.inputs))
