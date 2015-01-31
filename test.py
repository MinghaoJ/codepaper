import numpy as np
import cv2

red_lower_bound1 = np.array([0,50,150])
red_upper_bound1 = np.array([10,255,191])
red_lower_bound2 = np.array([170,50,150])
red_upper_bound2 = np.array([179,255,191])

im = cv2.imread('test3.png')
im_grey = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
im = cv2.cvtColor(im, cv2.COLOR_BGR2HSV)

edgemask = cv2.bitwise_or(cv2.inRange(im,red_lower_bound1,red_upper_bound1),cv2.inRange(im,red_lower_bound2,red_upper_bound2))

(_,allmask) = cv2.threshold(im_grey,90,255,cv2.THRESH_BINARY_INV)
nodemask = cv2.bitwise_and(allmask,cv2.bitwise_not(edgemask))

#contours, hierarchy = cv2.findContours(nodemask,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

#cv2.drawContours(nodemask, contours, -1, (255,100,100), 3)
#lines = cv2.HoughLinesP(nodemask,20,1,1)

#print len(lines)



cv2.imwrite('output.png',edgemask) 
cv2.imwrite('output2.png',nodemask) 