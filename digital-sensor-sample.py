import RPi.GPIO as GPIO
import time
import atexit

@atexit.register
def clean():
    GPIO.output(11, GPIO.LOW)
    GPIO.cleanup()
GPIO.setmode(GPIO.BOARD)

GPIO.setup(11, GPIO.OUT)
GPIO.setup(8, GPIO.IN)

while True:
    if GPIO.input(8):
        GPIO.output(11, 1)
    else:
        GPIO.output(11, 0)
