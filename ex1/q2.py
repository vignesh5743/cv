
import cv2
import numpy as np
import matplotlib.pyplot as plt
array = np.random.randint(256, size=(8, 8)) 

print(array)
plt.imshow(array,cmap="gray")
plt.show()