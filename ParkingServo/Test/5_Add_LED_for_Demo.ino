#include <Servo.h>
Servo myservo;

int trigPin = 9;
int echoPin = 10;
int ledPin = 13;
int servoPin = 3;
long duration;
int distance;

void setup() {
  myservo.attach(servoPin);
  pinMode(trigPin, OUTPUT);
  pinMode(echoPin, INPUT);
  pinMode(ledPin, OUTPUT);
  myservo.write(0);
}

void loop() {
  digitalWrite(trigPin, LOW);
  delayMicroseconds(2);
  digitalWrite(trigPin, HIGH);
  delayMicroseconds(10);
  digitalWrite(trigPin, LOW);
  duration = pulseIn(echoPin, HIGH);
  distance = duration * 0.034 / 2;

  if (distance < 6) {
    digitalWrite(ledPin, HIGH);
    myservo.write(90);
    delay(3000);
  } else {
    digitalWrite(ledPin, LOW);
    myservo.write(0);
  }

  delay(500);
}
