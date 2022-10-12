#include <SoftwareSerial.h>

#include <ArduinoJson.h>


#include <DHT11.h>  //아두이노 온습도센서 DHT11을 사용하기위해 위에서 설치해두었던 라이브러리를 불러옵니다.

DHT11 dht11(A0);  /*불러온 라이브러리 안에 몇번 PIN에서 데이터값이 나오는지
                     설정해줘야 합니다. 아날로그 0번 PIN인 A0으로 설정했습니다.
                     */

SoftwareSerial mySerial(11, 10); // HC-06 TX=11번핀 , RX=10번핀 연결

StaticJsonBuffer<200> jsonBuffer;
JsonObject& root = jsonBuffer.createObject();

int ledpin = 7;

void setup()
{
  mySerial.begin(9600); // 통신 속도 9600bps로 블루투스 시리얼 통신 시작
  pinMode(ledpin,OUTPUT);
}


void loop()
{
  String jsondata = "";

  digitalWrite(ledpin,LOW);
  
  float temp, humi; /*온도와 습도 값이 저장될 변수를 만들어줍니다. 온습도값이 
                      소수점이기때문에 float변수를 사용했습니다.
                    */    
  int result = dht11.read(humi, temp); /* DHT.h 함수안에 dht11이라는 메소드를 사용해서
                                             현재 온습도 값을 자동으로 계산해줍니다.
                                             계산후 현재 온습도가 데이터가 나오는지 아닌지
                                             판단한 리턴값을 result 변수에 저장해줍니다.
                                             dht11메소드 에서는 온습도가 잘 감지되면 0이라는 
                                             리턴값을 보내줍니다.
                                          */


  if (result == 0)  /* 온습도가 잘측정이되서 result변수에 0이라는 값이 들어오면 
                       if문이 실행됩니다.
                    */ 
  {
    root["tempvalue"] = temp;
    root["humivalue"] = humi;

    root.printTo(jsondata);

    char ch[jsondata.length()+1] = {0};

    

    jsondata.toCharArray(ch,sizeof(ch)+1);

    mySerial.write(ch);

    digitalWrite(ledpin,HIGH);
    
  }
  
  
  delay(1000); 
  /* 
  일반적인 딜레이 값이 아니라 DHT11에서 권장하는
  딜레이함수를 사용해줘야 정상적인 값이 나옵니다. 옆에는 DHT11 라이브러리안에
  미리 설정되어있는 딜레이시간을 적용시킨 모습 입니다.
  */
                                  
}
