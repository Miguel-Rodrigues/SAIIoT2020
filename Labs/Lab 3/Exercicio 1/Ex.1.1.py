# ex_led ver2.0

import RPi.GPIO as GPIO
import time

led1 = 4
led2 = 3
ledState = True

def toggleLeds(toggle):
    GPIO.output(led1, toggle);
    GPIO.output(led2, not toggle);
    time.sleep(0.5);
    return not toggle;

GPIO.setwarnings(False);
GPIO.setmode(GPIO.BCM);
GPIO.setup(led1, GPIO.OUT);
GPIO.setup(led2, GPIO.OUT);

while(True):
    ledState = toggleLeds(ledState);
    pass

GPIO.cleanup();
