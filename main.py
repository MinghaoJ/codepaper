import GraphParse as gp
import functions as fn
import eval

head, graph = gp.makeGraph()
head.function = fn.add
head.inputs[0].function = fn.sub
eval.seekInputNodes(head, graph)