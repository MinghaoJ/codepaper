import numpy as np
import cv2

def maskNodesAndEdges(im):
    red_lower_bound1 = np.array([0,25,90])
    red_upper_bound1 = np.array([10,255,191])
    red_lower_bound2 = np.array([170,25,90])
    red_upper_bound2 = np.array([179,255,191])

    im_grey = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
    im = cv2.cvtColor(im, cv2.COLOR_BGR2HSV)

    edge_mask = cv2.bitwise_or(cv2.inRange(im,red_lower_bound1,red_upper_bound1),cv2.inRange(im,red_lower_bound2,red_upper_bound2))
    (_,allmask) = cv2.threshold(im_grey,90,255,cv2.THRESH_BINARY_INV)
    node_mask = cv2.bitwise_and(allmask,cv2.bitwise_not(edge_mask))
    return (node_mask, edge_mask)

def parseContours(in_mask):
    parsed = []
    _, found, _ = cv2.findContours(in_mask,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

    for el in found:
        if len(el) > 100:
            parsed.append(el)

    return parsed

def consolidateNodes(boxes):
    def area(box):
        return box[1][0] * box[1][1]
    l = len(boxes)
    matched = map(lambda x: False, range(l))
    unique_boxes = []
    for i in range(l):
        if (matched[i] == True):
            continue
        for j in range(i + 1, l):
            if (matched[j] == True):
                continue
            if (cv2.rotatedRectangleIntersection(boxes[i],boxes[j])[0] == 2):
                matched[j] = matched[i] = True
                if (area(boxes[i]) < area(boxes[j])):
                    unique_boxes.append(boxes[j])
                else:
                    unique_boxes.append(boxes[i])
                break
    return unique_boxes

node_mask, edge_mask = maskNodesAndEdges(cv2.imread('test4.png'))

parsed_nodes = parseContours(node_mask)
parsed_edges = parseContours(edge_mask)

edge_boxes = map(cv2.minAreaRect, parsed_edges)
node_boxes = map(cv2.minAreaRect, parsed_nodes)

node_boxes = consolidateNodes(node_boxes)

# DEBUG
edge_points = map(np.int0, map(cv2.boxPoints, edge_boxes))
node_points = map(np.int0, map(cv2.boxPoints, node_boxes))

cv2.drawContours(node_mask, edge_points, -1, (255,255,255), 3)
cv2.drawContours(node_mask, node_points, -1, (255,255,255), 3)

cv2.imwrite('output.png',edge_mask) 
cv2.imwrite('output2.png',node_mask)

print "Total nodes:"
print len(parsed_nodes)
print "Total edges:"
print len(parsed_edges)