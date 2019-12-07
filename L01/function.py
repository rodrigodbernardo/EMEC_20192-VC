import cv2
import numpy as np
from matplotlib import pyplot as plt

def meanFilter(img_in):

    kernel = 5

    lin, col = img_in.shape

    mask = np.zeros((kernel,kernel), np.uint8)
    mask[:,:] = 1
    mLin, mCol = mask.shape
    mCorner = int((mLin - 1) / 2)

    img_out = np.zeros(((lin + mLin - 1), (col + mCol - 1)), np.uint8)
    img_out[mCorner:(lin + mCorner), mCorner:(col + mCorner)] = img_in

    for i in range (mCorner, lin + 1):
        for j in range (mCorner, col + 1):
            mSample = img_out[(i-mCorner):(i+mCorner +1),(j - mCorner): (j+mCorner+1)]
            img_out[i,j] = mSample.mean()

    return img_out[mCorner:(lin+mCorner),mCorner:(col+mCorner)]

def medianFilter(img_in):

    kernel = 5
    lin,col = img_in.shape

    
    mask = np.zeros((kernel,kernel), np.uint8)
    mask[:,:] = 1
    mLin, mCol = mask.shape
    mCorner = int((mLin - 1) / 2)

    img_out = np.zeros(((lin + mLin - 1), (col + mCol - 1)), np.uint8)
    img_out[mCorner:(lin + mCorner), mCorner:(col + mCorner)] = img_in

    for i in range (mCorner, lin + 1):
        for j in range (mCorner, col + 1):
            mSample = img_out[(i-mCorner):(i+mCorner +1),(j - mCorner): (j+mCorner+1)]
            num = []

            for m in mSample:
                for n in m:
                    num.append(n)
            num.sort()
            medianI = int((len(num)-1)/2)

            img_out[i,j] = num[medianI]

    return img_out[mCorner:(lin+mCorner),mCorner:(col+mCorner)]

def gaussianFilter(img_in):

    lin,col = img_in.shape

    mSize = 5
    std_dev = 10

#getmask
    x = np.zeros((mSize,mSize),np.int16)
    y = np.zeros((mSize,mSize),np.int16)

    border = int((mSize-1)/2)

    for i in range(mSize):
        for j in range(mSize):
            x[i,j] = i - border
            y[i,j] = j - border

    mask = (1/(2 * np.pi * std_dev**2)) * np.exp(-((x**2 + y**2) / (2 * std_dev**2)))
    
    '''
                        1                          -(x^2 + y^2)
gaussMask =  ---------------------------- x exp[ --------------------- ]
              2 x pi x (std_deviation^2)          2 x std_deviation^2

    '''

    max = mask.max()
    min = mask.min()
    for m in range(mSize):
        for n in range(mSize):
            mask[m,n] = int(100*(mask[m,n]-min)/(max-min))
#gotmask

    mLin, mCol = mask.shape
    mCorner = int((mLin - 1)/2)
    
    img_out = np.zeros(((lin + mLin - 1),(col + mCol - 1)),np.uint8)
    img_out[mCorner:(lin+mCorner),mCorner:(col+mCorner)] = img_in
    
    mSum = mask.sum()
    #copy = img_out.copy()

    for layer in range(0,1):
        for i in range(mCorner, lin + 1):
            for j in range(mCorner, col + 1):
                mSample = img_out[(i - mCorner):(i + mCorner + 1), (j - mCorner):(j + mCorner + 1)]

                img_out[i, j] = (mSample*mask).sum()/mSum

    return img_out[mCorner:(lin + mCorner), mCorner:(col + mCorner)]

def laplacianFilter(img_in):
    
    #verify
    mask = np.array([[0,1,0],[1,-10,1],[0,1,0]])
    lin, col = img_in.shape
    mLin, mCol = (3,3)
    mCorner = int((mLin - 1) / 2)

    img_out = np.zeros(((lin+mLin - 1),(col+mCol - 1)),np.uint8)
    img_out[mCorner:(lin+mCorner),mCorner:(col+mCorner)] = img_in

    # for x1 in range (int(mLin/2),lin - int(mLin/2)):
    #     for y1 in range (int(mCol/2), col - int(mCol/2)):
    #         m = 0

    #         for x2 in range (int(-mLin/2),int(mLin/2) +1):
    #             for y2 in range(int(-mCol/2),int(mCol/2) +1):
    #                 if x2 == 0 and y2 == 0:
    #                     m += (img_in[y2+y1,x2+x1]*(-8))
    #                 else:
    #                     m += img_in[y2+y1,x2+x1]

    #         m = abs(m)
    #         img_out[x1,y1] = m
    for layer in range(0,1):
        for i in range(mCorner, mLin + 1):
            for j in range(mCorner, col + 1):
                mSample = img_out[(i - mCorner):(i+1 + mCorner),(j - mCorner):(j+1 + mCorner)]
                mSample = mSample*mask
                if mSample.sum()<0:
                    img_out[i,j] = 0
    return img_out

def prewitt(img,sentido):
    img_out = img.copy()
    if(sentido==0):
        mask = np.array([[-1, -1, -1], [0, 0, 0], [1, 1, 1]])
    else:
        mask = np.array([[-1, 0, 1], [-1, 0, 1], [-1, 0, 1]])

    lin, col = img_out.shape
    
    mLin, maskcol = (3, 3)
    mCorner = int((mLin - 1) / 2)

    img_out = np.zeros(((lin + mLin - 1), (col + maskcol - 1)), np.uint8)
    img_out[mCorner:(lin + mCorner), mCorner:(col + mCorner)] = img
    
    imgCopy = img_out.copy()
    
    for camada in range(0, 1):
        for i in range(mCorner, lin + 1):
            for j in range(mCorner, col + 1):
                mSample = imgCopy[(i - mCorner):(i + mCorner + 1), (j - mCorner):(j + mCorner + 1)]
                mSample = mSample * mask
                # 0 0 0 182 117 135 95 88 96
                img_out[i, j] = 0 if mSample.sum() < 0 else mSample.sum()

    return img_out

def sobel(img,sentido):
    img_out = img.copy()
    if(sentido==0):
        mask = np.array([[1, 2, 1], [0, 0, 0], [-1, -2, -1]])
    else:
        mask = np.array([[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]])

    lin, col = img_out.shape
    mLin, maskcol = (3, 3)
    mCorner = int((mLin - 1) / 2)
    img_out = np.zeros(((lin + mLin - 1), (col + maskcol - 1)), np.uint8)
    img_out[mCorner:(lin + mCorner), mCorner:(col + mCorner)] = img
    imgCopy = img_out.copy()
    for camada in range(0, 1):
        for i in range(mCorner, lin + 1):
            for y in range(mCorner, col + 1):
                mSample = imgCopy[(i - mCorner):(i + mCorner + 1), (y - mCorner):(y + mCorner + 1)]
                mSample = mSample * mask
                img_out[i, y] = 0 if mSample.sum() < 0 else mSample.sum()

    return img_out

def histogram(img):

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

def thresholding(img):
    lin,col = img.shape
    img_out = np.zeros(((lin),(col)),np.uint8)

    for i in range (lin):
        for j in range (col):
            if (img[i,j] >= 100):
                img_out[i,j] = 250
            else:
                img_out[i,j] = 0 
    return img_out

def equalization(img):
    rows, columns = img.shape

    img_out = img.copy()
    max = img.max()
    min = img.min()
    for i in range((0), rows):
        for j in range((0), columns):
            img_out[i, j] = int(255 * ((img[i, j] - min) /(max - min)))
    histo = np.zeros(256)

    for i in img_out:
        for y in i:
            histo[y] += 1

    fig, axs = plt.subplots(2)
    fig.suptitle('Histograma')
    axs[0].plot(histo)
    axs[1] = plt.imshow(img, cmap='gray')
    plt.show()
    return img_out

