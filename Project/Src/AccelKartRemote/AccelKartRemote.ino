// ISCTE - IUL
// SAIIoT 2020
// Accelerometer Kart Remote control
// Group 8

#include "Accelerometer.h"
#include "AccelKartClient.h"

void setup()
{
  Serial.begin(115200);
  while (!Serial);

  Serial.println("== Program Start ==");

  initializeSensor();
  initializeWiFi();

  Serial.println("Load completed!");
}

void loop()
{
  sensorData *data = getSensorData();

  if (moveKart(data) == 0)
  {
    abort();
  }

  Serial.println();

  delay(500);
}