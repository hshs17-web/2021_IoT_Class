import picamera
import time

path = '/home/pi/src/06_mutiemedia'

camera = picamera.PiCamera()

nowtime = time.strftime("%Y%m%d_%H%M%S")
try:
    camera.resolution = (640, 480)
    camera.start_preview()
    while True:
        value = input("photo: 1, video: 2, exit: 9 ")
        if value == '1':
            camera.capture('%s/%s.jpg'% (path, nowtime))
            print("사진 촬영")
        elif value == '2':
            camera.start_recording('%s/%s.h264'% (path, nowtime))
            print("동영상 촬영")
            input('press enter to stop')
            camera.stop_recording()
        elif value == '9':
            exit()
        else:
            print("incorrect command")

finally:
    camera.stop_preview()

