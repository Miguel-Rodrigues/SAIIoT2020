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
    char endpoint[100];

    if (WiFi.status() == WL_CONNECTED)
    {
        http.begin(address);
        http.addHeader("Content-Type", "application/json");

        Serial.print("Sending data to '");
        Serial.print(address);
        Serial.println("'...");

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

        if (httpResponseCode > 0) 
        {
            String response = http.getString();
            if(httpResponseCode >= 200 && httpResponseCode < 400)
            {
                Serial.println(httpResponseCode);
                Serial.print(": ");
            }
            else {
                Serial.print("Error on sending POST: ");
                Serial.println(httpResponseCode);
                Serial.print("Message: ");
            }

            Serial.println(response);
        }
        else
        {
            Serial.print("Unknown Error: ");
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