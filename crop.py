# -*- coding: utf-8 -*-
"""
Created on Fri Mar 16 13:08:27 2018

@author: dpr
"""
#will crop an image into a desired size

import cv2

def main():
    img= cv2.imread("F:/temp/download.jpg")
    imgpath = "F:/temp2/4.jpg"
    
    crop_img = img[90:200, 90:200]
    
    cv2.namedWindow("cropped",cv2.WINDOW_AUTOSIZE)
    cv2.imshow('cropped', crop_img)
    cv2.waitKey(0)
    cv2.destroyWindow("cropped")
    
    cv2.imwrite(imgpath , img)

if __name__ == "__main__":
    main()