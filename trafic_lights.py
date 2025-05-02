import RPi.GPIO as GPIO
import time
import atexit

@atexit.register
def clean():
    GPIO.output(11, GPIO.LOW)
    GPIO.output(13, GPIO.LOW)
    GPIO.output(15, GPIO.LOW)
    GPIO.cleanup()
GPIO.setmode(GPIO.BOARD)

GPIO.setup(11, GPIO.OUT)
GPIO.setup(13, GPIO.OUT)
GPIO.setup(15, GPIO.OUT)


while True:
    GPIO.output(15, GPIO.HIGH)
    time.sleep(10)
    GPIO.output(15, GPIO.LOW)
    GPIO.output(11, GPIO.HIGH)
    time.sleep(5)
    GPIO.output(11, GPIO.LOW)
    time.sleep(0.7)
    GPIO.output(11, GPIO.HIGH)
    time.sleep(0.7)
    GPIO.output(11, GPIO.LOW)
    time.sleep(0.7)
    GPIO.output(11, GPIO.HIGH)
    time.sleep(0.7)
    GPIO.output(11, GPIO.LOW)
    time.sleep(0.7)
    GPIO.output(11, GPIO.HIGH)
    time.sleep(0.7)
    GPIO.output(11, GPIO.LOW)
    GPIO.output(13, GPIO.HIGH)
    time.sleep(3)
    GPIO.output(13, GPIO.LOW)


