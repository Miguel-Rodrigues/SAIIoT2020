2.1

#button & LED
import RPi.GPIO as GPIO
import time
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
switch_pin=18
led_pin=25 #ou 20
GPIO.setup(switch_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(led_pin, GPIO.OUT)
led_state=False
old_input_state=True # pulled_up
while True:
    new_input_state=GPIO.input(switch_pin)
    if new_input_state==False and old_input_state==True:
        led_state=not led_state
    old_input_state=new_input_state
    GPIO.output(led_pin, led_state)
GPIO.cleanup()

2.2

# LED intensity and button with interruptions
import RPi.GPIO as GPIO #library GPIO
import time #library time
GPIO.setwarnings(False)
led_pin=25 #ou 20
GPIO.setmode(GPIO.BCM)
GPIO.setup(led_pin,GPIO.OUT)
def my_callback(channel):
    print("hit the button ")
GPIO.setup(17, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.add_event_detect(17, GPIO.FALLING, callback=my_callback)
pwm_led=GPIO.PWM(led_pin,500) # refresh rate 500Hz
pwm_led.start(100)
i=0
while True:
    i=i+1
    print(i)
    duty_s=input("Enter the brightness value (0 to 100):")
    duty=int(duty_s)
    pwm_led.ChangeDutyCycle(duty)
    time.sleep(1)
GPIO.cleanup()