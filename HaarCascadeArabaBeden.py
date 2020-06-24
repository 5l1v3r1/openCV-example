import cv2
import numpy as np

video = cv2.VideoCapture("uskudar.mp4")
insan_bulucu = cv2.CascadeClassifier("haarcascade_fullbody.xml")

while True:
    ret,kare = video.read()

    gri_ton = cv2.cvtColor(kare,cv2.COLOR_BGR2GRAY)

    bodys = insan_bulucu.detectMultiScale(gri_ton,1.1,4)

    for (x,y,w,h) in bodys:
        cv2.rectangle(kare,(x,y),(x+w,y+h),(255,0,0),3)


    cv2.imshow("video",kare)

    if cv2.waitKey(25) & 0xFF == ord('q'):
        break

video.release()
cv2.destroyAllWindows()