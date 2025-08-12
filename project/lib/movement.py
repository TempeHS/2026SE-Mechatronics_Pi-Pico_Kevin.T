class Movement:
    def __init__(self, left_servo, right_servo, debug):
        self.__left_servo = left_servo
        self.__right_servo = right_servo
        self.__debug = debug

    def stop(self):
        if self.__debug:
            print("stopping")
        self.__left_servo.stop()
        self.__right_servo.stop()

    def forwards(self):
        if self.__debug:
            print("moving forwards")
        self.__left_servo.set_duty(2000)
        self.__right_servo.set_duty(1000)

    def backwards(self):
        if self.__debug:
            print("moving backwards")
        self.__left_servo.set_duty(1000)
        self.__right_servo.set_duty(2000)

    def turn_right(self):
        if self.__debug:
            print("turning right")
        self.__left_servo.set_duty(2000)
        self.__right_servo.set_duty(1500)

    def turn_left(self):
        if self.__debug:
            print("turning left")
        self.__left_servo.set_duty(1500)
        self.__right_servo.set_duty(2000)
        # it dont werk 💔