// ISCTE - IUL
// SAIIoT 2020
// Accelerometer Kart Remote control
// Group 8

#include "AccelKartClient.h"

const char* moveKartTemplate = "{"
    "\"name\":\"%s\","
    "\"gyro\":{\"x\":%f,\"y\":%f,\"z\":%f},"
    "\"accel\":{\"x\":%f,\"y\":%f,\"z\":%f},"
    "\"compass\":{\"x\":%f,\"y\":%f,\"z\":%f},"
    "\"pitch\":%f,\"roll\":%f,\"heading\":%f,"
    "\"button1\":%s,\"button2\":%s"
"}";

void initializeWiFi(char const * ssid, char const * password, char const * address)
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
    HTTPClient http;
    int httpResponseCode = 0;
    const char* const call = "api/moveKart/";
    char endpoint[100];

    if (WiFi.status() == WL_CONNECTED)
    {
        strcpy(endpoint, address);
        strcat(endpoint, call);

        http.begin(endpoint);
        http.addHeader("Content-Type", "application/json");

        Serial.println("Sending data...");

        //Serializing data
        char payload[300];
        sprintf(payload, moveKartTemplate, data->name,
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
            Serial.print(httpResponseCode);
            Serial.print(": ");
            Serial.println(response);
        }
        else
        {
            Serial.print("Error on sending POST: ");
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