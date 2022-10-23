import RPi.GPIO as GPIO
import time

GREEN = 40
YELLOW = 38

def blink(res):

	GPIO.setmode(GPIO.BOARD)
	GPIO.setup(GREEN,GPIO.OUT)
	GPIO.setup(YELLOW,GPIO.OUT)

	if res == "PASS":
		GPIO.output(GREEN,0)
		GPIO.output(YELLOW,1)
	else:
		GPIO.output(GREEN,1)
		GPIO.output(YELLOW,0)

def clearup(): 
	
	GPIO.cleanup()

if __name__ == '__main__':
	blink("PASS")	
	blink("NOT PASS")
