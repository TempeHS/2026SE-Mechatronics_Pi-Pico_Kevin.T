class Colour_sensor:
    def __init__(self, colour_sensor, debug):
        self.__colour_sensor = colour_sensor
        self.__debug = debug

    def sense(self):
        if self.__debug:
            print("sensing")
        hsv = self.__colour_sensor.readHSV()
        
        hue = hsv["hue"]
        if hue > 75 and hue < 85:
            return "green"
        else:
            return "not green"