import RPi.GPIO as GPIO
import time 
import board 
import busio
import adafruit_adxl34x #움직임감지와 LED, 부저와의 연결시에 사용
import Adafruit_ADXL345 #기울기감지와 서보모터와의 연동시에 사용

PIN_LED = 19 #LED 핀
BUZZER_PIN = 13 #부저 핀
pin = 26 #서보모터 핀
GPIO.setmode(GPIO.BCM) #LED, 부저, 서보모터 설정 (11~14번 줄)
GPIO.setup(PIN_LED, GPIO.OUT)
GPIO.setup(BUZZER_PIN, GPIO.OUT)
GPIO.setup(pin, GPIO.OUT) 

accel = Adafruit_ADXL345.ADXL345() #자이로센서의 3축(x, y, z) 값을 불러옴

pwm = GPIO.PWM(BUZZER_PIN, 262) 
p = GPIO.PWM(pin, 50)
p.start(6)

i2c = busio.I2C(board.SCL, board.SDA) #자이로센서 기본설정 (22~24번 줄)
accelerometer = adafruit_adxl34x.ADXL345(i2c) 
accelerometer.enable_motion_detection(threshold=18) 

try:
    while True:
        x, y, z = accel.read() #자이로센서값을 매번 받아옴(변수는 y만 사용하지만, y를 받기 위해 x, z 변수 생성)
        if y < -250 : #y축 각도별로 서보모터를 회전시켜 수평을 맞춤 (29~64번 줄)
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
        
        if accelerometer.events['motion'] == 1: #움직임을 감지하는 조건문
            GPIO.output(PIN_LED, GPIO.HIGH) #움직임이 감지되면 LED를 켜고 부저를 울림 (67~70번 줄)
            pwm.start(50)
            print("움직임 감지. 수평을 맞추는 중입니다. . .")
            pwm.ChangeFrequency(262)
        else: 
            GPIO.output(PIN_LED, GPIO.LOW) #움직임이 감지되지 않으면 LED와 부저를 끔 (72~74번 줄)
            print("움직임 미감지. 수평상태입니다.")
            pwm.stop()
        time.sleep(0.5) #감지 딜레이 시간(0.1일경우 조금 빠르게 움직임, 0.5 이상으로 느려질경우 감지가 느려짐)
finally: #종료시 모든 장비를 정지함 (76~78번 줄)
    pwm.stop()
    GPIO.cleanup()