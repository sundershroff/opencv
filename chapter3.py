import cv2

image = cv2.imread("./friends.png")
# Draw Line on image
image = cv2.line(
    img=image,
    pt1=(200,200),
    pt2=(500,500),
    color=(0,255,0),
    thickness=3,
)

# Draw Arrow on image
# image = cv2.arrowedLine(
#     img=image,
#     pt1=(500,500),
#     pt2=(200,200),
#     color=(0,255,0),
#     thickness=3,
# )

# Draw Rectangle on image
image = cv2.rectangle(
    img=image,
    pt1=(200,200),
    pt2=(500,500),
    color=(0,255,0),
    thickness=cv2.FILLED, # Fille The Box
)

# Draw Circle on image
# image = cv2.circle(
#     img=image,
#     center=(250,250),
#     radius=100,
#     color=(0,255,0),
#     thickness=2,
# )


cv2.imshow("Window",image)
cv2.waitKey(0)