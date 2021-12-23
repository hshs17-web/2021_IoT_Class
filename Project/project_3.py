#프로젝트 실행을 위한 모듈 
import time
from lcd import drivers 
import adafruit_ssd1306 
import board
import cv2
import digitalio
import RPi.GPIO as GPIO
import pigpio #서보모터가 떨리지 않도록 잡아주는 모듈

#GPIO핀 설정
SERVO_PIN = 18
TRIG_PIN = 4
ECHO_PIN = 14
BUZZER_PIN = 6

#GPIO 모드 설정
GPIO.setmode(GPIO.BCM)
GPIO.setup(TRIG_PIN, GPIO.OUT)
GPIO.setup(BUZZER_PIN, GPIO.OUT)
GPIO.setup(ECHO_PIN, GPIO.IN)
cap = cv2.VideoCapture(0)
pwm = GPIO.PWM(BUZZER_PIN, 330)
display = drivers.Lcd()
GPIO.setup(SERVO_PIN, GPIO.OUT)
pwm1 = GPIO.PWM(SERVO_PIN, 50)
pi = pigpio.pi()
pi.set_servo_pulsewidth(18, 500)
time.sleep(1)



if not cap. isOpened():
    print('Camera open failed')
    exit()
    
try:
    while True:      
        #카메라 촬영하기
        ret, frame = cap.read()
        if not ret:
            break
        cv2.imshow('frame', frame)
        if cv2.waitKey(10) == 27:
            break
        #초음파 센서를 이용한 거리 측정
        GPIO.output(TRIG_PIN, True)
        time.sleep(0.00001)
        GPIO.output(TRIG_PIN, False)
        while GPIO.input(ECHO_PIN) == 0:
            pass
        start = time.time()
        while GPIO.input(ECHO_PIN) == 1:
            pass
        stop = time.time()
        
        #초음파의 시간차를 이용해 거리 측정하기
        duration_time = stop - start
        distance = duration_time*17160

        #거리가 15 이하라면...
        if distance < 15:
            print('Distance: %.1fcm' % distance) #연결된 컴퓨터에 거리 출력
            display.lcd_display_string("someone detected", 1) #LCD에 거리를 출력하고 누군가 감지되었음을 출력
            display.lcd_display_string('Distance: %.1fcm' % distance, 2)
            cv2.imwrite('stranger.jpg', frame) #사진 촬영
            pi.set_servo_pulsewidth(18, 1500) #서보 모터 회전을 통한 문 닫기
            time.sleep(1)
            pwm.start(50) #피에조 부저를 통해 감지되었음을 알린다
            time.sleep(5)
            pwm.stop()
            
finally:
    #장치 정리
    GPIO.cleanup()
    cap.release()
    cv2.destroyAllWindows()
    print('cleanup and exit')
