import cv2
import pytesseract
import numpy as np 

# Carrega a imagem
img = cv2.imread('imagem_com_ruido.jpg')

# Converte a imagem para escala de cinza
escala_cinza = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow("escala_cinza", escala_cinza)


# Aplica um filtro para reduzir o ruído
filtro_ruido = cv2.medianBlur(escala_cinza, 3)
cv2.imshow("filtro_ruido", filtro_ruido)

#normalização da imagem
imagem_normalizada = cv2.normalize(filtro_ruido, None, alpha=0, beta=255, norm_type=cv2.NORM_MINMAX)
cv2.imshow("imagem normalizada", imagem_normalizada)


#Limiarização da imagem
thresh = cv2.threshold(imagem_normalizada, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]
cv2.imshow("Limiarização", thresh)


cv2.waitKey(0)
cv2.destroyAllWindows()


# Configurações do Pytesseract
config = r'--oem 3 --psm 6 -l por'

# Extrai o texto da imagem com Pytesseract
text = pytesseract.image_to_string(thresh, config=config)

# Salva o texto em um arquivo .txt
with open('imagem_com_ruido.txt', mode='w') as file:
    file.write(text)
