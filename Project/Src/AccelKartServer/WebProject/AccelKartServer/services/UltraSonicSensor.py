#Libraries
import logging
import RPi.GPIO as GPIO
import time

class UltraSonicSensor:
    __logger: logging.Logger

    #set GPIO Pins
    __triggerPin = 21
    __echoPin = 20

    #Speed of sound
    __echoSpeed = 34300

    def __init__(self): 
        self.__logger = logging.getLogger(__name__)
        #GPIO Mode (BOARD / BCM)
        GPIO.setmode(GPIO.BCM)
        
        #set GPIO direction (IN / OUT)
        GPIO.setup(self.__triggerPin, GPIO.OUT)
        GPIO.setup(self.__echoPin, GPIO.IN)
        pass

    def getDistance(self):
        # set Trigger to HIGH
        GPIO.output(self.__triggerPin, True)
    
        # set Trigger after 0.01ms to LOW
        time.sleep(0.00001)
        GPIO.output(self.__triggerPin, False)
    
        StartTime = time.time()
        StopTime = time.time()
    
        # save StartTime
        while GPIO.input(self.__echoPin) == 0:
            StartTime = time.time()
    
        # save time of arrival
        while GPIO.input(self.__echoPin) == 1:
            StopTime = time.time()
    
        # time difference between start and arrival
        TimeElapsed = StopTime - StartTime

        # multiply with the sonic speed (34300 cm/s)
        # and divide by 2, because there and back
        distance = (TimeElapsed * self.__echoSpeed) / 2
        
        self.__logger.debug("Measured distance: " + str(distance) + "cm.")
        return distance
