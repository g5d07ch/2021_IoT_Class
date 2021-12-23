import RPi.GPIO as GPIO
import time

import board
import busio
import adafruit_adxl34x

PIN_LED = 19
BUZZER_PIN = 13
SERVO_PIN = 26
GPIO.setmode(GPIO.BCM)
GPIO.setup(PIN_LED, GPIO.OUT)
GPIO.setup(BUZZER_PIN, GPIO.OUT)
GPIO.setup(SERVO_PIN, GPIO.OUT)

pwm = GPIO.PWM(BUZZER_PIN, 262)
pwm1 = GPIO.PWM(SERVO_PIN, 50)
pwm.start(10)
pwm1.start(7.5)

melody = [262, 294, 330, 349, 392, 440, 494, 523]

try:
    while True:
        val = input('1: 0도, 2: -90도, 3: +90도, 9: Exit > ')
        if val == '1':
            pwm1.ChangeDutyCycle(7.5)    # 0도
        elif val == '2':
            #pwm.ChangeDutyCycle(5)     # -45도
            pwm1.ChangeDutyCycle(2.5)    # -45도
        elif val == '3':
            #pwm.ChangeDutyCycle(10)    # +45도
            pwm1.ChangeDutyCycle(12.5)   # +90도
        elif val == '9':
            break
finally:
    pwm.stop()
    GPIO.cleanup()

for i in melody:
    pwm.ChangeFrequency(i)
    time.sleep(1)

pwm.stop()

for i in range(10):
    GPIO.output(PIN_LED, GPIO.HIGH)
    print("Led on")
    time.sleep(1)
    GPIO.output(PIN_LED, GPIO.LOW)
    print("Led off")
    time.sleep(1)



GPIO.cleanup()