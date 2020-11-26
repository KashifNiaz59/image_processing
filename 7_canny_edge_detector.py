import cv2

cv2.imread("imageProcessing.jpg")

# canny edge detector or optimal detector
# cv2.Canny(image,minVla,maxVal)

canny_image=cv2.Canny(img,100,200)

cv2.imshow("original value",img)
cv2.imshow("Canny Edge Detector",canny_image)

cv2.waitKey(0)
