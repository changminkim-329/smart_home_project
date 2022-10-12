/*
HC-06 bluetooth
http://www.devicemart.co.kr/
*/

#include <ArduinoJson.h>


#include <SoftwareSerial.h> // 0,1번핀 제외하고 Serial 통신을 하기 위해 선언
StaticJsonBuffer<200> jsonBuffer;
JsonObject& root = jsonBuffer.createObject();


// Serial 통신핀으로 D11번핀을 Rx로, D10번핀을 Tx로 선언
SoftwareSerial mySerial(11, 10); // HC-06 TX=11번핀 , RX=10번핀 연결
String myString = "";
int led_pin = 2;
int btn_pin = 7;
int led_state = 1;


void setup()
{
 mySerial.begin(9600); // 통신 속도 9600bps로 블루투스 시리얼 통신 시작
 pinMode(led_pin,OUTPUT);
 pinMode(btn_pin,INPUT);
}

void loop()
{
  String jsondata = "";
  int btn_state = digitalRead(btn_pin);

  if(btn_state){
    if(led_state){
      led_state = 0;
    }
    else{
      led_state = 1;
    }
  }

  while(mySerial.available()){
    char myChar = (char)mySerial.read();
    myString += myChar;
    delay(5);
  }

  if(!myString.equals(""))  //myString 값이 있다면
  {
      if(myString =="ON")  //myString 값이 'on' 이라면
      {
        led_state = 1;
      } 
      
      if(myString == "OFF"){
        led_state = 0;  //LED OFF
      }
      
    myString="";  //myString 변수값 초기화
  }
  
  root["led_state"] = led_state;


  digitalWrite(led_pin,led_state);

  root.printTo(jsondata);
  char ch[jsondata.length()+1] = {0};
  jsondata.toCharArray(ch,sizeof(ch)+1);
  mySerial.write(ch);

  delay(1000);

}
