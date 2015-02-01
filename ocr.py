from pytesser import *
import cv2

def parseText(node):
    cornerPoints = cv2.boxPoints(node)
    img_crop = filteredImage[cornerPoints[0][1]:cornerPoints[2][1], cornerPoints[1][0]:cornerPoints[3][0]]
    text = image_to_string(img_crop)
    return text
    
    
print parseText(node)
 