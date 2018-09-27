# -*- coding: utf-8 -*-
"""
Created on Sat Mar 17 00:01:41 2018

@author: dpr
"""

import cv2
import numpy as np
import matplotlib.pyplot as mpl
def main():
    img= cv2.imread("F:/temp/download.jpg", cv2.IMREAD_COLOR)
    imgpath = "F:/temp2/4.jpg"
    cv2.line(img, (5,5), (100,100), (134,156,56), 10)
    cv2.rectangle(img, (15,34), (134,125), (134,15,200), 5)
    cv2.circle(img, (178,132), 40, (134,156,250), -1)
    pts = np.array([[100,50],[90,80],[50,67],[34,21]], np.int32)
    pts = pts.reshape((-1,1,2))
    cv2.polylines(img, [pts], True, (0,250,255), 6)
    font = cv2.FONT_HERSHEY_SIMPLEX
    cv2.putText(img, 'preyas', (34,56), font, 1, (0,0,235), 4, cv2.LINE_AA)
    cv2.namedWindow("source window",cv2.WINDOW_AUTOSIZE)
    cv2.imshow('source window', img)
    cv2.waitKey(0)
    cv2.destroyWindow("source window")
    
    #cv2.imwrite(imgpath , img)

if __name__ == "__main__":
    main()