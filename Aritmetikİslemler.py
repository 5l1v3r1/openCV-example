import cv2
import numpy as np

def main():
    dev_resmi=cv2.imread("dev.jpg")
    misaka_resmi=cv2.imread("misaka.jpg")
    logo=cv2.imread("logo.jpg")


    pythonLogoGray= cv2.cvtColor(logo,cv2.COLOR_BGR2GRAY)

    yukseklik,genislik,kanal=logo.shape

    print("Genişlik:{},Yükseklik:{},Kanal:{}".format(genislik,yukseklik,kanal))

    cv2.imshow("Dev",dev_resmi)
    cv2.imshow("Misaka",misaka_resmi)
    cv2.imshow("pythonLogoGray",pythonLogoGray)

    ROI=dev_resmi[0:yukseklik,0:genislik]

    ret,mask = cv2.threshold(pythonLogoGray,10,255,cv2.THRESH_BINARY)
    #pythonLogoGray pixel değeri 10 un üzerinde olan tüm değerleri 255(Beyaz)yapacağız
    #ret=maxdeğer(10) , mask=THRESH işlemi görmüş remimin matrixi

    mask_invert=cv2.bitwise_not(mask)
    #mask tam tersini aldık
    cv2.imshow("Mask",mask)

    dev_backGround=cv2.bitwise_and(ROI,ROI,mask = mask_invert)

    add=cv2.add(dev_backGround,logo)

    cv2.imshow("Mask", mask)
    cv2.imshow("dev_backGround", dev_backGround)
    cv2.imshow("AddPhoto", add)

    dev_resmi[0:yukseklik,0:genislik] = add

    cv2.imshow("DevResmıVeLogo",dev_resmi)

    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()