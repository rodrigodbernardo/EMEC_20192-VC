import cv2
import time

import numpy as np
from matplotlib import pyplot as plt
#import function

print("IFCE CAMPUS FORTALEZA - 2019.2\nVISÃO COMPUTACIONAL")
#time.sleep(2)
print("AUTOR: RODRIGO D B ARAUJO\t20162015010231")
#time.sleep(1)

while True:

    print("01 - MÉDIA")
    print("02 - MEDIANA")
    print("03 - GAUSSIANO")
    print("04 - LAPLACIANO")
    print("05 - PREWITT")
    print("06 - SOBEL")
    print("07 - HISTOGRAMA")
    print("08 - LIMIARIZAÇÃO")
    print("09 - EQUALIZAÇÃO DE HISTOGRAMA")
    print("10 - MULTILIMIARIZAÇÃO")
    op = input(">>>")

    if op == '1':
# idk why, but this question don't work. It was working before. I suspect that there's something with the file path.
        print("01 - MÉDIA")
        path = './base/01.jpeg'
        img = cv2.imread(path, 0)
        lin, col = img.shape
        #img_out = img_in.copy()

        kernel = 5
        mask = np.zeros((kernel,kernel), np.uint8)
        mask[:,:] = 1
        mLin, mCol = mask.shape
        mCorner = int((mLin - 1) / 2)

        img_out = np.zeros(((lin + mLin - 1), (col + mCol - 1)), np.uint8)
        img_out[mCorner:(lin + mCorner), mCorner:(col + mCorner)] = img

        for i in range (mCorner, lin + 1):
            for j in range (mCorner, col + 1):
                mSample = img_out[(i-mCorner):(i+mCorner +1),(j - mCorner): (j+mCorner+1)]
                img_out[i,j] = mSample.mean()

        img_out = img_out[mCorner:(lin+mCorner),mCorner:(col+mCorner)]

        cv2.imshow("01 - Mean Filter(original image)", img)
        cv2.imshow("Result 01 - Mean Filter", img_out)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    elif op == '2':
        print("02 - MEDIANA")
    elif op == '3':
        print("03 - GAUSSIANO")
    elif op == '4':
        print("04 - LAPLACIANO")
    elif op == '5':
        print("05 - PREWITT")
    elif op == '6':
        print("06 - SOBEL")
    elif op == '7':
        print("07 - HISTOGRAMA")
    elif op == '8':
        print("08 - LIMIARIZAÇÃO")
    elif op == '9':
        print("09 - EQUALIZAÇÃO DE HISTOGRAMA")
    elif op == '10':
        print("10 - MULTILIMIARIZAÇÃO")

    else:
        print("Invalido")
    time.sleep(2)
