import RPi.GPIO as gpio

gpio.setmode(gpio.BCM)

gpio.setup(18, gpio.OUT)
gpio.setup(19, gpio.IN, pull_up_down=gpio.PUD_DOWN)

while True:
	if gpio.input(19) == gpio.HIGH:
		print('button was pushed!')
		gpio.output(18, gpio.HIGH)

	else: 
		gpio.output(18, gpio.LOW)
