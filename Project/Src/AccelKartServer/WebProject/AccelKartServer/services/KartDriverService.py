# AccelKartServer/services/KartDriverService.py
from threading import Lock
from .WatchdogService import WatchdogService
import RPi.GPIO as GPIO

class SingletonMeta(type):
    """
    This is a thread-safe implementation of Singleton.
    """

    _instances = {}

    _lock: Lock = Lock()
    """
    We now have a lock object that will be used to synchronize threads during
    first access to the Singleton.
    """

    def __call__(cls, *args, **kwargs):
        """
        Possible changes to the value of the `__init__` argument do not affect
        the returned instance.
        """
        # Now, imagine that the program has just been launched. Since there's no
        # Singleton instance yet, multiple threads can simultaneously pass the
        # previous conditional and reach this point almost at the same time. The
        # first of them will acquire lock and will proceed further, while the
        # rest will wait here.
        with cls._lock:
            # The first thread to acquire the lock, reaches this conditional,
            # goes inside and creates the Singleton instance. Once it leaves the
            # lock block, a thread that might have been waiting for the lock
            # release may then enter this section. But since the Singleton field
            # is already initialized, the thread won't create a new object.
            if cls not in cls._instances:
                instance = super().__call__()
                cls._instances[cls] = instance
        return cls._instances[cls]

class KartDriverService(metaclass=SingletonMeta):
    __watchdog: WatchdogService
    __leftMotorPins = (26, 19)
    __rightMotorPins = (13, 8)
    __leftPWMs: None
    __rightPWMs: None
    __isLeftMotorClockwise = True
    __isRightMotorClockwise = True
    __frequency = 100

    def __init__(self): 
        print("Initializing Kart Driver Service")
        self.__watchdog = WatchdogService(1000, self.stopKart)
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)

        self.__leftPWMs = self.__initMotor(self.__leftMotorPins, 100)
        self.__rightPWMs = self.__initMotor(self.__rightMotorPins, 100)
        pass

    def __initMotor(self, pins, frequency):
        for pin in pins:
            GPIO.setup(pin, GPIO.OUT)
            pwm = GPIO.PWM(pin, frequency)
            pwm.start(0)
            yield pwm

    def moveKart(self, request):
        print("hit!" + request)
        self.__watchdog.reset()
        pass

    def stopKart(self):
        [pwm.ChangeDutyCycle(0) for pwm in self.__leftPWMs +  self.__rightPWMs]
        pass