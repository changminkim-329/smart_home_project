/*
HC-06 bluetooth
http://www.devicemart.co.kr/
*/


#include <SoftwareSerial.h> // 0,1번핀 제외하고 Serial 통신을 하기 위해 선언

// Serial 통신핀으로 D11번핀을 Rx로, D10번핀을 Tx로 선언
SoftwareSerial mySerial(10, 11); // HC-06 TX=11번핀 , RX=10번핀 연결
String myString = "";
int pin = 2;
void setup()
{
 Serial.begin(9600); // 통신 속도 9600bps로 PC와 시리얼 통신 시작
 mySerial.begin(9600); // 통신 속도 9600bps로 블루투스 시리얼 통신 시작
 pinMode(pin,OUTPUT);
}

void loop()
{
 // mySerial 핀에 입력이 들어오면, 바이트단위로 읽어서 PC로 출력
 while(mySerial.available()){
  char myChar = (char)mySerial.read();
  myString += myChar;
  delay(5);
 }

  if(!myString.equals(""))  //myString 값이 있다면
  {
    Serial.println("input value: "+myString); //시리얼모니터에 myString값 출력
 
      if(myString =="ON")  //myString 값이 'on' 이라면
      {
        digitalWrite(pin, HIGH); //LED ON
      } else
      
      if(myString == "OFF"){
        digitalWrite(pin, LOW);  //LED OFF
      }
      
    myString="";  //myString 변수값 초기화
  }
 
  // Serial 핀에 입력이 들어오면, 바이트단위로 읽어서 블루투스로 출력
 if (Serial.available()){
   mySerial.write(Serial.read());
   
 }
 
}
