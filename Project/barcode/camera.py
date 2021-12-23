import picamera
import time

path = '/home/pi/src/06_mutiemedia'

camera = picamera.PiCamera()

nowtime = time.strftime("%Y%m%d_%H%M%S")
try:
    camera.resolution = (640, 480)
    camera.start_preview()
    if input("카메라 촬영을 원하시면 1을 입력하세요") == '1':
        camera.capture('%s/%s.jpg'% (path, nowtime))
        print("사진 촬영")
finally:
    camera.stop_preview()

