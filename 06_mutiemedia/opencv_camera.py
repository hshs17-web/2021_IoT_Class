import cv2

# 카메라 장치 열기
cap = cv2.VideoCapture(0)

if not cap.isOpened():
     print('Camera open failed')
     exit()

#카메라 사진찍기
# ret, frame = cap.read()
# cv2.imshow('frame', frame)
# cv2.waitKey(0)
# cv2.imwrite('ouput.jpg', frame)
#카메라 동영상찍기
while True:
    ret, frame = cap.read()
    if not ret:
        break
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    edge = cv2.Canny(frame, 50, 100)
    cv2.imshow('gray', gray)
    cv2.imshow('frame', frame)
    cv2.imshow('edge', edge)
    
    
    if cv2.waitKey(10) == 13:
        break

cap.release()
cv2.destroyAllWindows()

