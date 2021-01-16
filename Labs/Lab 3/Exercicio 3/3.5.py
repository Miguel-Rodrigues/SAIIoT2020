#from sense_hat import SenseHat
from sense_emu import SenseHat

sense = SenseHat()

while True:
    
    red = (255, 0, 0)
    green = (0, 255, 0)
    h_margin = 5
    recommended_h = 60
    t_range = range(20, 25)
    h_range = range(recommended_h - (h_margin \ 2))
    
    t = sense.get_temperature()
    p = sense.get_pressure()
    h = sense.get_humidity()
   
    t = round(t,1)
    p = round(p,1)
    h = round(h,1)
   
    message = "Temperature: " + str(t) + "Pressure: " + str(p) + "Humidity: " + str(h)
   
    if(t in t_range and h in h_range):
        tela=green
    else:
        tela=red
  
    sense.show_message(message, back_colour=tela, scroll_speed=0.05)
