import serial
BAUD_RATE = 57600
DEVICE = '/dev/ttyUSB0'
s = serial.Serial(DEVICE, BAUD_RATE)
s.write('<GETVER>>'.encode('utf-8'))
version = s.read(14)
print(version)
return version
s.close()
exit()
