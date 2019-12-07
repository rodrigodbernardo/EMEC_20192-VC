import cv2
import numpy as np
from matplotlib import pyplot as plt


img = cv2.imread('./base/02.jpeg',0)

cv2.imshow("Image",img)