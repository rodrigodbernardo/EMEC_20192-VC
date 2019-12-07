import cv2
import numpy as np
import process2

img1_path = "C:\\PDI\\imagens\\lnn.jpeg"
img = cv2.imread(img1_path,cv2.IMREAD_GRAYSCALE)
print("Escolha qual operação deseja aplicar sobre a imagem:")
print("1-Filtro da média")
print("2-Filtro da mediana")
print("3-Filtro Gaussiano")
print("4-Filtro Laplaciano")
print("5-Prewitt")
print("6-Sobel")
print("7-Mostrar histograma")
print("8-Limiarização")
print("9-Equalizar histograma")
print("10-Multilimiarização")
op = input("")


if op == '1':
    img_result = process2.aplicarMedia(img,9)
elif op == '2':
    img_result = process2.aplicarMediana(img, 9)
elif op == '3':
    img_result = process2.aplicarGaussiano(img,3,5)
elif op == '4':
    img_result = process2.aplicarLaplaciano(img)#opção de aplicar negativo
elif op == '5':
    print("Deseja aplicar:")
    print("1-Filtro para as verticais:")
    print("2-Filtro para as Horizontais")
    print("3-Soma das duas")
    escolha = input("")
    if escolha=='2':
        img_result = process2.aplicarPrewitt(img, 0)  # aplicar soma
    elif escolha=='1':
        img_result = process2.aplicarPrewitt(img, 1)  # aplicar soma
    else:
        img_result = process2.aplicarPrewitt(img, 0) +process2.aplicarPrewitt(img, 1)  # aplicar soma

elif op == '6':
    print("Deseja aplicar:")
    print("1-Filtro para as verticais:")
    print("2-Filtro para as Horizontais")
    print("3-Soma das duas")
    escolha = input("")

    if escolha=='2':
        img_result = process2.aplicarSobel(img, 0)  # aplicar soma
    elif escolha=='1':
        img_result = process2.aplicarSobel(img, 1)  # aplicar soma
    else:
        img_result = process2.aplicarSobel(img, 0) +process2.aplicarPrewitt(img, 1)  # aplicar soma
elif op == '7':
    img_result = process2.mostrarHistograma(img)
elif op == '8':
    limiar = int(input("Escolha um limiar"))
    img_result = process2.aplicarLimiarizacao(img, limiar)
elif op == '9':
    img_result = process2.equalizarHistograma(img)
elif op == '10':
    limiar =[]
    LimiarNumnumero = int(input("deseja definir quantos limiares?"))
    for i in range(0,LimiarNumnumero):
        limiar.append(int(input("Digite um limiar")))
    img_result = process2.aplicarMultLimiar(img,limiar)

else:
    print("Opção invalida")

cv2.imshow("Teste",img_result)
cv2.waitKey()