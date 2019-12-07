import cv2
import numpy as np
from PIL import Image
import sys

def translation(img):
    lin, col = img.shape[:2]

    tMatrix = np.float32([[1,0,70],[0,1,110]])

    return cv2.warpAffine(img,tMatrix,(col,lin))

def rotation(img, angle):
  
    (h, w) = img.shape[:2]
    (cX, cY) = (w // 2, h // 2)
 

    M = cv2.getRotationMatrix2D((cX, cY), angle, 1.0)
    cos = np.abs(M[0, 0])
    sin = np.abs(M[0, 1])
 
    nW = int((h * sin) + (w * cos))
    nH = int((h * cos) + (w * sin))
 
    M[0, 2] += (nW / 2) - cX
    M[1, 2] += (nH / 2) - cY
 
    return cv2.warpAffine(img, M, (nW, nH))

def scale(img,scale):

    width = int(img.shape[1] * scale / 100)
    height = int(img.shape[0] * scale / 100)
    dim = (width, height)
        
    return cv2.resize(img, dim, interpolation = cv2.INTER_AREA)

def erosion(img,kType):
    if kType == '1':
        kernel = np.ones((3,3),np.uint8)
    elif kType == '2':
        kernel = np.ones((5,5),np.uint8)
    elif kType == '3':
        kernel = np.array([[0, 1, 0],[1, 1, 1],[0, 1, 0]], dtype = np.uint8)
    return cv2.erode(img,kernel,iterations = 5)

def dilation(img,kType):
    if kType == '1':
        kernel = np.ones((3,3),np.uint8)
    elif kType == '2':
        kernel = np.ones((5,5),np.uint8)
    elif kType == '3':
        kernel = np.array([[0, 1, 0],[1, 1, 1],[0, 1, 0]], dtype = np.uint8)
    return cv2.dilate(img,kernel,iterations = 5)

def morphGrad(img,kType):
    if kType == '1':
        kernel = np.ones((3,3),np.uint8)
    elif kType == '2':
        kernel = np.ones((5,5),np.uint8)
    elif kType == '3':
        kernel = np.array([[0, 1, 0],[1, 1, 1],[0, 1, 0]], dtype = np.uint8)
    return cv2.morphologyEx(img, cv2.MORPH_GRADIENT, kernel)



def get8n(x, y, shape):
    out = []
    maxx = shape[1]-1
    maxy = shape[0]-1

    #top left
    outx = min(max(x-1,0),maxx)
    outy = min(max(y-1,0),maxy)
    out.append((outx,outy))

    #top center
    outx = x
    outy = min(max(y-1,0),maxy)
    out.append((outx,outy))

    #top right
    outx = min(max(x+1,0),maxx)
    outy = min(max(y-1,0),maxy)
    out.append((outx,outy))

    #left
    outx = min(max(x-1,0),maxx)
    outy = y
    out.append((outx,outy))

    #right
    outx = min(max(x+1,0),maxx)
    outy = y
    out.append((outx,outy))

    #bottom left
    outx = min(max(x-1,0),maxx)
    outy = min(max(y+1,0),maxy)
    out.append((outx,outy))

    #bottom center
    outx = x
    outy = min(max(y+1,0),maxy)
    out.append((outx,outy))

    #bottom right
    outx = min(max(x+1,0),maxx)
    outy = min(max(y+1,0),maxy)
    out.append((outx,outy))

    return out

def region_growing(img, seed):
    list = []
    outimg = np.zeros_like(img)
    list.append((seed[0], seed[1]))
    processed = []
    print (len(list))
    while(len(list) > 0):
        pix = list[0]
        outimg[pix[0], pix[1]] = 255
        for coord in get8n(pix[0], pix[1], img.shape):
            if img[coord[0], coord[1]] != 0:
                outimg[coord[0], coord[1]] = 255
                if not coord in processed:
                    list.append(coord)
                processed.append(coord)
        list.pop(0)
        cv2.imshow("progress",outimg)
        cv2.waitKey(1)
    return outimg

def watershed(img):
    ret, thresh = cv2.threshold(img,0,255,cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)

    kernel = np.ones((3,3),np.uint8)

    opening = cv2.morphologyEx(thresh,cv2.MORPH_OPEN,kernel,2)

    sure_bg = cv2.dilate(opening,kernel,3)
     
    dist_transform = cv2.distanceTransform(opening,cv2.DIST_L2,5)

    ret, sure_fg = cv2.threshold(dist_transform,0.7*dist_transform.max(),255,0)

    sure_fg = np.uint8(sure_fg)

    unknown = cv2.subtract(sure_bg,sure_fg)

    ret, markers = cv2.connectedComponents(sure_fg)

    markers = markers+1

    markers[unknown==255] = 0

    markers = cv2.watershed(img,markers)
    img[markers == -1] = [255,0,0]

    return img