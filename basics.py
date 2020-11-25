# ********** some basics of the image ******************
# i have an image " imageProcessing.jpg "

# using opencv library
# import it

import cv2

# **** READ IMAGE ----> imread()
img=cv2.imread("imageProcessing")


# to display image in 2-D array
# check the type of the array
print(type(img))
print(img)


# **** SHOWING IMAGE ---> imshow()
cv2.imshow('original image',img)
cv2.waitKey(0)
# the waitkey function take time as an argument in milliseconds as a delay for the window to close. 
# here we set the time to zero to show the window forever until we close it manually


# **** getting HEIGHT and WIDTH of the picture
height, width=img.shape[0:2]
print("height :",height)
print("width :",width)


