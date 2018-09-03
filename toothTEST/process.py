import protocol
import httplib, urllib
import time
key = 'SVJ8DR6KDI9QPEBO'

def Cloud():
    protocol.GoSignal()
    time.sleep(1)
    while True:
        data1, data2, data3, data4 = protocol.GetData()
        if data1 == -1 :
            print('ready for booting...')
            break
        params1 = urllib.urlencode({'field1': data1, 'key' : key})
        params2 = urllib.urlencode({'field2': data2, 'key' : key})
        params3 = urllib.urlencode({'field3': data3, 'key' : key})
        params4 = urllib.urlencode({'field4': data4, 'key' : key})
        headers = {"Content-typZZe": "application/x-www-form-urlencoded","Accept": "text/plain"}
        conn = httplib.HTTPConnection("api.thingspeak.com:80")
        try:
            conn.request("POST", "/update", params1, headers)
            conn.request("POST", "/update", params2, headers)
            conn.request("POST", "/update", params3, headers)
            conn.request("POST", "/update", params4, headers)
            response = conn.getresponse()
            data = response.read()
            conn.close()
        except:
            print "connection failed"
        break



