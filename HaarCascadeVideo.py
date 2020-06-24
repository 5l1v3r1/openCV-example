
import cv2
import numpy as np


camera = cv2.VideoCapture(0)

fourcc = cv2.VideoWriter_fourcc(*'XVID')

kayit = cv2.VideoWriter('kayit.avi',fourcc,20,(640,480))

while True:
    ret,kare = camera.read()

    yuz_casc = cv2.CascadeClassifier("haarcascade_frontalcatface.xml")
    eye_casc = cv2.CascadeClassifier("haarcascade_eye.xml")


    gray_image = cv2.cvtColor(kare,cv2.COLOR_BGR2GRAY)

    #Yüzleri tespit etmemiziçin gereken işlem
    faces = yuz_casc.detectMultiScale(gray_image,1.5,5)
    #1.1 = Resmi ne kadar büyüteceğimiz,daha fazla piksel aralığı alıyor
    #4 = Kontrol aşaması , resmimizi kaç defa tarayacak

    for(x,y,w,h) in faces :
        cv2.rectangle(kare,(x,y),(x+w,y+h),(255,0,0),2)
        yuz_bolgesi = kare[y:y+h,x:x+w]
        gray_yuz_bolgesi = cv2.cvtColor(yuz_bolgesi,cv2.COLOR_BGR2GRAY)
        gozler = eye_casc.detectMultiScale(gray_yuz_bolgesi,1.1,4)

        for(a,b,c,d) in gozler:
            cv2.rectangle(yuz_bolgesi,(a,b),(a+c),(c+d),(0,255,0),2)

    kayit.write(kare)

    cv2.imshow("Video",kare)

    if cv2.waitKey(25) & 0xFF == ord('q'):
        break

camera.release()
cv2.destroyAllWindows()
