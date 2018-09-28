# -*- coding: utf-8 -*-
"""
Created on Sat Mar 17 23:05:00 2018

@author: dpr
"""

import cv2
import numpy as np

def main():
    img= cv2.imread("F:/temp/bookpage.jpg", cv2.IMREAD_COLOR)

    #img = cv2.imread('bookpage.jpg')
    grayscaled = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    retval, threshold = cv2.threshold(img, 12, 255, cv2.THRESH_BINARY)
    retval, threshold1 = cv2.threshold(grayscaled, 12, 255, cv2.THRESH_BINARY)
    threshold2 = cv2.adaptiveThreshold(grayscaled, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 115, 1)
    retval2,threshold3 = cv2.threshold(grayscaled,125,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
    cv2.imshow('original',img)
    cv2.imshow('threshold',threshold)
    cv2.imshow('threshold1',threshold1)
    cv2.imshow('threshold2',threshold2)
    cv2.imshow('threshold3',threshold3)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
if __name__ == "__main__":
    main()