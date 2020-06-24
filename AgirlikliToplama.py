import cv2
import numpy as np

def main():
    image1=cv2.imread("misaka.jpg")
    image2=cv2.imread("eren.jpg")

    print("eren resim değerleri: Yükseklik:{},Genişlik:{},KanalSayısı:{}".format(image1.shape[0],image1.shape[1],image1.shape[2]))
    print("misaka resim değerleri: Yükseklik:{},Genişlik:{},KanalSayısı:{}".format(image2.shape[0],image2.shape[1],image2.shape[2]))



    cv2.imshow("Misaka",image1)
    cv2.imshow("Eren",image2)

    add=cv2.add(image1,image2)

    agirlikli_toplam=cv2.addWeighted(image1,0.2,image2,0.8,0)
    #mage1,0.2=image1 den nekadar pixel yoğunluğu olsun
    #image2,0.8=image2 de nekadar pixel yoğunluğu olsun
    #Bu alpha(0.2) ve beta(0.8) değerlerinin toplamı 1 olacak


    cv2.imshow("toplam",add)
    cv2.imshow("AğırlıklıToplama",agirlikli_toplam)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()