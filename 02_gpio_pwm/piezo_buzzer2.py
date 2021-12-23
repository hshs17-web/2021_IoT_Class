import RPi.GPIO as GPIO
import time

BUZZER_PIN = 4

GPIO.setmode(GPIO.BCM)
GPIO.setup(BUZZER_PIN, GPIO.OUT)

# 주파수
pwm = GPIO.PWM(BUZZER_PIN, 262)
pwm.start(10) # duty cycle (0~100) . 소리 크기

melody_1 = [392, 392, 440, 440, 392, 392, 330]

melody_2 = [392, 392, 330, 330, 294]

melody_3 = [392, 330, 294, 330, 262]

try:
    for i in melody_1:
        pwm.ChangeFrequency(i)
        time.sleep(0.5)
    time.sleep(0.7)
    for i in melody_2:
        pwm.ChangeFrequency(i)
        time.sleep(0.5)
    time.sleep(1.0)
    for i in melody_1:
        pwm.ChangeFrequency(i)
        time.sleep(0.5)
    time.sleep(0.7)
    for i in melody_3:
        pwm.ChangeFrequency(i)
        time.sleep(0.5)
    time.sleep(1.0)

finally:
    pwm.stop()
    GPIO.cleanup()
    print('cleanup and exit')