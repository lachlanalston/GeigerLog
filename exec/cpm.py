import serial

BAUD_RATE = 57600
DEVICE = '/dev/ttyUSB0'

s = serial.Serial(DEVICE, BAUD_RATE)

s.write('<GETCPM>>'.encode('utf-8'))
version = s.read(2)
cpm = version[1]
print(cpm)

s.close()
exit()
