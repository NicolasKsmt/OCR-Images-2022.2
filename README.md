# Trabalho de Processamento de Imagens 2022.2 - UFRRJ

Reconhecimento de caracteres em imagens (OCR) utilizando Python + OpenCV e Tesseract 




## Grupo
Integrantes:    
Nicolas Machado Pereira     
Vitor Moreira de Brito  
Lediane Oliveira da Silva     
Matheus Montenegro Soares 
## Como rodar o projeto:

Instaleas bibliotecas necessárias:  **pip install opencv-python** e **pip install pytesseract**

No linux, instale o tesseract-ocr: **sudo apt-get install tesseract-ocr**

No Windows, instale o tesseract-ocr: https://github.com/UB-Mannheim/tesseract/wiki

Leia os comentários no código (principalmente no **main.py**) para entender melhor o que está acontecendo.

Para rodar use: **python3 main.py**


    
## Filtros Utilizados

Grayscale :
```
def getGray(image):     
    return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
```
Thresholding:
```
def getThresholding(image):
    return cv2.threshold(image, 75, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]
```
Noise removal:
```
def removeNoise(image):
    return cv2.medianBlur(image,5)
```
Dilation:
```
def getDilate(image):
    kernel = np.ones((1,1),np.uint8)
    return cv2.dilate(image, kernel, iterations = 1)
```
Gaussian Blur
```
def getGaussian(image, varGa1, varGa2):
    return cv2.GaussianBlur(image, (varGa1, varGa2), 0)
```
Erosion
```
def getErosion(image):
    kernel = np.ones((1,1),np.uint8)
    return cv2.erode(image, kernel, iterations = 1)
```
Canny:
```
def getCanny(image):
    return cv2.Canny(image, 200, 125)
```

Normalization
```
def getNormalization(image):
    norm_img = np.zeros((image.shape[0],image.shape[1]))
    return cv2.normalize(image, norm_img, 15, 255, cv2.NORM_MINMAX)
```
Opening:
```
def getOpening(image):
    kernel = np.ones((3,3),np.uint8)
    return cv2.morphologyEx(image, cv2.MORPH_OPEN, kernel)
```

