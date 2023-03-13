import cv2
import pytesseract
import config
import re
import image_mod

from pytesseract import Output
from image_mod import *
from filters import *
from config import *

# Configura o tesseract com o caminho do executável
path = "E:\Tesseract\Tesseract.exe"
pytesseract.pytesseract.tesseract_cmd = path

<<<<<<< Updated upstream
# dica : 'which tesseract' no terminal para descobrir o path do tesseract no linux e 'where tesseract' no windows.

# Path default do tesseract no Linux (Ubuntu): r'/usr/bin/tesseract'
# Path default do tesseract no Windows : r'C:\Users\Python\AppData\Local\Programs\Tesseract-OCR\tesseract.exe'

image = cv2.imread("disc.png")
#showImage(image)
#image_copy = bugFix(image)


gray_image = getGray(image) # Converte a imagem para escala de cinza
gauss_image = getGaussian(gray_image, 3, 3) # Aplica o desfoque Gaussiano na imagem
thresh_image = getThresholding(gauss_image) # Aplica um threshold para transformar a imagem em binária
norm_image = getNormalization(thresh_image) # Aplica a normalização na imagem
=======
image = cv2.imread("motiv.png")
#showImage(image)
#image_copy = bugFix(image)

gray_image = getGray(image)
gauss_image = getGaussian(gray_image, 3, 3)
thresh_image = getThresholding(gauss_image)
norm_image = getNormalization(thresh_image)
erode_image = getErosion(norm_image)
>>>>>>> Stashed changes

showImage(erode_image)

boxedImage = getBoxes(erode_image)
showImage(boxedImage)

<<<<<<< Updated upstream
# Transforma a imagem em texto

text = pytesseract.image_to_string(norm_image, lang=language.LANG)
=======
text = pytesseract.image_to_string(erode_image, lang=language.LANG)
>>>>>>> Stashed changes
with open("text.txt", "w") as folder:
    folder.write(text)

text_num = pytesseract.image_to_string(erode_image, config=custom_config_num)
with open("text_num.txt", "w") as folder:
    folder.write(text_num)

text_wl = pytesseract.image_to_string(erode_image, config=custom_config_wl)
with open("text_wl.txt", "w") as folder:
    folder.write(text_wl)