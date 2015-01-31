import numpy as np
import cv2

red_lower_bound1 = np.array([0,25,90])
red_upper_bound1 = np.array([10,255,191])
red_lower_bound2 = np.array([170,25,90])
red_upper_bound2 = np.array([179,255,191])

im = cv2.imread('test4.png')
im_grey = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
im = cv2.cvtColor(im, cv2.COLOR_BGR2HSV)

edgemask = cv2.bitwise_or(cv2.inRange(im,red_lower_bound1,red_upper_bound1),cv2.inRange(im,red_lower_bound2,red_upper_bound2))
(_,allmask) = cv2.threshold(im_grey,90,255,cv2.THRESH_BINARY_INV)
nodemask = cv2.bitwise_and(allmask,cv2.bitwise_not(edgemask))

nodes, hierarchy = cv2.findContours(nodemask,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
cv2.drawContours(nodemask, nodes, -1, (255,100,100), 3)
edges, hierarchy = cv2.findContours(edgemask,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

parsed_nodes = []
parsed_edges = []

for n in nodes :
	if (len(n) > 100) :
		parsed_nodes.append(n)
		print n[len(n)-1]
	
print "Total nodes:"
print len(parsed_nodes)

for c in edges :
	if (len(c) > 100) :
		parsed_edges.append(c)
		print c[len(c)-1]
	
print "Total edges:"
print len(parsed_edges)

#lines = cv2.HoughLinesP(parsed_edges,1,np.pi/180,100,100,100)
#for x1,y1,x2,y2 in lines[0]:
#    cv2.line(edgemask,(x1,y1),(x2,y2),(0,255,0),2)

cv2.drawContours(nodemask, parsed_nodes, -1, (255,255,255), 3)
cv2.drawContours(edgemask, parsed_edges, -1, (255,255,255), 3)
	
cv2.imwrite('output.png',edgemask) 
cv2.imwrite('output2.png',nodemask) 