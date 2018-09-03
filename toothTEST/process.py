import protocol
import httplib, urllib
import time
key = 'SVJ8DR6KDI9QPEBO'

def Cloud():
    protocol.GoSignal()
    time.sleep(0.2)
    while True:
        data1, data2, data3, data4 = protocol.GetData()
        if data1 == -1 :
            print "wait for proper data..."
            print ""
            break
        print "wait for uploading..."
        print ""
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



