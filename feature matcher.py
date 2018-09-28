# -*- coding: utf-8 -*-
"""
Created on Mon Mar 19 13:26:59 2018

@author: dpr
"""
"""
will match an object contained in 2 different images without caring about orientation
"""
import numpy as np
import cv2
import matplotlib.pyplot as plt

img1 = cv2.imread('F:/temp/opencv-feature-matching-template.jpg',0)
img2 = cv2.imread('F:/temp/opencv-feature-matching-image.jpg',0)
orb = cv2.ORB_create()
kp1, des1 = orb.detectAndCompute(img1,None)
kp2, des2 = orb.detectAndCompute(img2,None)
bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)
matches = bf.match(des1,des2)
matches = sorted(matches, key = lambda x:x.distance)
img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10],None, flags=2)
plt.imshow(img3)
plt.show()