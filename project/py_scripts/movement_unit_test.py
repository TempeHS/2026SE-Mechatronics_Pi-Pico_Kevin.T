from machine import Pin, PWM
from movement import Movement
from servo import Servo
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

movement = Movement(left_servo, right_servo, True)


print("forwards")
movement.forwards()
sleep(1)
print("backwards")
movement.backwards()
sleep(1)
print("stop")
movement.stop()
sleep(1)
print("turning right")
movement.turn_right()
sleep(1)
print("turning left")
movement.turn_left()
sleep(1)
movement.stop()