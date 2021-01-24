# AccelKartServer/services/WatchdogService.py

#Source: https://stackoverflow.com/questions/16148735/how-to-implement-a-watchdog-timer-in-python
from datetime import datetime
from datetime import timedelta
from background_task import background
import logging

class WatchdogService(Exception):

    touched = False
    running = False
    timeout = 0

    def __init__(self, timeout, userHandler = None):  # timeout in milliseconds
        self.__logger = logging.getLogger(__name__)
        self.__logger.debug("Releasing the watchdog.")
        
        self.timeout = timeout
        self.userHandler = userHandler
        self.handler(schedule=timedelta(milliseconds = timeout))

    def reset(self):
        self.__logger.debug("Feeding the watchdog.")
        self.touched = True

    def stop(self):
        self.__logger.debug("Putting the leash...")
        self.touched = False
        self.running = False

    @background(schedule=timedelta(milliseconds = 1000))
    def handler(self):
        if (not self.touched):
            self.__logger.debug("Watchdog bitten the cat!!")
            self.stop()
            if self.userHandler is not None:
                self.userHandler()
            else:
                self.defaultHandler()
            pass
        elif(self.running):
            self.touched = False
            self.handler(schedule=timedelta(milliseconds = self.timeout))
            pass

    def defaultHandler(self):
        raise self