import serial
import time
ser = serial.Serial("/dev/ttyUSB0",baudrate=9600)
idx = 0
while True:
    ser.write(str(idx))
    print(idx)
    ser.write("\r\n")
    time.sleep(1)
    idx = idx + 1
