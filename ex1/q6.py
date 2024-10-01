# -*- coding: utf-8 -*-
"""
Created on Wed Jul 10 11:49:21 2024

@author: Administrator
"""

import cv2
import matplotlib.pyplot as plt

img = cv2.imread("D:/photo.png", cv2.IMREAD_COLOR)

x, y, w, h = 50, 50, 200, 200 

cropped_img = img[y:y+h, x:x+w]

new_size = (100, 100)

resized_img = cv2.resize(cropped_img, new_size)

plt.figure(figsize=(15, 5))

plt.subplot(131)
plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
plt.title('Original Image')

plt.subplot(132)
plt.imshow(cv2.cvtColor(cropped_img, cv2.COLOR_BGR2RGB))
plt.title('Cropped Image')

plt.subplot(133)
plt.imshow(cv2.cvtColor(resized_img, cv2.COLOR_BGR2RGB))
plt.title('Resized Image')

plt.show()
