// ISCTE - IUL
// SAIIoT 2020
// Accelerometer Kart Remote control
// Group 8

#ifndef __AccelKartClient__H__
#define __AccelKartClient__H__

#include <string.h>
#include <WiFi.h>
#include <HTTPClient.h>
#include "Accelerometer.h"

void initializeWiFi();
int moveKart(sensorData *data);

#endif