import cv2
import numpy as np
from matplotlib import pyplot as plt

def aplicarMedia(img,matriz):
    img_return = img.copy()
    mask = np.zeros((matriz,matriz), np.uint8)
    mask[:, :] = 1

    height, width = img_return.shape
    maskHeight, maskWidth = mask.shape
    maskCorner = int((maskHeight-1)/2)
    img_return = np.zeros(((height + maskHeight-1), (width + maskWidth-1)), np.uint8)
    img_return[maskCorner:(height + maskCorner), maskCorner:(width + maskCorner)] = img

    for i in range(maskCorner, height+1):
        for y in range(maskCorner, width+1):
            maskAmostra = img_return[(i-maskCorner):(i+maskCorner+1), (y-maskCorner):(y+maskCorner+1)]
            img_return[i,y] = maskAmostra.mean()

    img_return = img_return[maskCorner:(height + maskCorner), maskCorner:(width + maskCorner)]
    return img_return

def aplicarMediana(img,matriz):
    img_return = img.copy()
    mask = np.zeros((matriz,matriz), np.uint8)
    mask[:, :] = 1

    height, width = img_return.shape
    maskHeight, maskWidth = mask.shape
    maskCorner = int((maskHeight - 1) / 2)
    img_return = np.zeros(((height + maskHeight - 1), (width + maskWidth - 1)), np.uint8)
    img_return[maskCorner:(height + maskCorner), maskCorner:(width + maskCorner)] = img

    for i in range(maskCorner, height + 1):
        for y in range(maskCorner, width + 1):
            maskAmostra = img_return[(i - maskCorner):(i + maskCorner + 1), (y - maskCorner):(y + maskCorner + 1)]
            img_return[i,y] = getMediana(maskAmostra)


    return img_return

def getMediana(matriz):
    nuns = []

    for i in matriz:
        for y in i:
            nuns.append(y)
    nuns.sort()
    medianaIndex = int(((len(nuns)-1)/2))
    return nuns[medianaIndex]

def aplicarGaussiano(img, matriz, desv):
    img_return = img.copy()
    mask = gerarGaussianMask(matriz, desv)

    height, width = img_return.shape
    maskHeight, maskWidth = mask.shape
    maskCorner = int((maskHeight - 1) / 2)
    img_return = np.zeros(((height + maskHeight - 1), (width + maskWidth - 1)), np.uint8)
    img_return[maskCorner:(height + maskCorner), maskCorner:(width + maskCorner)] = img
    maskSum = mask.sum()
    img_copy = img_return.copy()
    for camada in range(0,1):
        for i in range(maskCorner, height + 1):
            for y in range(maskCorner, width + 1):
                maskAmostra = img_copy[(i - maskCorner):(i + maskCorner + 1), (y - maskCorner):(y + maskCorner + 1)]

                img_return[i, y] = (maskAmostra*mask).sum()/maskSum
    img_return = img_return[maskCorner:(height + maskCorner), maskCorner:(width + maskCorner)]
    return img_return

def gerarGaussianMask(formato, desv):
    x = np.zeros((formato, formato), np.int16)
    y = np.zeros((formato, formato), np.int16)
    borda = int((formato-1)/2)
    for m in range(formato):
        for n in range(formato):
            x[m, n] = n - borda
            y[m, n] = m - borda
    num = (1 / (2 * np.pi * desv**2)) * np.exp(-((x ** 2 + y ** 2) / (2*desv**2)))
    #num = num/num[0,0]
    #num = np.round(num,decimals=0)
    max = num.max()
    min = num.min()
    for m in range(formato):
        for n in range(formato):
            num[m,n] = int(100*(num[m,n]-min)/(max-min))
    return num

def aplicarLaplaciano(img):
    img_return = img.copy()

    mask = np.array([[0,1,0],[1,-4,1],[0,1,0]])
    height, width = img_return.shape
    maskHeight, maskWidth = (3,3)
    maskCorner = int((maskHeight - 1) / 2)
    img_return = np.zeros(((height + maskHeight - 1), (width + maskWidth - 1)), np.uint8)
    img_return[maskCorner:(height + maskCorner), maskCorner:(width + maskCorner)] = img
    imgCopy = img_return.copy()
    for camada in range(0,1):
        for i in range(maskCorner, height + 1):
            for y in range(maskCorner, width + 1):
                maskAmostra = imgCopy[(i - maskCorner):(i + maskCorner + 1), (y - maskCorner):(y + maskCorner + 1)]
                maskAmostra = maskAmostra*mask
                img_return[i, y] = 0 if maskAmostra.sum()<0 else maskAmostra.sum()

    return img_return

def aplicarPrewitt(img,sentido):
    img_return = img.copy()
    if(sentido==0):
        mask = np.array([[-1, -1, -1], [0, 0, 0], [1, 1, 1]])
    else:
        mask = np.array([[-1, 0, 1], [-1, 0, 1], [-1, 0, 1]])

    height, width = img_return.shape
    maskHeight, maskWidth = (3, 3)
    maskCorner = int((maskHeight - 1) / 2)
    img_return = np.zeros(((height + maskHeight - 1), (width + maskWidth - 1)), np.uint8)
    img_return[maskCorner:(height + maskCorner), maskCorner:(width + maskCorner)] = img
    imgCopy = img_return.copy()
    for camada in range(0, 1):
        for i in range(maskCorner, height + 1):
            for y in range(maskCorner, width + 1):
                maskAmostra = imgCopy[(i - maskCorner):(i + maskCorner + 1), (y - maskCorner):(y + maskCorner + 1)]
                maskAmostra = maskAmostra * mask
                # 0 0 0 182 117 135 95 88 96
                img_return[i, y] = 0 if maskAmostra.sum() < 0 else maskAmostra.sum()

    return img_return

def aplicarSobel(img,sentido):
    img_return = img.copy()
    if(sentido==0):
        mask = np.array([[1, 2, 1], [0, 0, 0], [-1, -2, -1]])
    else:
        mask = np.array([[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]])

    height, width = img_return.shape
    maskHeight, maskWidth = (3, 3)
    maskCorner = int((maskHeight - 1) / 2)
    img_return = np.zeros(((height + maskHeight - 1), (width + maskWidth - 1)), np.uint8)
    img_return[maskCorner:(height + maskCorner), maskCorner:(width + maskCorner)] = img
    imgCopy = img_return.copy()
    for camada in range(0, 1):
        for i in range(maskCorner, height + 1):
            for y in range(maskCorner, width + 1):
                maskAmostra = imgCopy[(i - maskCorner):(i + maskCorner + 1), (y - maskCorner):(y + maskCorner + 1)]
                maskAmostra = maskAmostra * mask
                img_return[i, y] = 0 if maskAmostra.sum() < 0 else maskAmostra.sum()

    return img_return

def mostrarHistograma(img):

    histo = np.zeros(256)

    for i in img:
        for y in i:
            histo[y] += 1

    fig, axs = plt.subplots(2)
    fig.suptitle('Histograma')
    axs[0].plot(histo)
    axs[1] = plt.imshow(img, cmap='gray')
    plt.show()
    return img

def aplicarLimiarizacao(img, limiar):
    img_return = img.copy()
    img_return[img_return > limiar] = 255
    img_return[img_return <= limiar] = 0
    return img_return

def equalizarHistograma(img):
    rows, columns = img.shape

    img_return = img.copy()
    max = img.max()
    min = img.min()
    for i in range((0), rows):
        for j in range((0), columns):
            img_return[i, j] = int(255 * ((img[i, j] - min) /(max - min)))
    histo = np.zeros(256)

    for i in img_return:
        for y in i:
            histo[y] += 1

    fig, axs = plt.subplots(2)
    fig.suptitle('Histograma')
    axs[0].plot(histo)
    axs[1] = plt.imshow(img, cmap='gray')
    plt.show()
    return img_return

def aplicarMultLimiar(img, limiar):
    img_return = img.copy()
    nLimiar = len(limiar)
    passo = int(255/(len(limiar)))
    limiar.append(0)
    limiar.append(255)
    limiar.sort()
    for i, value in enumerate(img_return):
        for y, valuey in enumerate(value):
            for m, valueLim in enumerate(limiar):
                if(valuey>=valueLim and valuey<limiar[m+1]):
                    img_return[i,y] = passo * m


    return img_return
