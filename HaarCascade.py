
import cv2
import numpy as np

yuz_casc = cv2.CascadeClassifier("haarcascade_frontalcatface.xml")

image = cv2.imread("face.jpg")

gray_image = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

#Yüzleri tespit etmemiziçin gereken işlem
faces = yuz_casc.detectMultiScale(gray_image,1.1,4)
#1.1 = Resmi ne kadar büyüteceğimiz,daha fazla piksel aralığı alıyor
#4 = Kontrol aşaması , resmimizi kaç defa tarayacak

print(faces)
#[[257  79 410 410]]
#410=Genişlik
#410= yükseklik
#257  79 = Resimdeki yüzün sol üst köşesindeki x,y kordinatı


for(x,y,w,h) in faces :
    cv2.rectangle(image,(x,y),(x+w,y+h),(255,0,0),2)

cv2.imshow("imaage",image)

cv2.waitKey(0)
cv2.destroyAllWindows()
