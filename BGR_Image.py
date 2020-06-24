import cv2

image = cv2.imread("yesilcam.png") #Opencv -> BGR(Blue,Green,Red)

print(image)
"""
  Blue Green Red       Blue + Green + Red = Color -> For one pixel   
[[[151  76  71]       151     76    71
  [149  64  63]
  [148  58  60]
  ...
  [159  85  70]
  [152  88  70]
  [154 100  83]]
  ...
"""

print(type(image))
#class 'numpy.ndarray' , type=array(dizi,matris)

print(image.size)
#piksel sayısı 855015
#HeightxWidthxChannelSize(3) = 855015

print(image.dtype)
#uint8 , 8 bit integer

print(image.shape)
"""
(595, 479, 3) = Genişlik , Yükseklik , Renk kanal sayısı
595x479x3 = 855015
"""


image_gray = cv2.imread("yesilcam.png",0) #Opencv -> BGR(Blue,Green,Red)
"""
image.shape=(595,479,1) tek bir kanal var , gri 
"""
print(image_gray)

print(image_gray.item(50,40))
#50,40 konumundaki pikselin değeri nedir

print(image.item(100,100,2))
#50,40, konumundaki pikselin  2.Kanaldaki(green) değeri

print(image.item(200,200,0)) #Blue
print(image.item(200,200,1)) #Green
print(image.item(200,200,2)) #Red


cv2.imshow("Yesilcam",image)
cv2.imshow("Yesilcam_gray",image_gray)

cv2.waitKey(0)
cv2.destroyAllWindows()
