import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt
import pandas as pd

dataset = pd.read_csv("dataset.txt", sep = ' ', header = None)
dataset.head()

x = dataset.iloc[:,:-1].values
y = dataset.iloc[:,-1].values
print (y)

for i in range(y.size):
    img = np.reshape(x[i,:],(35,35))
    cv.imwrite("./data/base/im-{}_{}.jpg".format(y[i],i),img.astype("uint8")*255)
    print("Image {} saved successfully.".format(i))

#cv.imshow("image", img.astype("uint8")*255)
#cv.waitKey()
