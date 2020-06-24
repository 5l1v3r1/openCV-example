import cv2
import numpy as np

#VideoCapture() , ()->
#0 , Pc deki tanımlı olan kamerayı alacak
#1 , usb
#2 , Video Adresi , VideoCapture(ajdha.mp4)
camera= cv2.VideoCapture(0)


while True:
    ret,kare=camera.read()

    cv2.imshow("Camera",kare)

    if cv2.waitKey(25) & 0xFF == ord('q'):
        break

camera.release()
cv2.destroyAllWindows()