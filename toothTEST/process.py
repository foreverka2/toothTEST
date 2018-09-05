import protocol
import httplib, urllib
import time
key = 'SVJ8DR6KDI9QPEBO'
 
def SetR0():
    protocol.GoSignal()
    time.sleep(0.2)
    R0_data1, R0_data2, R0_data3, R0_data4 = protocol.GetData()
    if R0_data1 == -1 :
        print "ready for set Reference Resistance..."
        print ""
        return -1, -1, -1, -1    
    print("Reference Resistance 1 is : " + str(R0_data1))
    print("Reference Resistance 2 is : " + str(R0_data2))
    print("Reference Resistance 3 is : " + str(R0_data3))
    print("Reference Resistance 4 is : " + str(R0_data4))
    print "All Reference Resistance is set!"
    print ""
    return R0_data1, R0_data2, R0_data3, R0_data4    


def Cloud(R0_data1, R0_data2, R0_data3, R0_data4):
    protocol.GoSignal()
    time.sleep(0.2)
    while True:
        R_data1, R_data2, R_data3, R_data4 = protocol.GetData()
        if R0_data1 == -1 :
            print "Data is jammed. we try to fix it..."
            print ""
            break

        '''Change from resistance to Pascal'''
        data1 = R_data1 - R0_data1 #We can change this equation
        data2 = R_data2 - R0_data2
        data3 = R_data3 - R0_data3
        data4 = R_data4 - R0_data4
        
        '''Filtering Negative data'''
        if data1 < 0 :
            data1 = 0
        if data2 < 0 :
            data2 = 0
        if data3 < 0 :
            data3 = 0
        if data4 < 0 :
            data4 = 0

        print("data 1 is : " + str(data1))
        print("data 2 is : " + str(data2))
        print("data 3 is : " + str(data3))
        print("data 4 is : " + str(data4))
        print "wait for uploading..."
        print ""

        '''Upload data to Cloud server'''
        params1 = urllib.urlencode({'field1': data1, 'key' : key})
        headers1 = {"Content-typZZe": "application/x-www-form-urlencoded","Accept": "text/plain"}
        conn = httplib.HTTPConnection("api.thingspeak.com:80")
        try:
            conn.request("POST", "/update", params1, headers1)
            response = conn.getresponse()
            data = response.read()
            conn.close()
        except:
            print "connection failed"


        params2 = urllib.urlencode({'field2': data2, 'key' : key})
        headers2 = {"Content-typZZe": "application/x-www-form-urlencoded","Accept": "text/plain"}
        conn = httplib.HTTPConnection("api.thingspeak.com:80")
        try:
            conn.request("POST", "/update", params2, headers2)
            response = conn.getresponse()
            data = response.read()
            conn.close()
        except:
            print "connection failed"


        params3 = urllib.urlencode({'field3': data3, 'key' : key})
        headers3 = {"Content-typZZe": "application/x-www-form-urlencoded","Accept": "text/plain"}
        conn = httplib.HTTPConnection("api.thingspeak.com:80")
        try:
            conn.request("POST", "/update", params3, headers3)
            response = conn.getresponse()
            data = response.read()
            conn.close()
        except:
            print "connection failed"


        params4 = urllib.urlencode({'field4': data4, 'key' : key})
        headers4 = {"Content-typZZe": "application/x-www-form-urlencoded","Accept": "text/plain"}
        conn = httplib.HTTPConnection("api.thingspeak.com:80")
        try:
            conn.request("POST", "/update", params4, headers4)
            response = conn.getresponse()
            data = response.read()
            conn.close()
        except:
            print "connection failed"
        print "All data is uploaded to cloud server!"
        print ""
        break



