import cv2
import numpy as np

camera = cv2.VideoCapture(0)

while True:
    ret,view = camera.read()

    gray_view = cv2.cvtColor(view,cv2.COLOR_BGR2GRAY)

    object = cv2.imread("telefon.jpg",0)

    w,h = object.shape #weight,height

    res = cv2.matchTemplate(gray_view,object,cv2.TM_CCOEFF_NORMED)
    """
    res değerinde , belirlenen nesne ile resim arasındaki benzer pisksellirin 
    benzerik oranını dödürüyor
    """

    esik_degeri = 0.8

    loc = np.where(res>esik_degeri)
    #Bnezerlilik orano 0.8 den büyük olanların yerleri kaydediliyor
    for n in zip(*loc[::-1]):
        cv2.rectangle(view,n,(n[0]+h,n[1]+w),(0,255,0),2)
        cv2.putText(view,"Telefon",(n[0]+10,n[1]+10),cv2.FONT_HERSHEY_COMPLEX,2,(0,255,255),2)
    cv2.imshow("View",view)

    if cv2.waitKey(25) & 0xFF == ord('q'):
        break

camera.release()
cv2.destroyAllWindows()