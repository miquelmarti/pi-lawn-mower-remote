# -*- coding: utf-8 -*-
import RPi.GPIO as GPIO

class RemoteGPIO:
	def __init__(self):
		GPIO.setmode(GPIO.BCM)

		GPIO.setup(19, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
		GPIO.setup(26, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
		GPIO.setup(16, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
		GPIO.setup(20, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)

		GPIO.add_event_detect(19, GPIO.BOTH, callback=self.key_pressed, bouncetime=100)
		GPIO.add_event_detect(26, GPIO.BOTH, callback=self.key_pressed, bouncetime=100)
		GPIO.add_event_detect(16, GPIO.BOTH, callback=self.key_pressed, bouncetime=100)
		GPIO.add_event_detect(20, GPIO.BOTH, callback=self.key_pressed, bouncetime=100)

		self.state='s'

	def key_pressed(self,channel):
		self.state='s'
		if GPIO.input(16):
			self.state='w'
		elif GPIO.input(20):
			self.state='x'
		if GPIO.input(19) and self.state=='s':
			self.state='d'
		elif GPIO.input(19) and self.state=='w':
			self.state='e'
		elif GPIO.input(19) and self.state=='x':
			self.state='c'
		elif GPIO.input(26) and self.state=='s':
			self.state='a'
		elif GPIO.input(26) and self.state=='w':
			self.state='q'
		elif GPIO.input(26) and self.state=='x':
			self.state='z'
		
		print self.state

	def exit(self):	
		GPIO.cleanup()
