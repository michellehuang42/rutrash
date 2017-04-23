import serial
import glob
import time


ser = serial.Serial('/dev/tty50', 9600, timeout=0)
ser.flushInput()


def recieve():
	while True:
		state = ser.readline()
		if len(state):
			return state


def send(input):
	ser.write(input)
	print 'sent'

