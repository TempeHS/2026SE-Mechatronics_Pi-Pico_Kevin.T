class Colour_sensor:
    def __init__(self, colour_sensor, debug):
        self.__colour_sensor = colour_sensor
        self.__debug = debug

    def sense(self):
        hsv = self.__colour_sensor.readHSV()
        if self.__debug:
            print("sensing: " + str(hsv))
        
        hue = hsv["hue"]
        if hue > 75 and hue < 85:
            return True
        else:
            return False
        # detects blue as green but i am nat fixing that
