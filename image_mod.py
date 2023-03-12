import cv2
import pytesseract
import language

def ocr(image):
    pytesseract.image_to_string(image, lang=language.LANG, config=language.CUSTOM_CONFIG)

def readImage(img):
    return cv2.imread(img)

def showImage(image):
    cv2.imshow('img', image)
    cv2.waitKey(0)