import cv2
import numpy as np

image = cv2.imread("../AgirlikliToplama/misaka.jpg")

faceOfImage=image[0:100,70:150] #piksel aralıklarını belirtip resmin yüzü çektik
print(image.shape)

cv2.imshow("Misaka",image)
cv2.imshow("faceOfImage",faceOfImage)

#Resmi Uzatma
uzatilanResim = cv2.copyMakeBorder(image,100,100,100,100,cv2.BORDER_REPLICATE)
"""
Parametreler(src,top,bottom,left,right,borderType,dst,value)
src = resmin adresi
top = üstten kaç piksel ötelenecek
bottom = alttan kaç piksel ötelenecek
.
"""

#Resmi Aynalama
aynalananResim = cv2.copyMakeBorder(image,100,100,100,100,cv2.BORDER_REFLECT)

#Resmi Tekrar etme
tekrarlananResim = cv2.copyMakeBorder(image,100,100,100,100,cv2.BORDER_WRAP)


#Resmi Etrafını Sarma
sarinanResim = cv2.copyMakeBorder(image,100,100,100,100,cv2.BORDER_CONSTANT)


#Çerçeve
cerceveResim = cv2.copyMakeBorder(image,15,15,15,15,cv2.BORDER_CONSTANT,value =[255,0,0])

#Kare
cv2.rectangle(image,(50,100),(100,150),(0,0,255),2)



cv2.imshow("uzatilanResim",uzatilanResim)
cv2.imshow("aynalananResim",aynalananResim)
cv2.imshow("tekrarlananResim",tekrarlananResim)
cv2.imshow("sarinanResim",sarinanResim)
cv2.imshow("cerceveResim",cerceveResim)
cv2.imshow("image",image)



cv2.waitKey(0)
cv2.destroyAllWindows()