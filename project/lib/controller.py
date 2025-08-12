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
        return [self.__front_us.distance_mm, self.__side_us.distance_mm]
    
    def set_idle_state(self):
        if self.__debug:
            print("IDLE state")
        self.state = "IDLE"
        self.__movement.stop()

    def set_forwards_state(self):
        self.__movement.forward()