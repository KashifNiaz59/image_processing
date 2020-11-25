import cv2

img=cv2.imread("imageProcessing.jpg")

# -------------- Gaussain Blur -----------------------
# uses Gaussian kernal. height & width of the kernal should be a positive and an odd number
# syntax : cv2.gaussainBlur(src,ksize,borderType)

#blur_image1=cv2.GaussianBlur(img,(0,0),0)
# gaussian blur not working on (0*0)
blur_image2=cv2.GaussianBlur(img,(1,1),0)
blur_image3=cv2.GaussianBlur(img,(3,3),0)
blur_image4=cv2.GaussianBlur(img,(5,5),0)
blur_image5=cv2.GaussianBlur(img,(7,7),0)

cv2.imshow("origianl image: ",img)
#cv2.imshow("Blur 0*0 :",blur_image1)
cv2.imshow("Blur 1*1 : ",blur_image2)
cv2.imshow("blur 3*3",blur_image3)
cv2.imshow("blur 5*5",blur_image4)
cv2.imshow("blur 7*7",blur_image5)

cv2.waitKey(0)
