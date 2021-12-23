import cv2

img = cv2.imread('test.jpg')
img2 = cv2.resize(img, (600, 400))

gray = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)

cv2.imshow('BTS', img2)
cv2.imshow('BTS_GRAY', gray)

while True:
    if cv2.waitKey() == ord('q'):
        break

cv2.imwrite('BTS_GRAY.jpg', gray)

cv2.destroyAllWindows()