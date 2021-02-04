#Libraries
import time
import logging
import asyncio
import RPi.GPIO as GPIO

class UltraSonicSensor:
    __logger: logging.Logger

    #set GPIO Pins
    __triggerPin = 21
    __echoPin = 20
    __maxDistance =  500 * 58.31 #500cm limit

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

    def __del__(self):
        self.loop.close()

    async def getDistance(self):
        self.__logger.debug("looping....")
        # set Trigger to HIGH
        GPIO.output(self.__triggerPin, True)
    
        # set Trigger after 0.01ms to LOW
        await asyncio.sleep(0.00001)
        GPIO.output(self.__triggerPin, False)
    
        StartTime = time.time()
        StopTime = time.time()
    
        # save StartTime
        while GPIO.input(self.__echoPin) == 0 and time.time() - StartTime < self.__maxDistance:
            StartTime = time.time()

        distance = float('inf')
        if (time.time() - StartTime < self.__maxDistance):    
            # save time of arrival
            while GPIO.input(self.__echoPin) == 1:
                StopTime = time.time()
        
            # time difference between start and arrival
            TimeElapsed = StopTime - StartTime

            # multiply with the sonic speed (34300 cm/s)
            # and divide by 2, because there and back
            distance = (TimeElapsed * self.__echoSpeed) / 2
            pass

        self.__logger.debug("Measured distance: " + str(distance) + "cm.")
        return distance
