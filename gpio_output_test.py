import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setup(31, GPIO.OUT)

while True :
    GPIO.output(31, GPIO.HIGH)
    time.sleep(0.5)
    GPIO.output(31, GPIO.LOW)
    time.sleep(0.5)