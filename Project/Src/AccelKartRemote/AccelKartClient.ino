// ISCTE - IUL
// SAIIoT 2020
// Accelerometer Kart Remote control
// Group 8

#include "AccelKartClient.h"

char const * ssid = "Viniltejo";
char const * ssidPassword = "arb6lvfc";
String address = "http://192.168.1.77:8081/";
const char* moveKartTemplate = "{\"name\":\"%s\",\"gyro\":{\"x\":%f,\"y\":%f,\"z\":%f},\"accel\":{\"x\":%f,\"y\":%f,\"z\":%f},\"compass\":{\"x\":%f,\"y\":%f,\"z\":%f},\"pitch\":%f,\"roll\":%f,\"heading\":%f,\"button1\":%s,\"button2\":%s}";

void initializeWiFi()
{
    Serial.println("Initializing WiFi card...");

    WiFi.begin(ssid, ssidPassword);

    while (WiFi.status() != WL_CONNECTED)
    {
        delay(1000);
        Serial.println("Connecting to WiFi...");
    }

    Serial.println("Connected to the WiFi network.");
}

int moveKart(sensorData *data)
{
    String call = "MoveKart";
    HTTPClient http;
    int httpResponseCode = 0;

    if (WiFi.status() == WL_CONNECTED)
    {
        http.begin(address + call);
        http.addHeader("Content-Type", "application/json");

        Serial.println("Sending data...");

        //Serializing data
        char payload[300];
        sprintf(payload, moveKartTemplate, "ESP32_9DOF_Sensor",
            data->gyro.x, data->gyro.y, data->gyro.z,
            data->accel.x, data->accel.y, data->accel.z,
            data->compass.x, data->compass.y, data->compass.z,
            data->pitch, data->roll, data->heading,
            data->button1 ? "true" : "false",
            data->button2 ? "true" : "false");

        httpResponseCode = http.POST(String(payload));

        if (httpResponseCode == 200)
        {
            String response = http.getString();
            Serial.println(httpResponseCode);
            Serial.println(response);
        }
        else
        {
            Serial.println("Error on sending POST:");
            Serial.println(httpResponseCode);
        }

        http.end();
    }
    else
    {
        Serial.println("Error in WiFi connection");
    }

    return httpResponseCode;
}