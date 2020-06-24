import cv2
import numpy as np

image = cv2.imread("attackOfTitans.jpg")

#Laplacian - Filtreleme
laplacian = cv2.Laplacian(image,cv2.CV_64F)

#Sobel - Filtreleme
sobel_vectiral = cv2.Sobel(image,cv2.CV_64F,1,0,ksize=5)#1,0 = dikey olduğunu gösterir
sobel_horizantol = cv2.Sobel(image,cv2.CV_64F,0,1,ksize=5)#0,1 = yatay olduğunu gösterir

#Canny - Filtreleme
edgies=cv2.Canny(image,100,200)#100,200 değerleri ile oynayarak filtrelemede değişiklik yapılır.

cv2.imshow("OrginalImage",image)
cv2.imshow("laplacian",laplacian)
cv2.imshow("sobel_vectiral",sobel_vectiral)
cv2.imshow("sobel_horizantol",sobel_horizantol)
cv2.imshow("edgies",edgies)


cv2.waitKey(0)
cv2.destroyAllWindows()