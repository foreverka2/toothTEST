#include <SoftwareSerial.h> //시리얼통신 라이브러리 호출
 
int blueTx=2;   //Tx (보내는핀 설정)at
int blueRx=3;   //Rx (받는핀 설정)
SoftwareSerial mySerial(blueTx, blueRx);  //시리얼 통신을 위한 객체선언
 
void setup() 
{
  Serial.begin(9600);   //시리얼모니터
  mySerial.begin(9600); //블루투스 시리얼
}
void loop()
{
  if (mySerial.available()) {       
    Serial.write(mySerial.read());  //이게 센서값 전송할때 필요한 것
  }
  /*if (Serial.available()) {         
    mySerial.write(Serial.read());  //시리얼 모니터 내용을 블루추스 측에 WRITE
  }*/
}
