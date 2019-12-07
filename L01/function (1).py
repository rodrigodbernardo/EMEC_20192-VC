import cv2
import numpy as np
from matplotlib import pyplot as plt

def meanFilter(image, kernel):
    mask = np.zeros