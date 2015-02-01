import numpy as np
import cv2

def seekInputNodes(node, graph):
    inputNodes = []
    inputNames = ['A','B','C','D','E','F','G']
    if len(node.inputs) == 0:
        inputNodes.append(node)
        return
    else:
        for n in node.inputs:
            seekInputNodes(n, graph)
    for i in range(len(inputNodes)):
        inputNodes[i].name = inputNames[i]
        print graph
        print inputNames[i]
        print inputNodes[i][0]
        cv2.putText(graph, inputNames[i], inputNodes[i][0], FONT_HERSHEY_SIMPLEX, 10, (0,0,255))
    return inputNodes

def setInputs(inputs, inputsNodes):
    for i in range(len(inputs)):
        inputNodes[i].value = inputs[i]

def evaluate(node):
    if len(node.inputs) == 0:
        return node.value
    else:
        return node.function(map(evaluate, node.inputs))
