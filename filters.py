import cv2
import pytesseract
import numpy as np

from PIL import Image
from pytesseract import Output


#path = "E:\Tesseract\Tesseract.exe"
#pytesseract.pytesseract.tesseract_cmd = path


# pré-processamento

# Converte a imagem para escala de cinza 
def getGray(image):
    return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

#def bugFix(image):
#    return cv2.medianBlur(image,0)

# Aplica um threshold para transformar a imagem em binária
def getThresholding(image):
    return cv2.threshold(image, 75, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]

# Remove o ruído da imagem
def removeNoise(image):
    return cv2.medianBlur(image,5)

# Dilatação
def getDilate(image):
    kernel = np.ones((1,1),np.uint8)
    return cv2.dilate(image, kernel, iterations = 1)

# Gaussian Blur ou Desfoque Gaussiano
def getGaussian(image, varGa1, varGa2):
    return cv2.GaussianBlur(image, (varGa1, varGa2), 0)

# Remoção de erosão 
def getErosion(image):
    kernel = np.ones((1,1),np.uint8)
    return cv2.erode(image, kernel, iterations = 1)

# Canny
def getCanny(image):
    return cv2.Canny(image, 200, 125)

# Normalização
def getNormalization(image):
    norm_img = np.zeros((image.shape[0],image.shape[1]))
    return cv2.normalize(image, norm_img, 15, 255, cv2.NORM_MINMAX)

# Opening
def getOpening(image):
    kernel = np.ones((3,3),np.uint8)
    return cv2.morphologyEx(image, cv2.MORPH_OPEN, kernel)

    
# get image boxes
def getBoxes(image):
    d = pytesseract.image_to_data(image, output_type=Output.DICT)
    n_boxes = len(d['text'])
    for i in range(n_boxes):
        if int(d['conf'][i]) > 60:
            (x, y, w, h) = (d['left'][i], d['top'][i], d['width'][i], d['height'][i])
            image = cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)
    return image