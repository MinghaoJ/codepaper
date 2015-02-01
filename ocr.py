from PIL import Image
from pytesseract import image_to_string
import numpy as np
import cv2

def parseText(node, imgFile):
    x,y,w,h = cv2.boundingRect(cv2.boxPoints(node.box))
    x,y,w,h = x+0.2*w,y+0.2*h,0.6*w,0.6*h
    
    img = cv2.imread(imgFile)
    img_grey = cv2.cvtColor(img[y:y+h, x:x+w], cv2.COLOR_BGR2GRAY)
    _,img_bin = cv2.threshold(img_grey,100,255,cv2.THRESH_BINARY)
    cv2.imwrite('tmp.jpg', img_bin)

    return image_to_string(Image.open('tmp.jpg'), config=' -psm 10') 