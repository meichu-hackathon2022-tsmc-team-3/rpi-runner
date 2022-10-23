#!/usr/local/bin/python
import time
import RPi.GPIO as GPIO

A = 880
B = 988
C = 1108 
D = 1174
E = 1318
F = 1567


def playMusic():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(16, GPIO.OUT)
    p = GPIO.PWM(16, 50)
    p.start(50)
    time.sleep(1)

    p.ChangeFrequency(A)
    time.sleep(.75)

    p.ChangeFrequency(B)
    time.sleep(1.25)
   
    p.ChangeFrequency(C)
    time.sleep(.75)

    p.ChangeFrequency(D)
    time.sleep(1)

    p.ChangeFrequency(E)
    time.sleep(.24)

    p.ChangeFrequency(20)
    time.sleep(.01)

    p.ChangeFrequency(E)
    time.sleep(.25)

    p.ChangeFrequency(F)
    time.sleep(1.5)

    p.stop()
    GPIO.cleanup()
