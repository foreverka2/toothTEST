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


void setup() {
  Serial.begin(115200);
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
  
  Serial.print("tested ohm No.1 ");
  Serial.print(res0,3);
  Serial.println(" ohm.");
  Serial.print("tested ohm No.1 ");
  Serial.print(res0/1000,3);
  Serial.println(" kohm.");
  Serial.println("");

  delay(500);
  
  Serial.print("tested ohm No.2 ");
  Serial.print(res1,3);
  Serial.println(" ohm.");
  Serial.print("tested ohm No.2 ");
  Serial.print(res1/1000,3);
  Serial.println(" kohm.");
  Serial.println("");

  delay(500);

  Serial.print("tested ohm No.3 ");
  Serial.print(res2,3);
  Serial.println(" ohm.");
  Serial.print("tested ohm No.3 ");
  Serial.print(res2/1000,3);
  Serial.println(" kohm.");
  Serial.println("");
  
  delay(500);

  Serial.print("tested ohm No.4 ");
  Serial.print(res3,3);
  Serial.println(" ohm.");
  Serial.print("tested ohm No.4 ");
  Serial.print(res3/1000,3);
  Serial.println(" kohm.");
  Serial.println("");

  delay(2000);
  
}
