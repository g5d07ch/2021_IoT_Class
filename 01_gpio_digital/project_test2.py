import RPi.GPIO as GPIO
import time
import Adafruit_ADXL345

pin = 26

GPIO.setmode(GPIO.BCM)
GPIO.setup(pin, GPIO.OUT)
p=GPIO.PWM(pin, 50)
p.start(6)
accel = Adafruit_ADXL345.ADXL345()

print('Printing X, Y, Z axis values, press Ctrl-C to quit...')

try:
    while True:
    
        x, y, z = accel.read()

        print('X={0}, Y={1}, Z={2}'.format(x, y, z))
        
        if y < -250 :
            p.ChangeDutyCycle(2)
        elif y < -240 :
            p.ChangeDutyCycle(2.5)
        elif y < -230 :
            p.ChangeDutyCycle(2.8) 
        elif y < -200 :
            p.ChangeDutyCycle(3)    
        elif y < -160 :
            p.ChangeDutyCycle(3.5)
        elif y < -110 :
            p.ChangeDutyCycle(4.3)
        elif y < -80 :
            p.ChangeDutyCycle(4.5)
        elif y < -40 :
            p.ChangeDutyCycle(5)
        elif y < -15 :
            p.ChangeDutyCycle(5.5)
        elif y < 15 :
            p.ChangeDutyCycle(6)
        elif y < 50 :
            p.ChangeDutyCycle(6.5)
        elif y < 110 :
            p.ChangeDutyCycle(7.5)           
        elif y < 160 :
            p.ChangeDutyCycle(8)
        elif y < 185 :
            p.ChangeDutyCycle(8.5)
        elif y < 210 :
            p.ChangeDutyCycle(8.8)
        elif y < 230 :
            p.ChangeDutyCycle(9.2)
        elif y < 250 :
            p.ChangeDutyCycle(9.5)
        elif y < 270 :
            p.ChangeDutyCycle(11)  
    
        time.sleep(0.5)
       
    
except KeybordInterrupt:
    p.stop()
GPIO.cleanup()