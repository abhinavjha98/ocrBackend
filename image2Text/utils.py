import matplotlib.pyplot as plt
import cv2
import easyocr
import re
import shutil, os
import time
img_names = []
import json


def image_convert(file_name):
    reader = easyocr.Reader(['en'])
    output = reader.readtext(file_name)
    count = 0
    for detection in output:
        text = detection[1]
        count += len(re.findall(r'\w+', text))
        if count > (100+10):
            break
        if count < 110:
            img = cv2.imread(file_name)
            for detection in output:
                top_left = tuple([int(val) for val in detection[0][0]])
                bottom_right = tuple([int(val) for val in detection[0][2]])
            
                img = cv2.rectangle(img,top_left,bottom_right,(255,255,255),-1)
            new_file = file_name
            file_names = file_name.split(".")
            new_file_name = "updated_"+file_names[0]+"."+file_names[1]
            try:
                cv2.imwrite("/home/abhinav/Projects/ocrBackend/ocrBackend/image2Text/images/"+new_file_name, img)
            except:
                pass
            try:
                shutil.move(file_name,'/home/abhinav/Projects/ocrBackend/ocrBackend/image2Text/images/')
                print("Successfully changed the image")
            except:
                pass
                
        else:
            try:
                shutil.move(file_name,'/home/abhinav/Projects/ocrBackend/ocrBackend/image2Text/documents/')
                print("Successfully changed the document")
            except:
                pass
                