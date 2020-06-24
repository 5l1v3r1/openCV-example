import cv2 
import numpy as np

video = cv2.VideoCapture("fsmMobese.mp4")
insan_bulucu = cv2.CascadeClassifier("cars.xml")

while True:
    ret,kare = video.read()

    gri_ton = cv2.cvtColor(kare,cv2.COLOR_BGR2GRAY)

    cars = insan_bulucu.detectMultiScale(gri_ton,1.1,4)

    for (x,y,w,h) in cars:
        cv2.rectangle(kare,(x,y),(x+w,y+h),(255,0,0),3)


    cv2.imshow("video",kare)

    if cv2.waitKey(10) & 0xFF == ord('q'):
        break

video.release()
cv2.destroyAllWindows()