#include <SoftwareSerial.h>
#define MQ_2 A0
#define BUZZER 6
SoftwareSerial BT(10, 11); // RX, TX

short int LED_PIN = 13;

void setup() {
  pinMode(LED_PIN, OUTPUT);
  digitalWrite(LED_PIN, LOW);
  Serial.begin(9600); // Serial Monitor
  BT.begin(9600); 

}

void send_alert();


void loop() {
  // if (BT.available()) {
  //   char c = BT.read();
  //   Serial.print(c);
  // }
  
  // if (Serial.available()) {
  //   char c = Serial.read();
  //   BT.print(c);
  // }
  short int sensor_value;
  sensor_value = analogRead(MQ_2);
  Serial.print("Sensor Value is: ");
  Serial.print(sensor_value);
  Serial.println("");
  if(sensor_value >= 300){
    send_alert();
    digitalWrite(LED_PIN, HIGH);
    digitalWrite(BUZZER, HIGH);
    delay(5000);
    digitalWrite(BUZZER, LOW);
    digitalWrite(LED_PIN, LOW);
  }
  delay(1000);

}

void send_alert(){
  Serial.print("Gas Level Too High!\n");
  BT.print('1');
  BT.print('\n');
}
