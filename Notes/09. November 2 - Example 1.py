


import RPi.GPIO as gpio 
import time 

gpio.setmode(gpio.BCM)
gpio.setup(18, gpio.OUT)

while True: 
	gpio.output(18, gpio.HIGH)
	passcode = input('What is the answer?:')

	if passcode == 'Hola!':
		gpio.output(18, gpio.LOW)
		time.sleep(4)

	else:
		gpio.output(18, gpio.HIGH)
		print('You are wrong!')


