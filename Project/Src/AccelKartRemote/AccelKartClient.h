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

void initializeWiFi(char const * ssid, char const * password, char const * address);
int moveKart(sensorData *data);

#endif