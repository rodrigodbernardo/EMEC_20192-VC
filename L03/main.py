###T03 - VC

#IZABELA LIBERATO
#RODRIGO D. BERNARDO

import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt
import pandas as pd

dataset = pd.read_csv("dataset.txt", sep = ' ', header = None)
#dataset.head()

x = dataset.iloc[:,:-1].values                                      #'x' armazenará os dados de cada imagem
y = dataset.iloc[:,-1].values                                       #'y' armazenará a ultima coluna, que contem os numeros referentes a cada imagem

#for i in range(y.size):
#    img = np.reshape(x[i,:],(35,35))
#    cv.imwrite("./data/base/im_{}-{}.jpg".format(i,y[i]),img.astype("uint8")*255)
#    print("Image {} saved successfully.".format(i))

img = np.reshape(x[0,:],(35,35))

huMoments = cv.HuMoments(cv.moments(img.astype("uint8")*255))
print(huMoments)
print(huMoments.shape)

#cv.imshow("image", img.astype("uint8")*255)
#cv.waitKey()
