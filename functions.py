import matplotlib.pyplot as plt 
from scipy import misc
import cv2
from skimage.feature import blob_dog , hog # Blob para reconhecimento
from skimage import measure, morphology # Para Label
from skimage import color, filters, exposure, img_as_float # Also for blob
from scipy import ndimage
import numpy as np

from skimage import transform
from matplotlib.patches import Rectangle


'''
vai retornar um vetor de structs, onde cada elemento da matrix tem 3 variaveis: 
[0] - Y - INICIAL
[1] - X - INICIAL
[2] - imagem cortada
[3] - Y - FINAL
[4] - X - FINAL
'''
def slidingWindow(img):
    step = img.shape[1]/5
    yEnd=0
    xEnd = 0
    res =[]
    for y in range(0, img.shape[0], step):
        for x in range(0, img.shape[1], step):
            yEnd=y+step
            xEnd=x+step
            if yEnd > img.shape[0]:
                yEnd=img.shape[0]
            if xEnd > img.shape[1]:
                xEnd = img.shape[1]
                
            res.append((x, y, img[y:yEnd, x:xEnd,] , xEnd, yEnd))
    return res


def face_detect(img):
    face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    return faces
    
    
    
    
    
    
    
    
    
    