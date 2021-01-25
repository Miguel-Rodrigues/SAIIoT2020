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
    __lastDistance = 0
    loop = asyncio.get_event_loop()

    #Speed of sound
    __echoSpeed = 34300

    def __init__(self): 
        self.__logger = logging.getLogger(__name__)
        #GPIO Mode (BOARD / BCM)
        GPIO.setmode(GPIO.BCM)
        
        #set GPIO direction (IN / OUT)
        GPIO.setup(self.__triggerPin, GPIO.OUT)
        GPIO.setup(self.__echoPin, GPIO.IN)

        asyncio.ensure_future(self.updateDistance(), self.loop)
        self.loop.run_forever()
        pass

    def __del__(self):
        self.loop.close()

    def getDistance(self):
        self.__logger.debug("Measured distance: " + str(self.__lastDistance) + "cm.")
        self.__lastDistance
        pass

    async def updateDistance(self):
        while (True):
            # set Trigger to HIGH
            GPIO.output(self.__triggerPin, True)
        
            # set Trigger after 0.01ms to LOW
            await asyncio.sleep(0.00001)
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
            self.__lastDistance = (TimeElapsed * self.__echoSpeed) / 2
            pass
