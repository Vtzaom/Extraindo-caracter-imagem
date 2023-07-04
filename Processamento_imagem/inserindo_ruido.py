import cv2
import numpy as np

# Carrega a imagem
img = cv2.imread('livroS.jpg')

# Converte a imagem para um array NumPy
img_array = np.array(img)

# Define o desvio padrão do ruído
std_dev = 100

# Adiciona ruído ao array usando a distribuição normal
noise = np.random.normal(0, std_dev, img_array.shape)

# Adiciona o ruído ao array da imagem
noisy_img_array = img_array + noise

# Normaliza os valores do array para o intervalo de 0 a 255
noisy_img_array = np.clip(noisy_img_array, 0, 255)

# Converte o array de volta para uma imagem
noisy_img = cv2.convertScaleAbs(noisy_img_array)

# Exibe a imagem com ruído na tela
cv2.imshow('Imagem com Ruído', noisy_img)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Salva a imagem com ruído em um arquivo
cv2.imwrite('imagem_com_ruido.jpg', noisy_img)
