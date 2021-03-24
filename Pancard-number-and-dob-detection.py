import pytesseract as tess
import numpy as np
import re
from pytesseract import Output
tess.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
from PIL import Image


import cv2

import imutils


img = cv2.imread('3657993.jpg')

a=int(input("Enter the angle to be rotated"))  


  
Rotated_image = imutils.rotate(img, a)


d = tess.image_to_data(Rotated_image, output_type=Output.DICT)
keys = list(d.keys())

date_pattern = '^(0?[1-9]|[12][0-9]|3[01])[\/\-](0?[1-9]|1[012])[\/\-]\d{4}$'
card_number = "[A-Z]{5}[0-9]{4}[A-Z]{1}"
n_boxes = len(d['text'])
for i in range(n_boxes):
    if int(d['conf'][i]) > 50:
    	if re.match(date_pattern, d['text'][i]):
	        (x, y, w, h) = (d['left'][i], d['top'][i], d['width'][i], d['height'][i])
	        img = cv2.rectangle(Rotated_image, (x, y), (x + w, y + h), (0, 255, 0), 2)

	        
n_boxes = len(d['text'])
for i in range(n_boxes):
    if int(d['conf'][i]) > 50:
    	if re.match(card_number, d['text'][i]):
	        (x, y, w, h) = (d['left'][i], d['top'][i], d['width'][i], d['height'][i])
	        img = cv2.rectangle(Rotated_image, (x, y), (x + w, y + h), (0, 255, 0), 2)



cv2.imshow('PANCARD NUMBER AND DATE OF BIRTH DETECTION', img)





cv2.waitKey(0)
