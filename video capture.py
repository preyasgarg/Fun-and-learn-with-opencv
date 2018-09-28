# -*- coding: utf-8 -*-
"""
Created on Fri Mar 16 20:05:19 2018

@author: dpr
"""
"""
will exit only when q is pressed instead of esc, will convert colored feed to grayscale.
"""
import cv2
import numpy as np

cap = cv2.VideoCapture(0)
#record = cv2.VideoWriter_fourcc(*'XVID')
#out = cv2.VideoWriter('myvideo.avi', record, 20.0, (640,480))
while(True):
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    #out.write(frame)
    cv2.imshow('frame', frame)
    cv2.imshow('grayframe', gray)
    
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    
cap.release()
#out.release()
cv2.destroyAllWindows()