from scipy import ndimage

import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread("./data/base/holcocephala.jpg",0)
img = cv2.resize(img,(256,256))

kernel = np.ones((5,5),np.uint8)
img_grad = cv2.morphologyEx(img, cv2.MORPH_GRADIENT, kernel)
img_open = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)
img_close = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel)
img_DIL = cv2.morphologyEx(img, cv2.MORPH_DILATE, kernel)
img_ERO = cv2.morphologyEx(img, cv2.MORPH_ERODE, kernel)

cv2.imshow("grad",img_grad)
cv2.imshow("open",img_open)
cv2.imshow("close",img_close)
cv2.imshow("DIL",img_DIL)
cv2.imshow("ERO",img_ERO)


cv2.waitKey()
cv2.destroyAllWindows()