#! /usr/bin/python
 
import serial
from time import sleep 

blueSerial = serial.Serial( "/dev/rfcomm1", 9600 )
 

def GetData():
    if blueSerial.readable() :
        temp = blueSerial.readline()
        if temp == b'G\r\n':
            temp2 = blueSerial.readline()
            if temp2 != b'G\r\n':
                data1 = int(temp2)
                data2 = int(blueSerial.readline())
                data3 = int(blueSerial.readline())
                data4 = int(blueSerial.readline())
                print(data1)
                print(data2)
                print(data3)
                print(data4)
            else :
                return -1, -1, -1, -1
        else :
            return -1, -1, -1, -1
    else :
        return -1, -1, -1, -1
    return data1, data2, data3, data4

def GoSignal():
    blueSerial.write(str.encode('#1'))

