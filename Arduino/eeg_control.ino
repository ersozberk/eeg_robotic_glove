#include <SoftwareSerial.h>

SoftwareSerial BTSerial(10, 11); // RX | TX

const int pumpPin = 8;

void setup() {
  pinMode(pumpPin, OUTPUT);
  BTSerial.begin(9600);
  Serial.begin(9600);
}

void loop() {
  if (BTSerial.available()) {
    char command = BTSerial.read();
    if (command == '1') {
      digitalWrite(pumpPin, HIGH); // Hava pompala
      Serial.println("Pump On");
    } else if (command == '0') {
      digitalWrite(pumpPin, LOW); // Hava pompalamayı durdur
      Serial.println("Pump Off");
    }
  }
}
