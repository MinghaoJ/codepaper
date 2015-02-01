import numpy as np
import cv2
import GraphCapture
import ocr
import eval

class Node:
    
    def __init__(self, function, name, box):
        self.function = function
        self.value = None
        self.name = name
        self.text = None
        self.box = box
        self.inputs = []

class Edge:

    def __init__(self, n1, n2):
        self.links = [n1, n2]

def addInputs(node):
    global node_boxes
    global edge_boxes
    global imgFile
    n = Node(None, '', node)
    n.text = ocr.parseText(n, imgFile)
    n.inputs = map(addInputs, makeBranches(node))
    return n
    
def makeBranches(node):
    global node_boxes
    global edge_boxes
    global imgFile
    branches = []
    for e in edges:
        if (node == e.links[0] and node[0][0] > e.links[1][0][0]):
            branches.append(e.links[1])
        if (node == e.links[1] and node[0][0] > e.links[0][0][0]):
            branches.append(e.links[0])
    return branches

def getRightMostNode():
    global node_boxes
    global edge_boxes
    global imgFile
    max = node_boxes[0][0][0]
    maxNode = None
    for x in range(1,len(node_boxes)):
        if node_boxes[x][0][0] > max:
            max = node_boxes[x][0][0]
            maxNode = node_boxes[x]
    return maxNode
    
def makeGraph():
    global node_boxes
    global edge_boxes
    global imgFile
    global edges
    (node_boxes, edge_boxes, imgFile, graph) = GraphCapture.getElements('image.jpg', 100, 200)
    edges = []
    for e in edge_boxes:
        n1 = None
        n2 = None
        for n in node_boxes:
            if(cv2.rotatedRectangleIntersection(n,e)[0] == 1):
                if(n1):
                    n2 = n
                else:
                    n1 = n
            if(n1 and n2):
                edges.append(Edge(n1,n2))
                break
    head = addInputs(getRightMostNode())
    eval.seekInputNodes(head, graph)
    cv2.imwrite('output.jpg', graph) 
    return head, graph