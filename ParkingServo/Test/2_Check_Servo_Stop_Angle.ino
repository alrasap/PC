#include <Servo.h>
Servo myservo;

void setup() {
  myservo.attach(3);
  Serial.begin(9600);
  Serial.println("Testing servo angles...");
}

void loop() {
  myservo.write(0);
  delay(2000);
  myservo.write(90);
  delay(2000);
  myservo.write(180);
  delay(2000);
}
