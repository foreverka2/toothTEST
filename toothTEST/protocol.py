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
                tempdata1 = temp2
                tempdata2 = blueSerial.readline()
                tempdata3 = blueSerial.readline()
                tempdata4 = blueSerial.readline()
                print("Sensor data 1 is : " + tempdata1)
                print("Sensor data 2 is : " + tempdata2)
                print("Sensor data 3 is : " + tempdata3)
                print("Sensor data 4 is : " + tempdata4)
                data1 = int(tempdata1)
                data2 = int(tempdata2)
                data3 = int(tempdata3)
                data4 = int(tempdata4)
            else :
                return -1, -1, -1, -1
        else :
            return -1, -1, -1, -1
    else :
        return -1, -1, -1, -1
    return data1, data2, data3, data4

def GoSignal():
    blueSerial.write(str.encode('#1'))

