#from sense_hat import SenseHat
from sense_emu import SenseHat

sense = SenseHat()

blue = (0,0,255)

yellow = (255,255,0)

while True:
    
    sense.show_message("SDSI 2018!", text_colour=yellow, back_colour=blue, scroll_speed=0.05)