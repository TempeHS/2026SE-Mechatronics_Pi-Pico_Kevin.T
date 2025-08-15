from machine import Pin, PWM
from movement import Movement
from servo import Servo
from PiicoDev_Ultrasonic import PiicoDev_Ultrasonic
from time import sleep

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

movement = Movement(left_servo, right_servo, False)
front_us = PiicoDev_Ultrasonic(id=[0, 0, 0, 0])
side_us = PiicoDev_Ultrasonic(id=[1, 0, 0, 0])

while True:
    print(f"Front: {front_us.distance_mm}mm, Side: {side_us.distance_mm}mm")
    if front_us.distance_mm > 200:
        movement.forwards()
    else:
        movement.turn_right()
    sleep(0.1)

