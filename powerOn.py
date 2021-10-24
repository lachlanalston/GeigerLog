import serial
BAUD_RATE = 57600
DEVICE = '/dev/ttyUSB0'
s = serial.Serial(DEVICE, BAUD_RATE)
s.write('<POWERON>>'.encode('utf-8'))
s.close()
exit()
