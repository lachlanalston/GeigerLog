import serial
BAUD_RATE = 57600
DEVICE = '/dev/ttyUSB0'
s = serial.Serial(DEVICE, BAUD_RATE)
s.write('<GETCFG>>'.encode('utf-8'))
config = s.read(256)
print(config)
s.close()
exit()
