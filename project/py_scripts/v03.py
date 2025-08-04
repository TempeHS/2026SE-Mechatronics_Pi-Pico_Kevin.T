"""
Sample code for servo library, demonstrating instantiation
and setting angles for a continuous servo the resulting wheel speed
of a set_duty(x) call are:

| Set duty |  Speed  | Direction |
| -------- | ------- | --------- |
|   500    | Fast    | Backward  |
|   1400   | Slow    | Backward  |
|   1500   | Stopped | None      |
|   1600   | Slow    | Forward   |
|   2500   | Fast    | Forward   |

"""

import time
from machine import Pin, PWM
from servo import Servo


# create a PWM servo controller (16 - pin Pico)
servo_pwm_left = PWM(Pin(16))
servo_pwm_right = PWM(Pin(15))

# Set the parameters of the servo pulses, more details in the "Documentation" section
freq = 50
min_us = 500
max_us = 2500
dead_zone_us = 1500

# create a servo object
left_servo = Servo(
    pwm=servo_pwm_left, min_us=min_us, max_us=max_us, dead_zone_us=dead_zone_us, freq=freq
)
right_servo = Servo(
    pwm=servo_pwm_right, min_us=min_us, max_us=max_us, dead_zone_us=dead_zone_us, freq=freq
)


while True:
    # manually set the servo duty time
    left_servo.set_duty(2500)
    right_servo.set_duty(500)
    time.sleep(2)
