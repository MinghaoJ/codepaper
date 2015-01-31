import numpy as np
import cv2

def edge_node_mask(im):
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

def parse_contours(in_mask):
    parsed = []
    found, _ = cv2.findContours(in_mask,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

    for el in found:
        if len(el) > 100:
            parsed.append(el)

    return parsed

(node_mask, edge_mask) = edge_node_mask(cv2.imread('test4.png'))

parsed_nodes = parse_contours(node_mask)

print "Total nodes:"
print len(parsed_nodes)

parsed_edges = parse_contours(edge_mask)
	
print "Total edges:"
print len(parsed_edges)


cv2.drawContours(node_mask, parsed_nodes, -1, (255,255,255), 3)
cv2.drawContours(edge_mask, parsed_edges, -1, (255,255,255), 3)
	
cv2.imwrite('output.png',edge_mask) 
cv2.imwrite('output2.png',node_mask)
