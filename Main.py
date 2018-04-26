from functions import *
from test import *


acerto = 50
res = geraResp(1)
tes = try_(res, acerto) 
por = '%'
print "Acertou em %d imagens, de um total de %d." % (tes, len(res))
print "Porcentagem de acerto: %.2f%c" % (tes*100/len(res), por)
print ""
## dimensoes = 1024 x 551  




























'''
for i in range(len(res)):
    print "----REs [%d]-----"% (i)
    print "    Path: ",res[i][0]
    print "    Faces: ", res[i][1]
    for vec in res[i][2]:
        print"\n      X = ", vec[0]
        print"      Y = ", vec[1]
'''

    


'''
#--------AINDA NAO OK--------
# Nao encontrou nenhum olho na imagem.
#acredito que seja o tamanho, talvez se utilizar o window sliding funcione :)
#
# Achar olhos na imagem
img = cv2.imread("test7.jpg")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

faces =  face_cascade.detectMultiScale(gray, 1.3, 5)
#Minimal neighbours    

plt.figure()
plt.imshow(gray, cmap='gray')
axis = plt.gca()
for (x,y,w,h) in faces:
    axis.add_patch(Rectangle((x,y), w, h, facecolor='none', edgecolor='red'))
    roi_gray = gray[y:y+h, x:x+w]
    
    olhos = eye_cascade.detectMultiScale(roi_gray, 1.3, 2)
    for (ex, ey, ew, eh) in olhos:
        axis.add_patch(Rectangle((x+ex,y+ey), ew, eh, facecolor='none', edgecolor='red'))
plt.show()
#https://docs.opencv.org/trunk/d7/d8b/tutorial_py_face_detection.html
'''




'''
IMAGENS PIRAMIDAIS
plt.figure()
# so consegui trabalhar dentro de um FOR, porque a funcao pyramid retorna um generator e nao um iterator, 
#entao nao sei o numero de objetos retornados por esse generator.
#https://www.pyimagesearch.com/2015/03/16/image-pyramids-with-python-and-opencv/
for resized in transform.pyramid_gaussian(img, downscale=2):
    #Condicao para parar, pois imagens muito pequenas nao valem a pena ser conferidas
    if resized.shape[0] <= 20 or resized.shape[1]<=20:
        break
    print "Shape : ", resized.shape
    plt.imshow(resized)
    plt.show()
'''



'''
SLIDDING WINDOW
result = slidingWindow(img)
plt.figure()
for i in range(0, 5):
    plt.subplot(1,6,i+1)
    plt.imshow(result[i][2])
plt.show()

print "X de %d ate %d" % (result[1][0], result[1][3])
print "Y de %d ate %d" % (result[1][1], result[1][4])
'''
