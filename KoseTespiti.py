import numpy as np
import cv2

def main():

    image=cv2.imread("cizim.jpg")
    image_gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    image_gray=np.float32(image_gray)

    corners = cv2.goodFeaturesToTrack(image_gray,50,0.01,10)
    #0.01 = sağlamlık derecesi
    #10 = köşeler arası uzuaklık
    #50 = max köşe sayısı

    corners = np.int0(corners)

    for corner in corners:
        x,y=corner.ravel()
        cv2.circle(image,(x,y),3,(255,0,0),-1)


    cv2.imshow("image",image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()