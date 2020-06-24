import cv2
import numpy as np

def main():
    image = cv2.imread("attackoftitans.jpg")
    print(image.shape)
    mask = np.zeros(image.shape[:2],np.uint8)
    """
    image ' nin boyutunu içeren bir zeros yani 0 matrix i oluşturduk
    image.shape[:2]=resmin boyutu, yüksekliği ve genişliği
    """

    bglModel = np.zeros((1,65),dtype = np.float64)#BackGroundModel
    fglModel = np.zeros((1,65),dtype = np.float64)#FrontGroundModel

    rect = (100,0,700,600)#(x,y,weight(genişlik),height(yükseklik))

    cv2.grabCut(image,mask,rect,bglModel,fglModel,5,cv2.GC_INIT_WITH_RECT)

    mask2 = np.where((mask == 0) | (mask == 2),0,1).astype(np.uint8)
    """
    (0-2) ArkaPlan -> Siyah
    (1-3) ÖnPlan   -> Beyaz
    """

    image = image*mask2[:,:,np.newaxis]

    cv2.imshow("Image",image)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()