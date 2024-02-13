import cv2

# Reading Image
# image = cv2.imread("./assets/person.jpg")

# #Showing Image
# cv2.imshow("Window Name",image)

# # Wait Until Type Any Key
# cv2.waitKey(0)


# Reading Video
# video = cv2.VideoCapture("./video.mp4")

# while True:
#     success, frame = video.read()
    
#     cv2.imshow("Frame By Frame",frame)
    
#     if cv2.waitKey(1) == ord('a'):
#         break 
# video.release()


# Using Webcam
video = cv2.VideoCapture(1)

video.set(3, 100)
video.set(4,50)
video.set(10, 100)

while True:
    success, frame = video.read()
    cv2.imshow("Frame Here",frame)
    
    if cv2.waitKey(1) == ord("a"):
        break
video.release()