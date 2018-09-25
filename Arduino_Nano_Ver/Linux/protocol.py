#! /usr/bin/python

import serial
from time import sleep 

blueSerial = serial.Serial( "/dev/rfcomm0", 9600 )

def GetData():
    if blueSerial.readable() :
        temp = blueSerial.readline()
        if temp == b'G\r\n':
            temp2 = blueSerial.readline()
            if temp2 != b'G\r\n':
                R1 = int(temp2)
                R2 = int(blueSerial.readline())
                R3 = int(blueSerial.readline())
                R4 = int(blueSerial.readline())
            else :
                return -1, -1, -1, -1
        else :
            return -1, -1, -1, -1
    else :
        return -1, -1, -1, -1
    return R1, R2, R3, R4

def GoSignal():
    blueSerial.write(str.encode('#1'))

