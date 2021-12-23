import RPi.GPIO as GPIO
import time

lp = [17, 27, 22]
GPIO.setmode(GPIO.BCM)

for i in range(3):
    GPIO.setup(lp[i], GPIO.OUT)


for i in range(9):
    GPIO.output(lp[i%3], GPIO.HIGH)
    time.sleep(2)
    GPIO.output(lp[i%3], GPIO.LOW)
    time.sleep(0.5)

GPIO.cleanup()