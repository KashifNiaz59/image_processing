import cv2

img=cv2.imread("imageProcessing.jpg")
height,widht=img.shape[0:2]


# ****** ROTATION OF THE IMAGE ******

# to get the rotation matrix, we use getRotationMatrix2D() ----> cv2
# cv2.getRotationMatrix2D(center,angle,scale)
# center = center of the image
# angle = how much degree you want to rotate the image
# scale = .5(half of the image), 1(original of image), 1.5( one and half size of image)

rotationMatrix=cv2.getRotationMatrix2D((width/2,height/2),180,5)

# to rotate the image, we have method wrapAffine() ----> cv2
# cv2.warpAffine(img,rotationMatrix,(width,height))

rotatedImage=cv2.warpAffine(img,rotationMatrix,(width,height))

cv2.imshow("Rotated Image",rotatedImage)
cv2.waitKey(0)
