import cv2

cv2.imread("imageProcessing")

# ---- median blur ------
# the median of all the pixels of the image is calculated inside the kernal area. central value is then placed with resultant median value.
# median blurring is used when there are salt and pepper noise in the image
# cv2.medianBlur(source,int)

median_blur=cv2.medianBlur(img,5)

cv2.imshow("median blur 5",median_blur)
cv2.imshow("original",img)

cv2.waitKey(0)

# ** salt and pepper noise
# this noise is caused by sharp and sudden disturbances in the image signal.
# it presents itself as sparsely occuring white and black pixels
