#include <Servo.h>
Servo myservo;

int trigPin = 9;
int echoPin = 10;
int servoPin = 3;
long duration;
int distance;

void setup() {
  myservo.attach(servoPin);
  pinMode(trigPin, OUTPUT);
  pinMode(echoPin, INPUT);
  myservo.write(0);
  Serial.begin(9600);
}

void loop() {
  int total = 0;
  for (int i = 0; i < 3; i++) {
    digitalWrite(trigPin, LOW);
    delayMicroseconds(2);
    digitalWrite(trigPin, HIGH);
    delayMicroseconds(10);
    digitalWrite(trigPin, LOW);
    duration = pulseIn(echoPin, HIGH);
    total += duration * 0.034 / 2;
    delay(100);
  }

  distance = total / 3;

  Serial.print("Avg Distance: ");
  Serial.println(distance);

  if (distance < 6) {
    myservo.write(90);
    delay(3000);
  } else {
    myservo.write(0);
  }

  delay(500);
}
