import serial

BAUD_RATE = 57600
DEVICE = '/dev/ttyUSB0'

s = serial.Serial(DEVICE, BAUD_RATE)

s.write('<GETTEMP>>'.encode('utf-8'))
version = s.read(4)
temp = float(version[0] + (version[1]/10))
print(temp)
	
s.close()
exit()
