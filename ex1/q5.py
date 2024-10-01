# -*- coding: utf-8 -*-
"""
Created on Wed Jul 10 11:41:01 2024

@author: Administrator
"""
import matplotlib.pyplot as plt

import cv2

img = cv2.imread("D:/photo.png", cv2.IMREAD_COLOR)

dimensions = img.shape

print(f"Dimensions of the image: {dimensions}")
plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
plt.title(f"Dimensions: {dimensions[1]} x {dimensions[0]} x {dimensions[2]}")
#plt.axis('off')
plt.show()