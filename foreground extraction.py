# -*- coding: utf-8 -*-
"""
Created on Mon Mar 19 00:15:27 2018

@author: dpr
"""
"""
can be used to exctract certain foreground for ex. faces
"""
import numpy as np
import cv2
from matplotlib import pyplot as plt

img = cv2.imread('F:/temp/myimage.jpg')
#img2 = cv2.imread('F:/temp/foreground-extraction.jpg')
#plt.imshow(img2)
mask = np.zeros(img.shape[:2],np.uint8)

bgdModel = np.zeros((1,65),np.float64)
fgdModel = np.zeros((1,65),np.float64)

rect = (450,275,350,400)

cv2.grabCut(img,mask,rect,bgdModel,fgdModel,5,cv2.GC_INIT_WITH_RECT)
mask2 = np.where((mask==2)|(mask==0),0,1).astype('uint8')
img = img*mask2[:,:,np.newaxis]
plt.imshow(img)
plt.colorbar()
plt.show()