import cv2
import time

import numpy as np
from matplotlib import pyplot as plt
import function

print("IFCE CAMPUS FORTALEZA - 2019.2\nVISÃO COMPUTACIONAL")
#time.sleep(2)
print("AUTOR: RODRIGO D B ARAUJO\t20162015010231")
#time.sleep(1)
a=1
while a == 1:

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
    op = input(">>> ")

    #01 - MEAN FILTER
    if op == '1':
        
        print("01 - MÉDIA")
        img = cv2.imread('./base/WE.jpg', 0)
    
        result = function.meanFilter(img)

        cv2.imwrite("./result/01.jpg",result)
        print("Salvando resultado em ~/result/01.jpg")

        cv2.imshow("01 - Mean Filter(original image)", img)
        cv2.imshow("Result 01 - Mean Filter", result)

        cv2.waitKey(0)
        cv2.destroyAllWindows()

    #02 - MEDIAN FILTER
    elif op == '2':

        print("02 - MEDIANA")
        img = cv2.imread('./base/redfield.jpg',0)
        
        result = function.medianFilter(img)

        cv2.imwrite("./result/02.jpg",result)
        print("Salvando resultado em ~/result/02.jpg")

        cv2.imshow("02 - Median Filter(original image)", img)
        cv2.imshow("Result 02 - Median Filter", result)

        cv2.waitKey(0)
        cv2.destroyAllWindows()

    #03 - GAUSSIAN FILTER
    elif op == '3':
        print("03 - GAUSSIANO")

        img = cv2.imread("./base/redfield.jpg",0)
        
        result = function.gaussianFilter(img)

        cv2.imwrite("./result/03.jpg",result)
        print("Salvando resultado em ~/result/03.jpg")

        cv2.imshow("03 - Gaussian Filter(original image)", img)
        cv2.imshow("Result 03 - Gaussian Filter", result)

        cv2.waitKey(0)
        cv2.destroyAllWindows()

    #04
    elif op == '4':
        print("04 - LAPLACIANO")

        img = cv2.imread("./base/holcocephala.jpg",0)

        result = function.laplacianFilter(img)

        cv2.imwrite("./result/04.jpg", result)
        print("Salvando resultado em ~/result/04.jpg")

        cv2.imshow("04 - Laplacian Filter(original image)", img)
        cv2.imshow("Result 04 - Laplacian Filter", result)

        cv2.waitKey(0)
        cv2.destroyAllWindows()
    
    #05
    elif op == '5':
        print("05 - PREWITT")
        
        print("O que deseja aplicar?")
        print("1-Filtro vertical")
        print("2-Filtro horizontal")
        option = input(">>>")


        img = cv2.imread("./base/coco.jpg",0)

        result = function.prewitt(img,option)

        cv2.imwrite("./result/05.jpg", result)
        print("Salvando resultado em ~/result/05.jpg")

        cv2.imshow("05 - PREWITT(original image)", img)
        cv2.imshow("05 - PREWITT", result)

        cv2.waitKey(0)
        cv2.destroyAllWindows()
    
    #06
    elif op == '6':
        print("06 - SOBEL")
        print("O que deseja aplicar?")
        print("1-Filtro vertical")
        print("2-Filtro horizontal")
        option = input(">>>")


        img = cv2.imread("./base/redfield.jpg",0)

        result = function.sobel(img,option)

        cv2.imwrite("./result/06.jpg", result)
        print("Salvando resultado em ~/result/06.jpg")

        cv2.imshow("06 - SOBEL(original image)", img)
        cv2.imshow("06 - SOBEL", result)

        cv2.waitKey(0)
        cv2.destroyAllWindows()

    #07
    elif op == '7':
        print("07 - HISTOGRAMA")

        img = cv2.imread("./base/mario.jpg",0)

        result = function.histogram(img)

        cv2.imwrite("./result/07.jpg", result)
        print("Salvando resultado em ~/result/07.jpg")

        #cv2.imshow("07 - HISTOGRAMA(original image)", img)
        cv2.imshow("07 - HISTOGRAMA", result)

        cv2.waitKey(0)
        cv2.destroyAllWindows()
    
    #08
    elif op == '8':
        print("08 - LIMIARIZAÇÃO")
        img = cv2.imread("./base/slug.jpg",0)
        
        
        #threshold = int(input("Definir limiar[0-255]: "))

        result = function.thresholding(img)

        cv2.imwrite("./result/08.jpg", result)
        print("Salvando resultado em ~/result/08.jpg")

        cv2.imshow("08 - LIMIARIZAÇÃO(original image)", img)
        cv2.imshow("08 - LIMIARIZAÇÃO", result)

        cv2.waitKey(0)
        cv2.destroyAllWindows()
    
    #09
    elif op == '9':
        print("09 - EQUALIZAÇÃO DE HISTOGRAMA")
        img = cv2.imread("./base/solid.jpg",0)

        result = function.equalization(img)

        cv2.imwrite("./result/09.jpg", result)
        print("Salvando resultado em ~/result/09.jpg")

        cv2.imshow("09 - EQUALIZAÇÃO DE HISTOGRAMA(original image)", img)
        cv2.imshow("09 - EQUALIZAÇÃO DE HISTOGRAMA", result)

        cv2.waitKey(0)
        cv2.destroyAllWindows()
    
    #10
    elif op == '10':
        print("10 - MULTILIMIARIZAÇÃO")
        img = cv2.imread("./base/solid.jpg",0)
        

    else:
        print("Invalido")
    
    a=0    
