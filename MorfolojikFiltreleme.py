import cv2
import numpy as np

camera = cv2.VideoCapture(0)

low_value = np.array([88,50,50])
high_value = np.array([130,255,255])


while True:
    ret,view = camera.read()

    hsv = cv2.cvtColor(view,cv2.COLOR_BGR2HSV)

    mask = cv2.inRange(hsv,low_value,high_value)

    filter_view = cv2.bitwise_and(view,view,mask=mask)


    kernel = np.ones((5,5),np.uint8)

    erosion = cv2.erode(mask,kernel,iterations=1)#Filtlenecek resmin içindeki boşlukları doldurur
    diolation = cv2.dilate(mask,kernel,iterations=1)#Filtlenecek resimndeki boşlukları genişletir

    opening = cv2.morphologyEx(mask,cv2.MORPH_OPEN,kernel)#Filtlenecek resmin içindeki boşlukları açar
    closing = cv2.morphologyEx(mask,cv2.MORPH_CLOSE,kernel)#Filtlenecek resmin içindeki boşlukları açar

    cv2.imshow("erosion",erosion)
    cv2.imshow("diolation",diolation)
    cv2.imshow("filter_view",filter_view)
    cv2.imshow("opening", opening)
    cv2.imshow("closing", closing)

    if cv2.waitKey(25) & 0xFF == ord('q'):
        break

camera.release()
cv2.destroyAllWindows()