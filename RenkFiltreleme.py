import cv2
import numpy as np

camera = cv2.VideoCapture(0)

low_value=np.array([100,150,50]) #Düşük değer        #100-130 değeri hue(renk) değer aralığı, (mavi)
                                                   #Saturation,150-255 rengin doygunluğu
high_value=np.array([130,255,255])#Yüksek değer    #

""" 
low_value=np.array([150,30,30]) #Kırmızı renk için değerler
                                                   
high_value=np.array([130,255,255])
"""

while True:

    ret,view = camera.read()
    """
    'ret'  paremetresi ; kameranın açık olup olmadığını kontrol ediyor
    açık ise True , kapalı ise False değerini alıyor , dtype = Boolean
    view  paremetresi ; kameranın kayıtta olduğu sürece aldığı görüntülerin bir matrix
    biçiminde array oluşturarak gorüntü paremetresini oluşturur.Toplam arka arkaya 3 kanalı 
    vardır bu (BGR) dır. Video birden fazla fotoğrafın bir araya gelmiş halidir. 
    """

    hsv = cv2.cvtColor(view,cv2.COLOR_BGR2HSV)
    """
    HSV=Hue/Renk[0-255] , Saturation/Doygunluk[0-255] , Value/Işık[0-255]
    """
    mask=cv2.inRange(hsv,low_value,high_value)

    and_image=cv2.bitwise_and(view,view,mask=mask)

    #Smoothed - Yumuşatma
    kernel=np.ones((15,15),dtype=np.float) / 225 #Sabit değerler
    smoothed = cv2.filter2D(and_image,-1,kernel)

    #k Blur
    blur= cv2.GaussianBlur(and_image,(15,15),0)

    #median - Ortalama
    median = cv2.medianBlur(and_image,15)

    #bilateral
    bilateral=cv2.bilateralFilter(and_image,15,75,75)


    cv2.imshow("Safe view(BGR)",view)
    cv2.imshow("HSV(HUE,STRATION,VALUE)",hsv)
    cv2.imshow("Mask",mask)
    cv2.imshow("FilterView",and_image)
    cv2.imshow("smoothed",smoothed)
    cv2.imshow("Blur",blur) #Smoothed den daha net oluyor
    cv2.imshow("Median",median) #Gürültü büyük ölçüde engellenmiş oluyor(favori)
    cv2.imshow("bilateral",bilateral) #Gürültü büyük ölçüde engellenmiş oluyor



    if cv2.waitKey(25) & 0xFF == ord('q'):
        break

camera.release()
cv2.destroyAllWindows()