import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
import serial

led = 17
button = 2

GPIO.setup(button, GPIO.IN, GPIO.PUD_UP)

GPIO.setup(led, GPIO.OUT)

while True:
  
  if GPIO.input(button) == True:
     GPIO.output(led, 1)
     time.sleep(0.2)
  if GPIO.input(button) == False:
     GPIO.output(led, 0)
     time.sleep(0.2)

GPIO.cleanup
