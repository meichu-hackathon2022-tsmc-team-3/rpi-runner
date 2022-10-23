import RPi.GPIO as GPIO
import time
from mfrc522 import SimpleMFRC522

from socket import socket, AF_INET, SOCK_DGRAM
from server import blink
from server.music import playMusic

def getImgResult(id):

	HOST = '192.168.162.189'
	PORT = 8026
	server_addr = (HOST, PORT)

	s = socket(AF_INET, SOCK_DGRAM)

	s.sendto(id.encode(), server_addr)

	indata, addr = s.recvfrom(1024)

	if b'not' in indata:
		return "NOT PASS"

	return "PASS"

reader = SimpleMFRC522()

try:
	while True:
		id,res = reader.read()
		print(f"READ: {hex(id) = }")
		result = getImgResult(hex(id))
		print(f"RESULT: {result = }")
		
		blink.blink(result)

		if result == "NOT PASS":
			playMusic()
		time.sleep(2)

		blink.clearup()

finally:
	GPIO.cleanup()

