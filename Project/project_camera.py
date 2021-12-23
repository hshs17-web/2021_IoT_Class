import cx2

cap = cv2.VideoCapture(0)

if not cap. isOpened():
    print('Camera open failed')
    exit()
while True:
    ret, frame = cap.read()
    if not ret:
        break
    cv2.imshow('frmae', frame)
    if distance < 30:
        cv2.imwrite('stranger.jpg', frame)
cap.release()
cv2.destroyAllwindows()