# AccelKartServer/services/WatchdogService.py

#Source: https://stackoverflow.com/questions/16148735/how-to-implement-a-watchdog-timer-in-python
import asyncio
import logging
from concurrent.futures import Future

class WatchdogService(Exception):

    touched = False
    running = False
    timeout = 0
    routine: Future = None
    loop = asyncio.get_event_loop()

    def __init__(self, timeout, userHandler = None):  # timeout in milliseconds
        self.__logger = logging.getLogger(__name__)
        self.__logger.debug("Releasing the watchdog.")
        
        self.timeout = timeout
        self.userHandler = userHandler
        self.reset()
        
        task = self.loop.create_task(self.checkWatchdog())
        self.loop.run_until_complete(task)
        pass

    def reset(self):
        self.__logger.debug("Feeding the watchdog.")
        self.touched = True

    def stop(self):
        self.__logger.debug("Putting the leash...")
        self.touched = False
        self.running = False

    async def checkWatchdog(self):
        while(not self.touched):
            if (self.running):
                self.touched = False
                await asyncio.sleep(self.timeout)
            else:
                return

        self.__logger.debug("Watchdog bitten the cat!!")
        self.stop()
        if self.userHandler is not None:
            self.userHandler()
        else:
            self.defaultHandler()

    def defaultHandler(self):
        raise self