import cv2
face_patterns = cv2.CascadeClassifier('./cascades/haarcascade_frontalface_default.xml')
cap = cv2.VideoCapture(0)
# 定义解码器并创建VideoWrite对象
# linux: XVID、X264; windows:DIVX
# 20.0指定一分钟的帧数
fourcc = cv2.VideoWriter_fourcc(*'MJPG')
out = cv2.VideoWriter('output.mp4', fourcc, 20.0, (640, 480))

while(cap.isOpened()):
    # get a frame
    ret, frame = cap.read()
    if ret == True:
        frame = cv2.flip(frame, 1)
    faces = face_patterns.detectMultiScale(frame, scaleFactor=1.1, minNeighbors=5, minSize=(100, 100))
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
        # 写入帧
        out.write(frame)
    # show a frame
    cv2.imshow("capture", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()