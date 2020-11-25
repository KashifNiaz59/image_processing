# pre requisits : 1_basics.py

import cv2

img=cv2.read("imageProcessing.jpg")
height,width=img.shape[0:2]

# ------ resize Image ------

# resize(src,dsize,fx,fy)
# src = source of the image
# dsize = desired size of the output image
# fx = scalling factor along x-axis
# fy = scalling factor along y-axis

# method-1
resizeImg=cv2.resize(img,(0,0),fx=1.75,fy=1.75)

# method-2
resizeImg1=cv2.resize(img,(550,350))

cv2.imshow('resized image',resizeImg)
cv2.imshow('resized image 1',resizeImg1)

cv2.waitKey(0)
