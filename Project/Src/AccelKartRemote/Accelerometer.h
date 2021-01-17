// ISCTE - IUL
// SAIIoT 2020
// Accelerometer Kart Remote control
// Group 8

#ifndef __Accelerometer__H__
#define __Accelerometer__H__

#include <Wire.h>
#include <SPI.h>
#include <SparkFunLSM9DS1.h>

// Earth's magnetic field varies by location. Add or subtract
// a declination to get a more accurate heading. Calculate
// your's here:
// http://www.ngdc.noaa.gov/geomag-web/#declination
//TODO: Review...
#define DECLINATION -8.58 // Declination (degrees) in Boulder, CO.

#define LSM9DS1_M 0x1E
#define LSM9DS1_AG 0x6B
#define SDA_1 21 //8
#define SCL_1 22 //9
#define BUTTON_1 32
#define BUTTON_2 33

LSM9DS1 imu;

typedef struct point3d
{
  float x;
  float y;
  float z;
  point3d(float x_, float y_, float z_)
  {
    x = x_;
    y = y_;
    z = z_;
  }
  point3d()
  {
    x = 0;
    y = 0;
    z = 0;
  }
} point3d;

typedef struct sensorData
{
  point3d gyro;
  point3d accel;
  point3d compass;
  float pitch;
  float roll;
  float heading;

  bool button1;
  bool button2;

  sensorData() {
    pitch = 0;
    roll = 0;
    heading = 0;
  }
} sensorData;

//Function definitions
void getGyro(sensorData *sensorData);
void getAccel(sensorData *sensorData);
void getMag(sensorData *sensorData);
void getAttitude(sensorData *sensorData);
void getButtons(sensorData *sensorData);

void initializeSensor();
sensorData* getSensorData();

#endif