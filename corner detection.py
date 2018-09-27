# -*- coding: utf-8 -*-
"""
Created on Mon Mar 19 12:02:48 2018

@author: dpr
"""

import numpy as np
import cv2

img = cv2.imread('F:/temp/corner-detection.png')
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
gray = np.float32(gray)

corners = cv2.goodFeaturesToTrack(gray, 10000, 0.01, 100)
corners = np.int0(corners)

for corner in corners:
    x,y = corner.ravel()
    cv2.circle(img,(x,y),3,255,-1)
    
cv2.imshow('Corner',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
