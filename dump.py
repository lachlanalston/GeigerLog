import serial

BAUD_RATE = 57600
DEVICE = '/dev/ttyUSB0'

def getVersion():
	s.write('<GETVER>>'.encode('utf-8'))
	version = s.read(14)
	return version	

def getCPM():
	s.write('<GETCPM>>'.encode('utf-8'))
	version = s.read(2)
	cpm = version[1]
	print(cpm)
	return cpm

def getTemp():
	s.write('<GETTEMP>>'.encode('utf-8'))
	version = s.read(4)
	temp = float(version[0] + (version[1]/10))
	print(temp)
	return temp

def getSerial():
	s.write('<GETSERIAL>>'.encode('utf-8'))
	serial = s.read(7)
	serial = serial.hex()
	print(serial)
	return serial
	
def rebootUnit():
	print("SYSTEM REBOOTING")
	s.write('<REBOOT>>'.encode('utf-8'))

def powerOff():
	s.write('<POWEROFF>>'.encode('utf-8'))
	
def powerOn():
	s.write('<POWERON>>'.encode('utf-8'))

def getConfig():
	s.write('<GETCFG>>'.encode('utf-8'))
	config = s.read(256)
	print(config)

def factReset():
	s.write('<FACTORYRESET>>'.encode('utf-8'))

s = serial.Serial(DEVICE, BAUD_RATE)
s.close()
exit()
