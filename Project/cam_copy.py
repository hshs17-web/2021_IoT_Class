import cv2
import time
cap = cv2.VideoCapture(0)
if not cap. isOpened():
    print('Camera open failed')
    exit()
while True:
    ret, frame = cap.read()
    if not ret:
        break
    cv2.imshow('frame', frame)
    if cv2.waitKey(10) == 27:
        break
    
cap.release()
cv2.destroyAllwindows()