#from sense_hat import SenseHat
from sense_emu import SenseHat

sense = SenseHat()
    
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)

while True:
    acceleration = sense.get_accelerometer_raw()
    x = acceleration['x']
    y = acceleration['y']
    z = acceleration['z']
            
    x = abs(x)
    y = abs(y)
    z = abs(z)
        
    if x > 1:
        sense.show_letter("X", red)
    if y > 1:
        sense.show_letter("Y", green)
    if z > 1:
        sense.show_letter("Z", blue)
        
    if x <= 1 and y <= 1 and z <= 1:
        sense.clear()
            
