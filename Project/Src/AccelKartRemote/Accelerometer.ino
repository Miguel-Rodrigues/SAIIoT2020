// ISCTE - IUL
// SAIIoT 2020
// Accelerometer Kart Remote control
// Group 8

#include "Accelerometer.h"

void getGyro(sensorData *sensorData)
{
    // Now we can use the gx, gy, and gz variables as we please.
    // Either print them as raw ADC values, or calculated in DPS.
    Serial.print("Gyro: ");
    sensorData->gyro = point3d(
        imu.calcGyro(imu.gx),
        imu.calcGyro(imu.gy),
        imu.calcGyro(imu.gz));

    Serial.print(sensorData->gyro.x, 2);
    Serial.print(", ");
    Serial.print(sensorData->gyro.y, 2);
    Serial.print(", ");
    Serial.print(sensorData->gyro.z, 2);
    Serial.println(" deg/s");
}

void getAccel(sensorData *sensorData)
{
    // Now we can use the ax, ay, and az variables as we please.
    // Either print them as raw ADC values, or calculated in g's.
    Serial.print("Accel: ");
    sensorData->accel = point3d(
        imu.calcAccel(imu.ax),
        imu.calcAccel(imu.ay),
        imu.calcAccel(imu.az));

    Serial.print(sensorData->accel.x, 2);
    Serial.print(", ");
    Serial.print(sensorData->accel.y, 2);
    Serial.print(", ");
    Serial.print(sensorData->accel.z, 2);
    Serial.println(" g");
}

void getMag(sensorData *sensorData)
{
    // Now we can use the mx, my, and mz variables as we please.
    // Either print them as raw ADC values, or calculated in Gauss.
    Serial.print("Compass: ");
    sensorData->compass = point3d(
        imu.calcMag(imu.mx),
        imu.calcMag(imu.my),
        imu.calcMag(imu.mz));

    Serial.print(sensorData->compass.x, 2);
    Serial.print(", ");
    Serial.print(sensorData->compass.y, 2);
    Serial.print(", ");
    Serial.print(sensorData->compass.z, 2);
    Serial.println(" gauss");
}

// Calculate pitch, roll, and heading.
// Pitch/roll calculations take from this app note:
// http://cache.freescale.com/files/sensors/doc/app_note/AN3461.pdf?fpsp=1
// Heading calculations taken from this app note:
// http://www51.honeywell.com/aero/common/documents/myaerospacecatalog-documents/Defense_Brochures-documents/Magnetic__Literature_Application_notes-documents/AN203_Compass_Heading_Using_Magnetometers.pdf
void getAttitude(sensorData *sensorData)
{
    float ax = sensorData->accel.x;
    float ay = sensorData->accel.y;
    float az = sensorData->accel.z;
    float my = -sensorData->compass.y;
    float mx = -sensorData->compass.x;
    float mz = sensorData->compass.z;

    float roll = atan2(ay, az);
    float pitch = atan2(-ax, sqrt(ay * ay + az * az));
    float heading;

    if (my == 0)
        heading = (mx < 0) ? PI : 0;
    else
        heading = atan2(mx, my);

    heading -= DECLINATION * PI / 180;

    if (heading > PI)
        heading -= (2 * PI);
    else if (heading < -PI)
        heading += (2 * PI);

    // Convert everything from radians to degrees:
    heading *= 180.0 / PI;
    pitch *= 180.0 / PI;
    roll *= 180.0 / PI;

    sensorData->heading = heading;
    sensorData->pitch = pitch;
    sensorData->roll = roll;

    Serial.print("Pitch: ");
    Serial.print(pitch, 2);
    Serial.print(", Roll: ");
    Serial.print(roll, 2);
    Serial.print(", Heading: ");
    Serial.println(heading, 2);
}

void getButtons(sensorData *sensorData)
{
    sensorData->button1 = digitalRead(BUTTON_1);
    sensorData->button2 = digitalRead(BUTTON_2);
    Serial.print("Button 1: ");
    Serial.print(sensorData->button1);
    Serial.print(", Button 2: ");
    Serial.println(sensorData->button2);
}

char const *sensorName;
void initializeSensor(char const *sensorName_)
{
    pinMode(SDA_1, INPUT_PULLUP);
    pinMode(SCL_1, INPUT_PULLUP);

    pinMode(BUTTON_1, INPUT);
    pinMode(BUTTON_2, INPUT);
    sensorName = sensorName_;

    Serial.println("Initializing I2C channel...");
    if (Wire.begin(SDA_1, SCL_1) == false)
    {
        Serial.println("Failed to start I2C Port.");
        while (1)
            ;
    }

    Serial.println("Initializing 9DOF sensor...");
    if (imu.begin() == false) // with no arguments, this uses default addresses (AG:0x6B, M:0x1E) and i2c port (Wire).
    {
        Serial.println("Failed to communicate with LSM9DS1.");
        Serial.println("Double-check wiring.");
        Serial.println("Default settings in this sketch will "
                       "work for an out of the box LSM9DS1 "
                       "Breakout, but may need to be modified "
                       "if the board jumpers are.");
        while (1)
            ;
    }
}

sensorData *getSensorData()
{
    sensorData *data = new sensorData(sensorName);
    // Update the sensor values whenever new data is available
    if (imu.gyroAvailable())
    {
        imu.readGyro();
    }

    if (imu.accelAvailable())
    {
        imu.readAccel();
    }

    if (imu.magAvailable())
    {
        imu.readMag();
    }

    getGyro(data);  // Print "G: gx, gy, gz"
    getAccel(data); // Print "A: ax, ay, az"
    getMag(data);   // Print "M: mx, my, mz"
    getButtons(data);
    getAttitude(data);

    return data;
}