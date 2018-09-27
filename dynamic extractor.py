# -*- coding: utf-8 -*-
"""
Created on Mon Mar 19 14:01:41 2018

@author: dpr
"""

import numpy as np
import cv2

#cap = cv2.VideoCapture('F:/temp/people-walking.mp4')
cap = cv2.VideoCapture(0)
fgbg = cv2.createBackgroundSubtractorMOG2()

while(1):
    ret, frame = cap.read()

    fgmask = fgbg.apply(frame)
    
    kernel = np.ones((2,2),np.uint8)
    
    opening = cv2.morphologyEx(fgmask, cv2.MORPH_OPEN, kernel) #noise remover
    closing = cv2.morphologyEx(opening, cv2.MORPH_CLOSE, kernel)

 
    cv2.imshow('frame',frame)
    #cv2.imshow('frame',fgmask)
    cv2.imshow('fgmask',fgmask)
    cv2.imshow('filtered',opening)
    cv2.imshow('filtered2',closing)
    
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break
    

cap.release()
cv2.destroyAllWindows()