 float GetRes(int TestInput){
  
  long reading = 0;
  float current_volt;
  
  for( int i = 0 ; i < 10 ; i++) // 10번 평균 값으로 계산하여 본다. , 3번은 정확한 값이 나오지않았다!
  {
    reading+=analogRead(TestInput);
  }
  
  reading = trunc((reading)/10);
  current_volt = (source_volt/1023.0)*reading;

  return current_volt;
 }
