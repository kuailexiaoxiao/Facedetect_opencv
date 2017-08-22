import cv2


def generate():
    face_cascade = cv2.CascadeClassifier('./cascades/haarcascade_frontalface_default.xml')
    cap = cv2.VideoCapture(0)
    count = 0
    while(True):
        ret, frame = cap.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)  # 转化为灰度图，因为人脸检测需要这样的色彩空间
        faces = face_cascade.detectMultiScale(gray, 1.3, 5)  # 进行人脸检测， 1.3的压缩率， 每个人脸矩形保留近邻数目的最小值
        # 检测操作的返回值为人脸矩形数组， 函数cv2.tectangle允许通过坐标来绘制矩形
        for (x, y, w, h) in faces:
            img = cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 225, 0), 2)  # x和y是左上角坐标，（255）是颜色，2是矩形框的宽度
            f = cv2.resize(gray[y:y+h, x:x+w], (200, 200))
        cv2.imshow('camera', frame)
        if cv2.waitKey(1) & 0xff == ord('c'):
            cv2.imwrite('./data/%s.pgm' % str(count), f)
            print(count)
            count += 1
            continue
        if cv2.waitKey(1) & 0xff == ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    generate()

