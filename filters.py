import cv2
import pytesseract
import numpy as np

from PIL import Image
from pytesseract import Output

# tesseract
path = "E:\Tesseract\Tesseract.exe"
pytesseract.pytesseract.tesseract_cmd = path

# pre-processing

# gray scaliing filter
def getGray(image):
    return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

#def bugFix(image):
#    return cv2.medianBlur(image,0)

# thresholding
def getThresholding(image):
    return cv2.threshold(image, 75, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]

# remove noise
def removeNoise(image):
    return cv2.medianBlur(image,5)

# dilatation
def getDilate(image):
    kernel = np.ones((1,1),np.uint8)
    return cv2.dilate(image, kernel, iterations = 1)

# gaussian
def getGaussian(image, varGa1, varGa2):
    return cv2.GaussianBlur(image, (varGa1, varGa2), 0)

# erosion
def getErosion(image):
    kernel = np.ones((1,1),np.uint8)
    return cv2.erode(image, kernel, iterations = 1)

# canny
def getCanny(image):
    return cv2.Canny(image, 200, 125)

# normalization
def getNormalization(image):
    norm_img = np.zeros((image.shape[0],image.shape[1]))
    return cv2.normalize(image, norm_img, 15, 255, cv2.NORM_MINMAX)

# opening
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