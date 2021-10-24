import serial
BAUD_RATE = 57600
DEVICE = '/dev/ttyUSB0'
s = serial.Serial(DEVICE, BAUD_RATE)
s.write('<GETSERIAL>>'.encode('utf-8'))
serial = s.read(7)
serial = serial.hex()
print(serial)
return serial
s.close()
exit()
