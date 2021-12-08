import cv2
cam=cv2.VideoCapture(0)
while True:
    _,img = cam.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
    faces = face_cascade.detectMultiScale(gray,1.1,4)
    for i in range(len(faces)):
        cv2.rectangle(img, (faces[i][0], faces[i][1]), (faces[i][0] + faces[i][2], faces[i][1] + faces[i][3]),(0, 0, 255), 3)
    cv2.imshow('Image',img)
    if cv2.waitKey(20) & 0xFF == 27:
        break
cv2.destroyAllWindows()