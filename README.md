# Trabalho de Processamento de Imagens

  Este trabalho consistia em processar a imagem de um texto e extrair o texto dela , para isso foi necessário acrescentar ruídos a imagem .
  O reconhecimento de caracteres foi realizado utilizando  utilizando **Python** , **OpenCV** e **Tesseract**.


## Executando em sua máquina local
1. Tenha o **Python** instalado em sua computador , se não tiver leia o tutorial de como instalar: https://www.python.org/downloads/ 
2. Instale o **Tesseract** , para tal acesse esse tutorial https://nanonets.com/blog/ocr-with-tesseract/ .
3. Instale o **OpenCV** , para sistema windowns cliclando [aqui](https://docs.opencv.org/4.x/d5/de5/tutorial_py_setup_in_windows.html) e para sistema linux clicando [aqui](https://docs.opencv.org/3.4/d2/de6/tutorial_py_setup_in_ubuntu.html)
4. Após as etapas anteriores , clone este repositório e execute o arquivo **processamento.py** .

## Testando outra imagem 
1. Adicione a imagem a pasta .
2. Carregue o nome da imagem no arquivo **inserindo_ruido.py** , como o exemplo : `img = cv2.imread('livroS.jpg')` .
3. Execute em seu terminal **python3 inserindo_ruido.py** e veja a imagem com ruido .
4. Execute em seu terminal **python3 processamento.py** e veja o texto extraído da imagem.