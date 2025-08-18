class Controller:
    def __init__(self, movement, front_us, side_us, colour_sensor, lcd, debug):
        self.__movement = movement
        self.__front_us = front_us
        self.__side_us = side_us
        self.__colour_sensor = colour_sensor
        self.__lcd = lcd
        self.state = "IDLE"
        self.__last_state_change = time()
        self.__debug = debug
    
    def read_dist(self):
        if self.__debug:
            print("read dist")
        return [self.__front_us.distance_mm, self.__side_us.distance_mm]
    
    def set_idle_state(self):
        if self.__debug:
            print("IDLE state")
        self.state = "IDLE"
        self.__movement.stop()

    def set_forwards_state(self):
        if self.__debug:
            print("FORWARDS state")
        self.state = "FORWARDS"
        self.__movement.forwards()

    def set_backwards_state(self):
        if self.__debug:
            print("BACKWARDS state")
        self.state = "BACKWARDS"
        self.__movement.backwards()

    def set_lturn_state(self):
        if self.__debug:
            print("LTURN state")
        self.state = "LTURN"
        self.__movement.turn_left()

    def set_rturn_state(self):
        if self.__debug:
            print("RTURN state")
        self.state = "RTURN"
        self.__movement.turn_right()

    def set_error_state(self):
        if self.__debug:
            print("ERROR state")
        self.state = "ERROR"
        self.__movement.stop()

    def set_detected_state(self):
        if self.__debug:
            print("DETECTED state")
        self.state = "DETECTED"
        self.__movement.stop()
    
    def update(self):
        time_now = time()
        if self.state == "IDLE":
            self.set_idle_state()
            if time_now - self.__last_state_change >= 5:
                self.set_forwards_state()
                self.__last_state_change = time_now

        elif self.state == "FORWARDS":
            self.set_forwards_state()

            # wall following is here
            fdist, sdist = self.read_dist()
            detect_range = 100

            ###### need to add a delay before it turns so it doesnt run into the wall
            # if side no wall then left
            if sdist >= detect_range:
                sleep(0.1) # little delay before turning
                self.set_lturn_state()
            
            # if side wall and front wall then right
            if sdist <= detect_range and fdist <= detect_range:
                sleep(0.1)
                self.set_rturn_state()

            # colour sensing
            if self.__colour_sensor.sense():
                self.set_detected_state()

        elif self.state == "BACKWARDS":
            self.set_backwards_state()

        elif self.state == "LTURN":
            self.set_lturn_state()
            # 1 second duration
            # may need to change this to a sleep or something so its more accurate coz riht now it runs on a global clock instead of a time period after right now
            if time_now - self.__last_state_change >= 1:
                self.set_forwards_state()
                self.__last_state_change = time_now

        elif self.state == "RTURN":
            self.set_rturn_state()
            # 1 second duration
            if time_now - self.__last_state_change >= 1:
                self.set_forwards_state()
                self.__last_state_change = time_now

        elif self.state == "DETECTED":
            self.set_detected_state()
            # 3 second duration
            if time_now - self.__last_state_change >= 3:
                self.set_forwards_state()
                self.__last_state_change = time_now

        else:
            self.set_error_state()

        # update lcd with state
        self.__lcd.fill(0)
        self.__lcd.text(self.state, 30, 20, 1)
        self.__lcd.show()

# test is here coz the time() in controller doesnt work in another file

from machine import Pin, PWM
from movement import Movement
from servo import Servo
from PiicoDev_Ultrasonic import PiicoDev_Ultrasonic
from colour_sensor import Colour_sensor
from PiicoDev_VEML6040 import PiicoDev_VEML6040
from PiicoDev_SSD1306 import *
from controller import Controller
from time import sleep, time


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

print("testing update")
while True:
    system.update()
    sleep(0.01)

print("testing system")
sleep(2)
print("testing forwards state")
system.set_forwards_state()
sleep(2)
print("testing idle state")
system.set_idle_state()
sleep(2)
print("testing backwards state")
system.set_backwards_state()
sleep(2)
print("testing lturn state")
system.set_lturn_state()
sleep(2)
print("testing rturn state")
system.set_rturn_state()
sleep(2)
system.set_idle_state()
