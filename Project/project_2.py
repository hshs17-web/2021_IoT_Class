import time
from lcd import drivers
import adafruit_ssd1306
import board
import cv2
import digitalio
import RPi.GPIO as GPIO
from PIL import Image, ImageDraw, ImageFont

TRIG_PIN = 4
ECHO_PIN = 14
BUZZER_PIN = 6

GPIO.setmode(GPIO.BCM)
GPIO.setup(TRIG_PIN, GPIO.OUT)
GPIO.setup(BUZZER_PIN, GPIO.OUT)
GPIO.setup(ECHO_PIN, GPIO.IN)
cap = cv2.VideoCapture(0)
pwm = GPIO.PWM(BUZZER_PIN, 330)
display = drivers.Lcd()

if not cap. isOpened():
    print('Camera open failed')
    exit()
try:
    while True:      
        ret, frame = cap.read()
        if not ret:
            break
        cv2.imshow('frame', frame)
        if cv2.waitKey(10) == 27:
            break
        
        GPIO.output(TRIG_PIN, True)
        time.sleep(0.00001)
        GPIO.output(TRIG_PIN, False)
        while GPIO.input(ECHO_PIN) == 0:
            pass
        start = time.time()
        while GPIO.input(ECHO_PIN) == 1:
            pass
        stop = time.time()
        
        duration_time = stop - start
        distance = duration_time*17160
    
        if distance < 30:
            print('Distance: %.1fcm' % distance)
            display.lcd_display_string("someone detected", 1)
            display.lcd_display_string('Distance: %.1fcm' % distance, 2)
            cv2.imwrite('stranger.jpg', frame)
            pwm.start(50)
            time.sleep(5)
            pwm.stop()
finally:
    GPIO.cleanup()
    cap.release()
    cv2.destroyAllWindows()
    display.lcd_clear()
    print('cleanup and exit')
