# ex_led ver2.0

import RPi.GPIO as GPIO
import time

class Motor:
    __pwm: GPIO.PWM
    __driver1: int
    __driver2: int
    
    def __init__(self, pwmPin: int, driverPin1: int, driverPin2: int, frequency: int):
        self.__driver1 = driverPin1
        self.__driver2 = driverPin2
    
        GPIO.setup(self.__driver1, GPIO.OUT);
        GPIO.setup(self.__driver2, GPIO.OUT);
        self.setDirection(True);
        
    
        GPIO.setup(pwmPin, GPIO.OUT)
        self.__pwm = GPIO.PWM(pwmPin, frequency)
        self.__pwm.start(0)
        pass
    
    def setSpeed(self, speed: int):
        self.__pwm.ChangeDutyCycle(speed)
        pass

    #def stop(self):
    #    self.__pwm.ChangeDutyCycle(0)
    #    pass

    #def forward(self):
    #    self.__pwm.ChangeDutyCycle(100)
    #    pass
    
    def setDirection(self, clockwise: bool):
        GPIO.output(self.__driver1, clockwise);
        GPIO.output(self.__driver2, not clockwise);
        pass
    pass

intensity = 0 #%
intensityStep = True
clockwise = True


GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

motor1 = Motor(13, 9, 11, 100)
motor2 = Motor(19, 26, 6, 100)

while(True):
    motor1.setSpeed(intensity)
    motor2.setSpeed(intensity)
    time.sleep(0.01)

    if (intensity == 0):
        intensityStep = 1
        clockwise = not clockwise
        motor1.setDirection(clockwise)
        motor2.setDirection(clockwise)
        pass
    
    elif (intensity == 100):
        intensityStep = -1
        pass

    intensity += intensityStep;
    pass

GPIO.cleanup();
