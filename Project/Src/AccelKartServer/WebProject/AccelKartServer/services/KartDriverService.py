# AccelKartServer/services/KartDriverService.py
# https://stackoverflow.com/questions/37916077/django-run-code-on-application-start-but-not-on-migrations
import asyncio
import sys
import logging
import RPi.GPIO as GPIO
import math as math
import copy as copy
from threading import Lock
from .WatchdogService import WatchdogService
from ..models import SensorData
from .UltraSonicSensor import UltraSonicSensor

class KartDriverService():
    __watchdog: WatchdogService
    __leftMotorPin1 = 26
    __leftMotorPin2 = 19
    __rightMotorPin1 = 13
    __rightMotorPin2 = 11
    __frequency = 100
    __deadzone = 1
    __limitDistance = 5

    __rollThreshold = 60
    __pitchThreshold = 45

    __warningLed = 4
    __hornLed = 3

    __leftPWM1: GPIO.PWM
    __leftPWM2: GPIO.PWM
    __rightPWM1: GPIO.PWM
    __rightPWM2: GPIO.PWM

    __logger: logging.Logger

    def __init__(self):
        self.__logger = logging.getLogger(__name__)
        self.__logger.info("Initializing Kart Driver Service")
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)
        GPIO.setup(self.__warningLed, GPIO.OUT)
        GPIO.setup(self.__hornLed, GPIO.OUT)

        self.__leftPWM1 = self.__initMotor(self.__leftMotorPin1, self.__frequency)
        self.__leftPWM2 = self.__initMotor(self.__leftMotorPin2, self.__frequency)
        self.__rightPWM1 = self.__initMotor(self.__rightMotorPin1, self.__frequency)
        self.__rightPWM2 = self.__initMotor(self.__rightMotorPin2, self.__frequency)

        self.__ultrasonicsensor = UltraSonicSensor()
        self.__watchdog = WatchdogService(1, self.stopKart)
        pass

    def __initMotor(self, pin, frequency):
        GPIO.setup(pin, GPIO.OUT)
        pwm = GPIO.PWM(pin, frequency)
        pwm.start(0)
        return pwm

    def calculateRatio(self, value, deadzone, threshold):
        if (math.fabs(value) < deadzone):
            return 0
        elif (math.fabs(value) > threshold):
            return math.copysign(1, value)
        else:
            return value / threshold

    def checkButtonActions(self, request):
        if (request.button1 == 'true'):
            GPIO.output(self.__warningLed, GPIO.HIGH)
            # self.calibrate(request)
            self.stopKart()
            return False

        else:
            GPIO.output(self.__warningLed, GPIO.LOW)
            pass

        if (request.button2 == 'true'):
            self.__logger.warn("HONK HONK!!!")
            GPIO.output(self.__hornLed, GPIO.HIGH)
            pass
        else:
            GPIO.output(self.__hornLed, GPIO.LOW)
            pass

        return True

    def moveKart(self, request: SensorData):
        if (self.checkButtonActions(request)):
            # request = self.applyCalibration(request)
            
            self.__logger.debug("Calculating pwm ratios")
            pitchRatio = self.calculateRatio(request.pitch, self.__deadzone, self.__pitchThreshold)
            rollRatio = self.calculateRatio(request.roll, self.__deadzone, self.__rollThreshold)
            self.__logger.debug("pitch: " + str(request.pitch) + ", roll: " + str(request.roll))
            self.__logger.debug("pitchRatio: " + str(pitchRatio) + ", rollRatio: " + str(rollRatio))

            self.__logger.debug("Setting duty cycles")
            if (pitchRatio >= 0):
                if asyncio.run(self.__ultrasonicsensor.getDistance()) >= self.__limitDistance:
                    if (rollRatio >= 0):
                        self.setDutyCycles(0, pitchRatio * (1 - rollRatio/2), 0, pitchRatio)
                        pass
                    else:
                        self.setDutyCycles(0, pitchRatio, 0, pitchRatio * (1 + rollRatio / 2))
                        pass
                else:
                    self.__logger.warn("Distance to short to drive through. Stopping!!")
                    GPIO.output(self.__warningLed, GPIO.HIGH)
                    self.stopKart()
                    pass
            else:
                if (rollRatio >= 0):
                    self.setDutyCycles(-pitchRatio * (1 - rollRatio/2), 0, -pitchRatio, 0)
                    pass
                else:
                    self.setDutyCycles(-pitchRatio, 0, -pitchRatio * (1 + rollRatio / 2), 0)
                    pass
                pass
            pass

            self.__watchdog.reset()
            pass
        pass

    def setDutyCycles(self, left1, left2, right1, right2):
        self.__logger.debug("left PWMs: (" + str(left1) + ", " + str(left2) + ")")
        self.__logger.debug("right PWMs: (" + str(right1) + ", " + str(right2) + ")")

        self.__leftPWM1.ChangeDutyCycle(left1 * 100)
        self.__leftPWM2.ChangeDutyCycle(left2 * 100)
        self.__rightPWM1.ChangeDutyCycle(right1 * 100)
        self.__rightPWM2.ChangeDutyCycle(right2 * 100)
        pass

    # def calibrate(self, request: SensorData):
    #     self.__calibration = copy.deepcopy(request)
    #     pass

    # def applyCalibration(self, request: SensorData) -> SensorData:
    #     # {
    #     #     "name": "",
    #     #     "gyro": { "x" : 0 , "y" : 0, "z" : 0 },
    #     #     "accel": { "x" : 0 , "y" : 0, "z" : 0 },
    #     #     "compass": { "x" : 0 , "y" : 0, "z" : 0 },
    #     #     "pitch": 0, "roll" : 0, "heading" : 0,
    #     #     "button1": True, "button2" : False
    #     # }
    #     if self.__calibration is not None:
    #         request.accel.x -= self.__calibration.accel.x
    #         request.accel.y -= self.__calibration.accel.y
    #         request.accel.z -= self.__calibration.accel.z
    #         request.gyro.x -= self.__calibration.gyro.x
    #         request.gyro.y -= self.__calibration.gyro.y
    #         request.gyro.z -= self.__calibration.gyro.z
    #         request.compass.x -= self.__calibration.compass.x
    #         request.compass.y -= self.__calibration.compass.y
    #         request.compass.z -= self.__calibration.compass.z
    #         request.pitch -= self.__calibration.pitch
    #         request.roll -= self.__calibration.roll
    #         request.heading -= self.__calibration.heading
    #         if (math.fabs(request.pitch) > 180):
    #             request.pitch -= 360
    #             pass
    #         if (math.fabs(request.roll) > 180):
    #             request.roll -= 360
    #             pass
    #         if (math.fabs(request.heading) > 180):
    #             request.heading -= 360
    #         pass
    #     return request

    def stopKart(self):
        self.__logger.debug("Hit the brake!!! I'm going to crash!!")
        self.__leftPWM1.ChangeDutyCycle(0)
        self.__leftPWM2.ChangeDutyCycle(0)
        self.__rightPWM1.ChangeDutyCycle(0)
        self.__rightPWM2.ChangeDutyCycle(0)
        pass
