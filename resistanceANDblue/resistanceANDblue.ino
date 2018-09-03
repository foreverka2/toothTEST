#include <SoftwareSerial.h>

#define RxPIN 2
#define TxPIN 3 
#define source_volt 5.0
#define Rref 1000.0

int MasterSignal = 0;

int testinput0 = A0;
int testinput1 = A1;
int testinput2 = A2;
int testinput3 = A3;
float current_volt0;
float current_volt1;
float current_volt2;
float current_volt3;
int res0; //측정 저항1
int res1; //측정 저항2
int res2; //측정 저항3
int res3; //측정 저항4

SoftwareSerial mySerial(RxPIN, TxPIN);
byte buffer[1024];
int bufferPosition;

void setup() {
  Serial.begin(9600);
  mySerial.begin(9600);
  bufferPosition = 0;
}

void loop() {
  
  current_volt0 = GetRes(testinput0);
  current_volt1 = GetRes(testinput1);
  current_volt2 = GetRes(testinput2);
  current_volt3 = GetRes(testinput3);

  res0 = Rref * ((current_volt0-current_volt1)/(source_volt-current_volt0));
  res1 = Rref * ((current_volt1-current_volt2)/(source_volt-current_volt0));
  res2 = Rref * ((current_volt2-current_volt3)/(source_volt-current_volt0));
  res3 = Rref * ((current_volt3)/(source_volt-current_volt0));

  String data0 = String(res0);
  String data1 = String(res1);
  String data2 = String(res2);
  String data3 = String(res3);
  
  mySerial.println('G'); // Slave인 아두이노에서 Master로 준비완료 신호 전송
  delay(100);
  MasterSignal = get_data(); // Master로부터 동작신호 수신

  if(MasterSignal == 1) // Master로부터 동작을 허락받은 경우
  {
    /*블루투스 센서값 송신*/
    mySerial.println(data0);
    mySerial.println(data1);
    mySerial.println(data2);
    mySerial.println(data3);
    MasterSignal = 0; // MasterSignal 초기화
  }

}


 int get_data(){
  int num;
  while(true) 
  {
    if(mySerial.available())
    {
      if(mySerial.find('#'))
      {
        num = mySerial.parseInt();
      }
      else
        continue;
      return num;
    }
    else
      continue;
  }
}
