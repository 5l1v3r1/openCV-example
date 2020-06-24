import cv2
import numpy as np

def main():

    kamera = cv2.VideoCapture(0)

    fourcc = cv2.VideoWriter_fourcc(*"XVID") #format

    kayit = cv2.VideoWriter("kayit.avi",fourcc,20,(640,480))


    while True:
        ret,goruntu=kamera.read()

        kayit.write(goruntu)

        #Ters görüntü için
        """
        ters_goruntu = cv2.flip(goruntu,0)
        """

        cv2.imshow("goruntu",goruntu)

        if cv2.waitKey(20) & 0XFF == ord('q'):
            break


    kamera.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()