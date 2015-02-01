import GraphParse as gp
import functions as fn
import eval

head = gp.makeGraph()
head.function = fn.add
head.inputs[0].function = fn.fact
print eval.evaluate(head)