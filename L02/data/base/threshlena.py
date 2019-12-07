import cv2

img = cv2.imread("lena.bmp",0)
ret,im = cv2.threshold(img, 128, 255, cv2.THRESH_BINARY)
cv2.imwrite('lena.jpg',im)