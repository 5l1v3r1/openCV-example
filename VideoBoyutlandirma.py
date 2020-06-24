import cv2
import numpy as np

camera = cv2.VideoCapture(0)

#kamerayı boyutlandırmak için
camera.set(3,300)#genişlik
camera.set(4,200)#yükseklik

def main():
    while True:
        ret,kare=camera.read()

        grayVideo=cv2.cvtColor(kare,cv2.COLOR_BGR2GRAY)

        cv2.imshow("Video",kare)
        cv2.imshow("Video_GRAY",grayVideo)


        if cv2.waitKey(25) & 0xFF==ord('q'):
            break
    kare.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()