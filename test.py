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

_,allmask = cv2.threshold(im_grey,191,255,cv2.THRESH_BINARY_INV)
nodemask = cv2.bitwise_and(cv2.threshold(im_grey,191,255,cv2.THRESH_BINARY_INV),cv2.bitwise_not(edgemask))

cv2.imwrite('output.png',edgemask) 
cv2.imwrite('output2.png',nodemask) 
