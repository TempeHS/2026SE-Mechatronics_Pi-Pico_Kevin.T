from time import sleep_ms

'''

'''

class Controller:
    def __init__(self, movement, front_us, side_us, colour_sensor, lcd, debug):
        self.__movement = movement
        self.__front_us = front_us
        self.__side_us = side_us
        self.__colour_sensor = colour_sensor
        self.__lcd = lcd
        self.state = "IDLE"
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
        if self.state == "IDLE":
            self.set_idle_state()
            sleep_ms(5000)
            self.set_forwards_state()

        elif self.state == "FORWARDS":
            self.set_forwards_state()

            ### wall following is here
            fdist, sdist = self.read_dist()
            detect_range = 150

            # if side no wall then left
            if sdist >= detect_range:
                sleep_ms(500) # little delay before turning
                self.set_lturn_state()
            
            # if side wall and front wall then right
            if sdist <= detect_range and fdist <= detect_range:
                sleep_ms(500)
                self.set_rturn_state()

            # colour sensing
            if self.__colour_sensor.sense():
                self.set_detected_state()

        elif self.state == "BACKWARDS":
            self.set_backwards_state()

        elif self.state == "LTURN":
            self.set_lturn_state()
            # 1 second duration
            sleep_ms(990)
            self.set_forwards_state()
            sleep_ms(500)

        elif self.state == "RTURN":
            self.set_rturn_state()
            # 1 second duration
            sleep_ms(990)
            self.set_forwards_state()
            sleep_ms(500)

        elif self.state == "DETECTED":
            self.set_detected_state()
            # 3 second duration
            sleep_ms(3000)
            self.set_forwards_state()

        else:
            self.set_error_state()

        # update lcd with state
        self.__lcd.fill(0)
        self.__lcd.text(self.state, 30, 20, 1)
        self.__lcd.show()

