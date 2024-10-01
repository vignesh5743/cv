# -*- coding: utf-8 -*-
"""
Created on Wed Jul 10 11:58:34 2024

@author: Administrator
"""

import cv2
import matplotlib.pyplot as plt

img = cv2.imread("D:/photo.png", cv2.IMREAD_COLOR)

(h, w) = img.shape[:2]
center = (w // 2, h // 2)
M = cv2.getRotationMatrix2D(center, 50, 1.0)
rotated_img = cv2.warpAffine(img, M, (w, h))

flipped_horizontally = cv2.flip(img, 1)

flipped_vertically = cv2.flip(img, 0)

plt.figure(figsize=(20, 5))

plt.subplot(141)
plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
plt.title('Original Image')
plt.axis('off')

plt.subplot(142)
plt.imshow(cv2.cvtColor(rotated_img, cv2.COLOR_BGR2RGB))
plt.title('Rotated Image (45 degrees)')
plt.axis('off')

plt.subplot(143)
plt.imshow(cv2.cvtColor(flipped_horizontally, cv2.COLOR_BGR2RGB))
plt.title('Flipped Horizontally')
plt.axis('off')

plt.subplot(144)
plt.imshow(cv2.cvtColor(flipped_vertically, cv2.COLOR_BGR2RGB))
plt.title('Flipped Vertically')
plt.axis('off')

plt.show()
