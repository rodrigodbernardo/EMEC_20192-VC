#   IFCE 2019.2 - VISAO COMPUTACIONAL
#   RODRIGO DOUGLAS BERNARDO DE ARAUJO
#
#   LISTA O2 - 

from time import sleep
from os import system
#from PIL import Image
from scipy import ndimage

import cv2
import numpy
import matplotlib.pyplot as plt
import function as func
#import imageio
mouseClick = []


print("IFCE CAMPUS FORTALEZA - 2019.2\nVISÃO COMPUTACIONAL")
#sleep(2)
print("AUTOR: RODRIGO D B ARAUJO\t20162015010231")
#sleep(1)

def on_mouse(event, x, y, flags, params):
    if event == cv2.EVENT_LBUTTONDOWN:
        print ('Seed: ' + str(x) + ', ' + str(y), img[y,x])
        clicks.append((y,x))

a=0
while a==0:

    print("01 - TRANSLAÇÃO, ROTAÇÃO E ESCALA")
    print("02 - TRANSFORMADA HAAR")
    print("03 - EROSÃO E DILATAÇÃO")
    print("04 - GRADIENTE MORFOLÓGICO EM TONS DE CINZA")
    print("05 - CRESCIMENTO DE REGIÃO - IMAGEM BINÁRIA")
    print("06 - CRESCIMENTO DE REGIÃO - IMAGEM EM TONS DE CINZA")
    print("07 - MÉTODO K-MEANS PARA SEGMENTAÇÃO")
    print("08 - TRANSFORMADA HOUGH")
    print("09 - TRANSFORMADA DE WATERSHED")
    print("10 - WAVELET E FOURIER")
    op = input(">>>")

    system('cls||clear')

    if op == '1':
        print("01 - TRANSLAÇÃO, ROTAÇÃO E ESCALA\n")
        op1 = input("Qual operação deseja executar?\n1 - Translação\n2 - Rotação\n3 - Escala\n>>> ")
        
        # cv2.imread() nao é compativel com as imagens .gif do banco de imagens binarias.

        img = plt.imread('./data/binary/tree-20.gif')
        #print (img)

        if op1 == '1':
            print("1 - Translação\n")

            result = func.translation(img)

            #cv2 nao pode salvar .gif

            #cv2.imwrite('./data/result/1-1_translation.jpg',result)
            plt.imsave('./data/result/1-1_translation.gif',result)
            print('Salvando resultado em ~/data/result/1-1_translation.gif')

            cv2.imshow('1-1 Translation (original image)',img)
            cv2.imshow('1-1 Translation (result)',result)

        elif op1 == '2':
            print("2 - Rotação\n")
            angle = int(input("Defina um angulo de rotação: "))

            result = func.rotation(img,angle)
            
            cv2.imwrite('./data/result/1-2_rotation.jpg',result)
            print('Salvando resultado em ~/data/result/1-2_rotation.jpg')

            cv2.imshow('1-1 Rotation (original image)',img)
            cv2.imshow('1-1 Rotation (result)',result)

        elif op1 == '3':
            print("3 - Escala\n")
            scale = int(input("Defina uma escala percentual (%): "))

            result = func.scale(img,scale)

            cv2.imwrite('./data/result/1-3_scale.jpg',result)
            print('Salvando resultado em ~/data/result/1-3_scale.jpg')

            cv2.imshow('1-3 Scale (original image)',img)
            cv2.imshow('1-3 Scale (result)',result)

        else:
            print("Opção inválida")

        cv2.waitKey()
        cv2.destroyAllWindows()

    elif op == '2':
        print("02 - TRANSFORMADA HAAR")

        img = cv2.imread('./data/base/holcocephala.jpg',0)
        
    elif op == '3':

        img = cv2.imread('./data/base/holcocephala.jpg',0)

        print("03 - EROSÃO E DILATAÇÃO")

        op3 = input("Qual operação deseja executar?\n1 - Erosão\n2 - Dilatação\n>>> ")
        element = input("Escolha um elemento estruturante.\n1 - Quadrado 3x3\n2 - Quadrado 5x5\n3 - Cruz\n>>> ")

        if element == '1':
            elementStr = 'square3'
        elif element == '2':
            elementStr = 'square5'
        elif element == '3':
            elementStr = 'cross'

        if op3 == '1':
            print('3.1 - Erosão\n')

            result = func.erosion(img,element)

            cv2.imwrite('./data/result/3-1_erosion_' + elementStr +'.jpg',result)
            print('Salvando resultado em ~/data/result/3-1_erosion_' + elementStr +'.jpg')

            cv2.imshow('3-1 - Erosion (original image)',img)
            cv2.imshow('3-1 Erosion (result)',result)

        elif op3 == '2':
            print('3.2 - Dilatação')
            operation = '2_dilation_'

            result = func.dilation(img,element)

            cv2.imwrite('./data/result/3-2_dilation_' + elementStr +'.jpg',result)
            print('Salvando resultado em ~/data/result/3-2_dilation_' + elementStr +'.jpg')

            cv2.imshow('3-1 - Dilation (original image)',img)
            cv2.imshow('3-1 - Dilation (result)',result)

        else:
            print("Opção inválida.\n")
        
        cv2.waitKey()
        cv2.destroyAllWindows()
        
    elif op == '4':
        print("04 - GRADIENTE MORFOLÓGICO EM TONS DE CINZA")

        img = cv2.imread('./data/grayscale/house.tif',0)
        #img = cv2.imread('./data/base/coin.jpg',0)

        element = input("Escolha um elemento estruturante.\n1 - Quadrado 3x3\n2 - Quadrado 5x5\n3 - Cruz\n>>> ")

        if element == '1':
            elementStr = 'square3'
        elif element == '2':
            elementStr = 'square5'
        elif element == '3':
            elementStr = 'cross'

        result = func.morphGrad(img,element)

        plt.imsave('./data/result/4_morphGrad_'+elementStr+'.gif',result)
        print('Salvando resultado em ~/data/result/4_morphGrad_'+elementStr+'.gif')

        cv2.imshow('4_morphGrad (original image)',img)
        cv2.imshow('4_morphGrad (result)',result)

        cv2.waitKey()
        cv2.destroyAllWindows()


    elif op == '5':
        print("05 - CRESCIMENTO DE REGIÃO - IMAGEM BINÁRIA")

        clicks = []
        #img = cv2.imread('./data/base/holcocephala.jpg',0)
        img = plt.imread('./data/binary/apple-16.gif',0)
        img = cv2.resize(img,(256,256))
        cv2.namedWindow('Entrada')
        cv2.setMouseCallback('Entrada', on_mouse, 0, )
        cv2.imshow('Entrada', img)
        cv2.waitKey()
        print("Iniciando crescimento de regiao")
        
        seed = clicks[-1]        
        result = func.region_growing(img, seed)

        cv2.imshow('Resultado',result)
        print("Crescimento finalizado.")
        #result = region_growing(img, seed)
        #cv2.imshow('Region Growing', result)
        #cv2.waitKey()
        #cv2.destroyAllWindows()
        cv2.waitKey()
        cv2.destroyAllWindows()


    elif op == '6':
        print("06 - CRESCIMENTO DE REGIÃO - IMAGEM EM TONS DE CINZA")
    
    elif op == '7':
        print("07 - MÉTODO K-MEANS PARA SEGMENTAÇÃO")
    elif op == '8':
        print("08 - TRANSFORMADA HOUGH")
    elif op == '9':
        print("09 - TRANSFORMADA DE WATERSHED")

        img  = cv2.imread("./data/base/coin.jpg",0)
        result = func.watershed(img)
        cv2.imshow('Resultado',result)
        
        cv2.waitKey()
        cv2.destroyAllWindows()

    elif op == '10':
        print("10 - WAVELET E FOURIER")

    else:
        print("Invalido")
    a=1
    #sleep(2)

