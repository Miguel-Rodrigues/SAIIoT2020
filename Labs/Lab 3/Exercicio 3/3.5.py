#from sense_hat import SenseHat
from sense_emu import SenseHat

sense = SenseHat()

def is_in_margin(value, recommended, margin):
    return recommended - (margin / 2) <= value <= recommended + (margin / 2)
    
while True:
    
    red = (255, 0, 0)
    green = (0, 255, 0)
    h_margin = 5
    recommended_h = 60
    t_margin = 5
    recommended_t = 22.5
    
    t = sense.get_temperature()
    p = sense.get_pressure()
    h = sense.get_humidity()
   
    t = round(t,1)
    p = round(p,1)
    h = round(h,1)
   
    t_in_range = is_in_margin(t, recommended_t, t_margin)
    h_in_range = is_in_margin(h, recommended_h, h_margin)
   
    message = "Temperature: " + str(t) + "Pressure: " + str(p) + "Humidity: " + str(h)
   
    if(h_in_range and t_in_range):
        tela=green
    else:
        tela=red
  
    sense.show_message(message, back_colour=tela, scroll_speed=0.05)
