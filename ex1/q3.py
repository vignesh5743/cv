# -*- coding: utf-8 -*-
"""
Created on Wed Jul 10 10:43:08 2024

@author: Administrator
"""

import cv2
import matplotlib.pyplot as plt

img = cv2.imread('D:/bike.jpg')

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

ret,thresh = cv2.threshold(gray,70,255,0)

imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

plt.subplot(131),plt.imshow(imgRGB,cmap = 'gray'),plt.title('Original Image'), plt.axis('off')
plt.subplot(132),plt.imshow(gray,cmap = 'gray'),plt.title('Grayscale Image'),plt.axis('off')
plt.subplot(133),plt.imshow(thresh,cmap = 'gray'),plt.title('Binary Image'),plt.axis('off')
plt.show()