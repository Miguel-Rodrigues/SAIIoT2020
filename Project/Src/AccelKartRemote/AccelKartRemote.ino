// ISCTE - IUL
// SAIIoT 2020
// Accelerometer Kart Remote control
// Group 8

#include <WiFi.h>
#include <HTTPClient.h>
#include "Accelerometer.h"

void setup()
{
  Serial.begin(115200);
  while (!Serial);

  Serial.println("== Program Start ==");

  initializeSensor();

  Serial.println("Load completed!");
}

void loop()
{
  sensorData* data = getSensorData();

  Serial.println();

  delay(500);
}