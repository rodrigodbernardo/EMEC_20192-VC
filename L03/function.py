import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt
import pandas as pd
import pprint
import os

def saveData():
    a =0
    a0 = 1
    a1 = 1
    a2 = 1
    a3 = 1
    a4 = 1
    a5 = 1
    a6 = 1
    a7 = 1
    a8 = 1
    a9 = 1
    b=0
    b0 = 1
    b1 = 1
    b2 = 1
    b3 = 1
    b4 = 1
    b5 = 1
    b6 = 1
    b7 = 1
    b8 = 1
    b9 = 1

    for i in range(y.size):
        img = np.reshape(x[i,:],(35,35))
        if (i < 670):
            if (y[i] == 0):          
                a = a0
                a0 += 1
            elif (y[i] == 1):
                a = a1
                a1 += 1
            elif (y[i] == 2):
                a = a2
                a2 += 1
            elif (y[i] == 3):
                a = a3
                a3 += 1
            elif (y[i] == 4):
                a = a4
                a4 += 1
            elif (y[i] == 5):
                a = a5
                a5 += 1
            elif (y[i] == 6):
                a = a6
                a6 += 1
            elif (y[i] == 7):
                a = a7
                a7 += 1
            elif (y[i] == 8):
                a = a8
                a8 += 1
            elif (y[i] == 9):
                a = a9
                a9 += 1
            cv.imwrite("./data/test/{}/{}.jpg".format(y[i],a),img.astype("uint8")*255)
        else:
            if (y[i] == 0):          
                b = b0
                b0 += 1
            elif (y[i] == 1):
                b = b1
                b1 += 1
            elif (y[i] == 2):
                b = b2
                b2 += 1
            elif (y[i] == 3):
                b = b3
                b3 += 1
            elif (y[i] == 4):
                b = b4
                b4 += 1
            elif (y[i] == 5):
                b = b5
                b5 += 1
            elif (y[i] == 6):
                b = b6
                b6 += 1
            elif (y[i] == 7):
                b = b7
                b7 += 1
            elif (y[i] == 8):
                b = b8
                b8 += 1
            elif (y[i] == 9):
                b = b9
                b9 += 1
            cv.imwrite("./data/train/{}/{}.jpg".format(y[i],b),img.astype("uint8")*255)
        
        print("Image {} saved successfully.".format(i))

dataset = pd.read_csv("dataset.txt", sep = ' ', header = None)

x = dataset.iloc[:,:-1].values
y = dataset.iloc[:,-1].values   #'y' armazenará a ultima coluna, que contem os numeros referentes a cada imagem

saveData()


