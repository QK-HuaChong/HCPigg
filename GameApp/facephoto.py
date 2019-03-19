import cv2

cap = cv2.VideoCapture(0)
while True:
    # get a frame
    pathf = 'G:\\haarcascadesdata\\haarcascades\\haarcascade_frontalface_default.xml'
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    face_cascade = cv2.CascadeClassifier(pathf)
    faces = face_cascade.detectMultiScale(gray,scaleFactor=1.1,minNeighbors=5,minSize=(30, 30),flags = cv2.CASCADE_SCALE_IMAGE)
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + w), (0, 255, 0), 1)
        # show a frame
        cv2.imshow("Face recognition ", frame)
    if cv2.waitKey(1) & 0xFF == ord(' '):
        cv2.imwrite("F:/Pic/fangjian.jpeg", frame)
        break
cap.release()
cv2.destroyAllWindows()