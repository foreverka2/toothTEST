#! /usr/bin/python
 
import serial
from time import sleep 

blueSerial = serial.Serial( "/dev/rfcomm0", 9600 )
 

while True:
    try:
        if blueSerial.readable() :
            print(blueSerial.readline())
            if blueSerial.readline() == 'Sensor data is ready\r\n':
                data1 = int(blueSerial.readline())
                data2 = int(blueSerial.readline())
                data3 = int(blueSerial.readline())
                data4 = int(blueSerial.readline())
    except:
        break
 
 
