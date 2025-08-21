from machine import Pin, PWM
from movement import Movement
from servo import Servo
from PiicoDev_Ultrasonic import PiicoDev_Ultrasonic
from colour_sensor import Colour_sensor
from PiicoDev_VEML6040 import PiicoDev_VEML6040
from PiicoDev_SSD1306 import *
from controller import Controller
from time import sleep, time, sleep_ms

servo_pwm_left = PWM(Pin(16))
servo_pwm_right = PWM(Pin(15))
freq = 50
min_us = 500
max_us = 2500
dead_zone_us = 1500
left_servo = Servo(
    pwm=servo_pwm_left, min_us=min_us, max_us=max_us, dead_zone_us=dead_zone_us, freq=freq
)
right_servo = Servo(
    pwm=servo_pwm_right, min_us=min_us, max_us=max_us, dead_zone_us=dead_zone_us, freq=freq
)

wheels = Movement(left_servo, right_servo, False)

fus = PiicoDev_Ultrasonic(id=[0, 0, 0, 0])
sus = PiicoDev_Ultrasonic(id=[1, 0, 0, 0])

sensor = PiicoDev_VEML6040()

colour_sensor = Colour_sensor(sensor, False)


display = create_PiicoDev_SSD1306()


system = Controller(wheels, fus, sus, colour_sensor, display, False)

while True:
    system.update()
    sleep(0.01)