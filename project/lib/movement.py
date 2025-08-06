from machine import Pin, PWM
from servo import Servo


servo_pwm = PWM(Pin("pin"))
freq = 50
min_us = 500
max_us = 2500
dead_zone_us = 1500

left_servo = Servo(
    pwm=servo_pwm, min_us=min_us, max_us=max_us, dead_zone_us=dead_zone_us, freq=freq
)


class Movement:
    def __init__(self, left_servo, right_servo, debug):
        self.__left_servo = left_servo
        self.__right_servo = right_servo
        self.__debug = debug

    def forwards(self):
        