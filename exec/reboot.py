import serial
BAUD_RATE = 57600
DEVICE = '/dev/ttyUSB0'
s = serial.Serial(DEVICE, BAUD_RATE)
print("SYSTEM REBOOTING")
s.write('<REBOOT>>'.encode('utf-8'))
s.close()
exit()
