#include <doxygen.h>
#include <ESP8266.h>
#include <SoftwareSerial.h>

#define SSID        "HYWLAN"
#define PASSWORD    "12345678"
#define HOST_NAME   "192.168.0.118"
#define HOST_PORT   (5555)
#define source_volt 5.0
#define Rref 1000.0

int testinput0 = A0;
int testinput1 = A1;
int testinput2 = A2;
int testinput3 = A3;
float current_volt0;
float current_volt1;
float current_volt2;
float current_volt3;
float res0; //측정 저항1
float res1; //측정 저항2
float res2; //측정 저항3
float res3; //측정 저항4

SoftwareSerial mySerial(3, 2); /* RX:D3, TX:D2 */
ESP8266 wifi = ESP8266(mySerial);

void setup(void)
{
    Serial.begin(9600); // 비트레이트 꼭 맞추자
    Serial.print("setup begin\r\n");
      
    if (wifi.setOprToStationSoftAP()) {
        Serial.print("to station + softap ok\r\n");
    } else {
        Serial.print("to station + softap err\r\n");
    }
 
    if (wifi.joinAP(SSID, PASSWORD)) {
        Serial.print("Join AP success\r\n");
        Serial.print("IP:");
        Serial.println( wifi.getLocalIP().c_str());       
    } else {
        Serial.print("Join AP failure\r\n");
    }
    
    if (wifi.disableMUX()) {
        Serial.print("single ok\r\n");
    } else {
        Serial.print("single err\r\n");
    }
    
    Serial.print("setup end\r\n");
}
 
void loop(void)
{
  current_volt0 = GetRes(testinput0);
  current_volt1 = GetRes(testinput1);
  current_volt2 = GetRes(testinput2);
  current_volt3 = GetRes(testinput3);

  res0 = Rref * ((current_volt0-current_volt1)/(source_volt-current_volt0));
  res1 = Rref * ((current_volt1-current_volt2)/(source_volt-current_volt0));
  res2 = Rref * ((current_volt2-current_volt3)/(source_volt-current_volt0));
  res3 = Rref * ((current_volt3)/(source_volt-current_volt0));

  uint8_t buffer[128] = {0};
    
  if (wifi.createTCP(HOST_NAME, HOST_PORT)) 
  {
      Serial.print("create tcp ok\r\n");
  } 
  else 
  {
      Serial.print("create tcp err\r\n");
  }
  String data0 = String.valueOf(res0);
  String data1 = String.valueof(res1);
  String data2 = String.valueof(res2);
  String data3 = String.valueof(res3);
  
  char *SenseData = data0 + data1 + data2 + data3 ; //이게 되나?
  wifi.send((const uint8_t*)SenseData, strlen(SenseData));
    
  uint32_t len = wifi.recv(buffer, sizeof(buffer), 10000); //10초 기다리기 줄여도됨
  if (len > 0) 
  {
      Serial.print("Received:[");
      for(uint32_t i = 0; i < len; i++) 
      {
          Serial.print((char)buffer[i]);
      }
      Serial.print("]\r\n");
  }
    
  if (wifi.releaseTCP()) 
  {
      Serial.print("release tcp ok\r\n");
  } 
  else
  {
      Serial.print("release tcp err\r\n");
  }
  delay(500); // 딜레이조절
}
