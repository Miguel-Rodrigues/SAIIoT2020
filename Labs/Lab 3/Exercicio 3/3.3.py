#from sense_hat import SenseHat
from sense_emu import SenseHat

sense = SenseHat()

sense.clear()

#pressure

pressure = sense.get_pressure()

print("Pressão = ", pressure)

#temperature
sense.clear()

temp = sense.get_temperature()

print("Temperatura = ", temp)

#humidity

sense.clear()

humidity = sense.get_humidity()

print("Humidade = ", humidity)