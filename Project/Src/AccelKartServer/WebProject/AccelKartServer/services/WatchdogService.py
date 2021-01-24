# AccelKartServer/services/WatchdogService.py

#Source: https://stackoverflow.com/questions/16148735/how-to-implement-a-watchdog-timer-in-python
from logging import Logger
import logging
from threading import Timer

class WatchdogService(Exception):
    def __init__(self, timeout, userHandler=None):  # timeout in seconds
        self.__logger = logging.getLogger(__name__)
        self.__logger.debug("Releasing the watchdog.")
        
        self.timeout = timeout
        self.userHandler = userHandler
        self.timer = Timer(self.timeout, self.handler)
        self.timer.start()

    def reset(self):
        self.__logger.debug("Feeding the watchdog.")
        self.timer.cancel()
        self.timer = Timer(self.timeout, self.handler)
        self.timer.start()

    def stop(self):
        self.__logger.debug("Putting the leash...")
        self.timer.cancel()

    def handler(self):
        self.__logger.debug("Watchdog bitten the cat!!")
        if self.userHandler is not None:
            self.userHandler()
        else:
            self.defaultHandler()
        pass

    def defaultHandler(self):
        raise self