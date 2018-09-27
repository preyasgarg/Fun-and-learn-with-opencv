# -*- coding: utf-8 -*-
"""
Created on Sun Mar 18 01:42:19 2018

@author: dpr
"""
"""
will filter out specific color form video frame
also can be used as a mask.
"""
import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while(1):
    _, frame = cap.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    
    lower_red = np.array([30,150,50])
    upper_red = np.array([255,255,180])
    
    mask = cv2.inRange(hsv, lower_red, upper_red)
    res = cv2.bitwise_and(frame,frame, mask= mask)
    mask_inv = cv2.bitwise_not(mask)
    res_inv = cv2.bitwise_and(frame,frame, mask= mask_inv)
    cv2.imshow('frame',frame)
    cv2.imshow('mask',mask)
    cv2.imshow('res',res)
    cv2.imshow('mask_inv',mask_inv)
    cv2.imshow('res_inv',res_inv)
    
    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break

cv2.destroyAllWindows()
cap.release()
