import cv2

camera = cv2.VideoCapture("HULK.mp4")
dataset = cv2.CascadeClassifier("./models/default.xml")

while True:
    success, frame = camera.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    origin = dataset.detectMultiScale(gray)
    for photo in origin:
        x = photo[0]
        y = photo[1]
        w = photo[2]
        h = photo[3]
        if w > 100:
            frame = cv2.rectangle(
                img=frame,
                pt1=(x, y),
                pt2=(x + w, y + h),
                thickness=3,
                color=(0, 0, 255)
            )
    cv2.imshow("Window Name", frame)
    if cv2.waitKey(1) == ord('a'):
        break
camera.release()