// ================================
// Servo + Ultrasonic Sensor Demo
// Moves servo based on distance
// ================================

#include <Servo.h>

// Servo setup
Servo myServo;
int servoPin = 6;

// Ultrasonic sensor pins
const int trigPin = 9;
const int echoPin = 10;

// Distance reading
long duration;
int distance;

void setup() {
  Serial.begin(9600);
  myServo.attach(servoPin);

  pinMode(trigPin, OUTPUT);
  pinMode(echoPin, INPUT);

  myServo.write(90); // Initial position
}

void loop() {
  // Trigger the sensor
  digitalWrite(trigPin, LOW);
  delayMicroseconds(2);

  digitalWrite(trigPin, HIGH);
  delayMicroseconds(10);
  digitalWrite(trigPin, LOW);

  // Read echo time
  duration = pulseIn(echoPin, HIGH);

  // Calculate distance (cm)
  distance = duration * 0.034 / 2;

  Serial.print("Distance: ");
  Serial.print(distance);
  Serial.println(" cm");

  // Move servo based on distance
  if (distance < 10) {
    myServo.write(0);   // Object close
  } else if (distance < 20) {
    myServo.write(90);  // Mid-range
  } else {
    myServo.write(180); // Object far
  }

  delay(500); // Wait a bit before next check
}
