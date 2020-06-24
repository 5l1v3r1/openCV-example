import numpy as np
import cv2

def main():
    image=np.zeros((400,400,3),dtype="uint8")
    print(image)
    #Resmi beyaz yapmak istersem = resim.fill(255)
    image.fill(255)

    #Çizgi-Line
    cv2.line(image,(100,300),(300,100),(0,0,0),5)

    #Daire,Circle
    cv2.circle(image,(200,200),60,(0,255,0),5)

    #Yazı,Text
    cv2.putText(image,"Mekatronik Dunyasi",(35,35),cv2.FONT_HERSHEY_COMPLEX,1,(255,0,0),2)

    #Kare,Rectangle
    cv2.rectangle(image,(250,150),(150,250),(150,150,0),2)

    cv2.imshow("BackGround",image)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()