// ISCTE - IUL
// SAIIoT 2020
// Accelerometer Kart Remote control
// Group 8

#include "Accelerometer.h"
#include "AccelKartClient.h"

#define deviceName "AccelKartRemote ESP32 9-DOF Smart Sensor"

char const * ssid = "MEO-A76917";
char const * ssidPassword = "CCFA669098";
char const * address = "http://192.168.1.97:8000/AccelKartServer/api/moveKart/";

// char const * ssid = "AccelKartNetwork";
// char const * ssidPassword = "arb6lvfc";
// char const * address = "http://192.168.1.78:8000/AccelKartServer/api/moveKart/";

void setup()
{
    Serial.begin(115200);
    while (!Serial);

    Serial.println("== Program Start ==");

    initializeSensor(deviceName);
    initializeWiFi(ssid, ssidPassword, address);

    Serial.println("Load completed!");
}

void loop()
{
    sensorData *data = getSensorData();

    // Reboots board if WiFi connection has lost.
    if (moveKart(data) == 0)
    {
        abort();
    }

    Serial.println();

    delay(500);
}
