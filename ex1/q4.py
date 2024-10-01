# -*- coding: utf-8 -*-
"""
Created on Wed Jul 10 11:20:54 2024

@author: Administrator
"""

import cv2
import matplotlib.pyplot as plt

img = cv2.imread("D:/photo.png", cv2.IMREAD_COLOR)

r=img[:,:,0]
g=img[:,:,1]
b=img[:,:,2]

#cv2.imshow("red", r)
#cv2.imshow("green", g)
#cv2.imshow("blue", b)




plt.subplot(131),plt.imshow(r,cmap='Reds'),plt.title('Red')
plt.subplot(132),plt.imshow(g,cmap='Greens'),plt.title('Green')
plt.subplot(133),plt.imshow(b, cmap='Blues'),plt.title('Blue')
plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()