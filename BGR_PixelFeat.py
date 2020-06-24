import cv2
import numpy as np

image = cv2.imread("samurayJack.jpg")

print("Resmin boyuyu=",str(image.size)) #Bu resmin kaç tane pikselden oluştuğunu öğrenmek istiyorum
#Resmin boyuyu 257712

print("Resmin yükseklik,genişlik,Kanal s.=",str(image.shape))
print("Resmin değişken tipi=",str(image.dtype))
print("image[50,50]=",image[50,50])
#Resimin 50 uzunluk , 50 genişliğindeki piselin değerileri

#image[50,50] = [255,255,255] #(50,50) konumundaki pikselin rengini değiştirdik
"""
for i in range(200):
    image[52,i]=[255,255,255]
"""

"""
Bolge = image[100:300,100:150] #y kordinatında 100'den 300' e kadar, x'de 200->400 e kadar
image[0:200,0:50]=Bolge # y(0,200) , x(0,50) bölgesini 'Bolge' ile değiştirdeik
"""

blueİmage,greenImage,redImage=cv2.split(image)
"""
cv2.split(image) , resmi kanallarına ayırdık , Blue,Green,Red kanallarını ayırıp
blueİmage,greenImage,redImage değişkenleerine sırası ile atadık
"""

pasteImage=cv2.merge((blueİmage,greenImage,redImage)) #3 kanalıda birleştiriyoruz
"""
image[100:150,100,170,2] = 255 , belirtilen bölge kırmızı olur
"""


cv2.imshow("samurayJack",image)
cv2.imshow("samurayJackBue",blueİmage)
cv2.imshow("samurayJackGreen",greenImage)
cv2.imshow("samurayJackRed",redImage)





cv2.waitKey(0)
cv2.destroyAllWindows()