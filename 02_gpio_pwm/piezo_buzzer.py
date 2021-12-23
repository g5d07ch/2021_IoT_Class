import RPi.GPIO as GPIO
import time

BUZZER_PIN = 4

GPIO.setmode(GPIO.BCM)
GPIO.setup(BUZZER_PIN, GPIO.OUT)

pwm = GPIO.PWM(BUZZER_PIN, 1)
pwm.start(10)

melody = [392, 392, 440, 440, 392, 392, 330, 392, 392, 330, 330, 294, 392, 392, 440, 440, 392, 392, 330, 392, 330, 294, 330, 262]
stop = [0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 1, 0.5, 0.5, 0.5, 0.5, 1.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 1, 0.5, 0.5, 0.5, 0.5, 1.5]
try:
    for i in range(24):
        pwm.ChangeFrequency(melody[i])
        time.sleep(stop[i])

finally:    
    pwm.stop()
    GPIO.cleanup()