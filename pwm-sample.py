import RPi.GPIO as GPIO
import time
import atexit

@atexit.register
def clean():
    GPIO.cleanup()
GPIO.setmode(GPIO.BOARD)

GPIO.setup(11, GPIO.OUT)
pwm = GPIO.PWM(11, 100)
pwm.start(0)
dt = 0

while True:
    while dt < 100:
        time.sleep(0.01)
        dt = dt + 1
        print(dt)
        pwm.ChangeDutyCycle(dt)
    while dt > 0:
        time.sleep(0.01)
        dt = dt - 1
        print(dt)
        pwm.ChangeDutyCycle(dt)
