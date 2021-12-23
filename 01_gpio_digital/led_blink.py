import RPi.GPIO as GPIO
import time

PIN_LED = 4
GPIO.setmode(GPIO.BCM)
GPIO.setup(PIN_LED, GPIO.OUT)

for i in range(10):
    GPIO.output(PIN_LED, GPIO.HIGH)
    print("Led on")
    time.sleep(1)
    GPIO.output(PIN_LED, GPIO.LOW)
    print("Led off")
    time.sleep(1)

GPIO.cleanup()