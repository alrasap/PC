// ============================================================
// Smooth Barrier Control using Ultrasonic Sensor + Servo
// The barrier opens at 6 cm, with smooth servo movement.
// Delay is tuned for safety and responsiveness.
// ============================================================

#include <Servo.h>

// Pins for ultrasonic sensor
const int trigPin = 9;
const int echoPin = 10;

// Pin for servo
const int servoPin = 6;

// Create servo object
Servo barrierServo;

// Variables for distance measurement
long duration;
int distance;

// Current servo position
int currentAngle = 0;  // Start closed
int targetAngle = 0;   // Where we want the servo to go

void setup() {
  Serial.begin(9600);

  pinMode(trigPin, OUTPUT);
  pinMode(echoPin, INPUT);

  barrierServo.attach(servoPin);
  barrierServo.write(currentAngle);  // Set initial position
}

void loop() {
  // --------- Measure Distance ---------
  digitalWrite(trigPin, LOW);
  delayMicroseconds(2);

  digitalWrite(trigPin, HIGH);
  delayMicroseconds(10);
  digitalWrite(trigPin, LOW);

  duration = pulseIn(echoPin, HIGH);
  distance = duration * 0.034 / 2;

  Serial.print("Distance: ");
  Serial.print(distance);
  Serial.println(" cm");

  // --------- Decide Target Position ---------
  if (distance <= 6 && distance > 0) {
    targetAngle = 90;  // Open barrier
    Serial.println("Barrier: OPENING");
  } else {
    targetAngle = 0;   // Close barrier
    Serial.println("Barrier: CLOSING");
  }

  // --------- Smooth Servo Movement ---------
  if (currentAngle != targetAngle) {
    // Move step-by-step toward targetAngle
    if (currentAngle < targetAngle) {
      currentAngle++;
    } else if (currentAngle > targetAngle) {
      currentAngle--;
    }
    barrierServo.write(currentAngle);
    delay(15);  // Delay between servo steps (tweakable)
  } else {
    delay(100); // Short pause when at target
  }
}
