# LED intensity
import RPi.GPIO as GPIO
GPIO.setwarnings(False)
led_pin=18
GPIO.setmode(GPIO.BCM)
GPIO.setup(led_pin,GPIO.OUT)
pwm_led=GPIO.PWM(led_pin,500) # update frequency 500Hz
pwm_led.start(100)
while True:
    duty_s= input("Enter the brightness value (0 to 100):")
    duty=int(duty_s)
    pwm_led.ChangeDutyCycle(duty)
GPIO.cleanup()
