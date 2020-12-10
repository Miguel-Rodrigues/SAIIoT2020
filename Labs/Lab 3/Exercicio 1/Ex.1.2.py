# ex_led ver2.0

import RPi.GPIO as GPIO
import time

class pwm:
    pin: int
    frequency: int
    dutyCucle: int
    pass

pwmPin0 = 13 
pwmPin1 = 19
pwmFrequency0 = 100 #Hz
pwmFrequency1 = 200 #Hz
intensity = 0 #%
intensityStep = True

def setupPWM(pin, dutyCycle):
    GPIO.setup(pin, GPIO.OUT)
    pwm = GPIO.PWM(pin, dutyCycle)
    pwm.start(0)
    return pwm

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

pwm0 = setupPWM(pwmPin0, pwmFrequency0)
pwm1 = setupPWM(pwmPin1, pwmFrequency1)

while(True):
    pwm0.ChangeDutyCycle(intensity)
    pwm1.ChangeDutyCycle(100 - intensity)
    time.sleep(0.01)

    if (intensity == 0):
        intensityStep = 1
        pass
    
    elif (intensity == 100):
        intensityStep = -1
        pass

    intensity += intensityStep;
    pass

GPIO.cleanup();
