import cv2
import numpy as np

def main():
    logo=cv2.imread("python_logo.png")

    print("Resmin özellikler",logo.shape)

    #Resmin boyutlarını 2 katına çıkarmak için
    x2_bigger_logo=cv2.pyrUp(logo)
    print("Resmin x2_logo",x2_bigger_logo.shape)

    # Resmin boyutlarını 2 kat küçültmek için
    x2_smaller_logo = cv2.pyrDown(logo)
    print("Resmin x2_smaller_logo", x2_smaller_logo.shape)

    resim=np.zeros((400,400,3),dtype="uint8")#400X400 boyutunda 3kanalı olan matrix (Siyah resim)
    print(resim)

    cv2.rectangle(resim,(100,300),(300,100),(255,255,255),5)

    cv2.imshow("Resim", resim)
    cv2.imshow("Logo", logo)
    cv2.imshow("x2_bigger_logo", x2_bigger_logo)
    cv2.imshow("x2_smaller_logo", x2_smaller_logo)


    cv2.waitKey(0)
    cv2.destroyAllWindows()



if __name__ == "__main__":
    main()