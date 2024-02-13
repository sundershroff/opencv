import cv2

# Original Image

image = cv2.imread("friends.png")


bw = cv2.resize(image,(300,200))
# bw = image[0:200, 500:800] # image[height, width]
cv2.imshow("Original", bw)
# cv2.imshow("Cropped",cropped_image)

cv2.waitKey(0)