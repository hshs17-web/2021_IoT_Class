import RPi.GPIO as GPIO
import time
import cv2
import threading
import board
import digitalio
from PIL import Image, ImageDraw, ImageFont
import adafruit_ssd1306

TRIG_PIN = 4
ECHO_PIN = 14
BUZZER_PIN = 6

GPIO.setmode(GPIO.BCM)
GPIO.setup(TRIG_PIN, GPIO.OUT)
GPIO.setup(BUZZER_PIN, GPIO.OUT)
GPIO.setup(ECHO_PIN, GPIO.IN)
cap = cv2.VideoCapture(0)
pwm = GPIO.PWM(BUZZER_PIN, 330)


RESET_PIN = digitalio.DigitalInOut(board.D4)
i2c = board.I2C()
oled = adafruit_ssd1306.SSD1306_I2C(128, 64, i2c, addr=0x3c, reset=RESET_PIN)
oled.fill(0)
oled.show()
image = Image.new("1", (oled.width, oled.height))
draw = ImageDraw.Draw(image)
font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 28)
font2 = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 14)


if not cap. isOpened():
    print('Camera open failed')
    exit()
def cvcamera(running_value):
    while running_value:  
        ret, frame = cap.read()
        if not ret:
            break
        cv2.imshow('frmae', frame)
        if distance < 30:
            cv2.imwrite('stranger.jpg', frame)
        if cv2.waitKey(10) == 27:
            break
try:
    t = threading.Thread(target=cvcamera, args=(1))
    while True:      
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
            time.sleep(0.1)
            draw.text((0, 30), "사람이 감지되었습니다", font=font2, fill=255)
            draw.text((34, 46), 'Distance: %.1fcm' % distance, font=font2, fill=255)
            pwm.start(50)
            time.sleep(5)
            pwm.stop()
        time.sleep(0.1)
finally:
    GPIO.cleanup()
    cap.release()
    cv2.destroyAllWindows()
    print('cleanup and exit')