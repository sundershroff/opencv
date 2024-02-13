import cv2

image = cv2.imread("friends.png")

roi = cv2.selectROI(image)
xAxis = roi[0]
yAxis = roi[1]
width = roi[2]
height = roi[3]

image = cv2.rectangle(
    img=image,
    pt1=(xAxis, yAxis),
    pt2=(xAxis+width, yAxis+height),
    thickness=2,
    color=(0,0,255)
)
cv2.imshow("Window Name",image)
cv2.waitKey(0)
cv2.imwrite("./result.jpg",image) 
print(roi)