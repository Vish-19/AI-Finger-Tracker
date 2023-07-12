import cv2
import mediapipe as mp
import time
cap=cv2.VideoCapture(0)
ctime=0
ptime=0
f=mp.solutions.face_detection
face=f.FaceDetection()
mpDraw=mp.solutions.drawing_utils

while True:
    _,img=cap.read()
    img1 = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = face.process(img1)
    if results.detections:
        for id,lm in enumerate(results.detections):
            hi, w, c = img.shape
            #print(id,lm.score, lm.location_data.relative_bounding_box)
            #mpDraw.draw_detection(img,lm) add it only if you need face points
            b=lm.location_data.relative_bounding_box
            bb= int(b.xmin * w), int(b.ymin * hi),\
                int(b.width * w), int(b.height * hi)
            if lm.score[0] *100 > 95:
                cv2.rectangle(img, bb, (0, 255, 0), 3)
            else:
                cv2.rectangle(img, bb, (0, 0, 255), 3)
            #cv2.putText(img,str(int(lm.score[0] * 100)), (bb[0],bb[1]-20), cv2.FONT_HERSHEY_PLAIN, 2, (255, 0, 255))

    ctime = time.time()
    fps = 1 / (ctime - ptime)
    ptime = ctime
    img = cv2.resize(img, (1024, 512))
    cv2.putText(img,"FPS="+str(int(fps)), (10, 70), cv2.FONT_HERSHEY_PLAIN,2, (255, 0, 255))
    cv2.imshow("Image", img)
    if cv2.waitKey(50) & 0xFF == 27:
        break