from colour_sensor import Colour_sensor
from PiicoDev_VEML6040 import PiicoDev_VEML6040
from time import sleep

sensor = PiicoDev_VEML6040()

colour_sensor = Colour_sensor(sensor, False)

while True:
    print(colour_sensor.sense())
    sleep(0.1)