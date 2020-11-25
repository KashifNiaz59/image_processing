# prerequisite : 1_basics.py for understanding it

import cv2

img=cv2.imread("imageProcessing")
height,width=img.shape[0:2]

# ------ CROP IMAGE -------

# start row & column image
startRow=int(height*.15)
startCol=int(width*.15)

# to end row & column
endRow=int(height*.85)
endCol=int(height*.85)

croppedImage=img[startRow:endRow,startCol:endCol]

cv2.imshow('original image',img)
cv2.imshow('cropped image',croppedImage)

cv2.waitKey(0)
