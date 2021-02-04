# AccelKartServer/services/WatchdogService.py

import logging
import threading
import time

class WatchdogService(Exception):

    __touched: bool = False
    __running: bool = False
    __timeout: float = 0
    __userHandler = None
    __loop = None

    def __init__(self, timeout = 60, userHandler = None):  # timeout in seconds
        self.__logger = logging.getLogger(__name__)        
        self.__timeout = timeout
        self.__userHandler = userHandler
        pass

    def __del__(self):
        pass

    def reset(self):
        self.__logger.debug("Petting the watchdog.")
        self.__touched = True
        if (not self.__running):
            self.__running = True
            self.__logger.debug("Releasing the watchdog.")
            t = threading.Thread(target=self.__checkWatchdog)
            t.setDaemon(True)
            t.start()
            pass

    def stop(self):
        self.__logger.debug("Putting the leash...")
        self.__touched = False
        self.__running = False

    def __checkWatchdog(self):
        while(self.__touched):
            if (self.__running):
                self.__touched = False
                self.__logger.debug("Watchdog is on guard...")
                time.sleep(self.__timeout)
            else:
                self.__logger.debug("Watchdog is sleeping...")
                return

        self.__logger.debug("Watchdog bitten the cat!!")
        self.stop()
        if self.__userHandler is not None:
            self.__userHandler()
        else:
            self.__defaultHandler()

    def __defaultHandler(self):
        raise Exception("Whatchdog triggered.")
        pass