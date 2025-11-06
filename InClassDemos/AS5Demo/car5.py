
class Car5:

    def __init__(self, horsepower):
        self.__horsepower = horsepower
        self.__current_speed = 0
        self.__max_speed = self.__set_max_speed()

    @property
    def current_speed(self):
        return self.__current_speed
    
    def __set_max_speed(self):
        max_speed = 0

        if self.__horsepower <= 150:
            ma_speed = 250
        elif self.__horsepower <= 200:
            max_speed = 280
        elif self.__horsepower <= 250:
            max_speed = 320
        else:
            max_speed = 350

        return max_speed
    
    # similar to add water method
    def increase_speed(self, mph):

        message = ""
        current_to_max = self.__max_speed - self.__current_speed

        if current_to_max >= mph:
            self.__current_speed += mph
            message = f"Speed increased by {mph} mph\nCurrent speed is: {self.current_speed}"
        else:
            message = f"Not possible to increase speed.\nCurrent speed is {self.current_speed} mph\nCan increase speed by {current_to_max} mph"
        return message
    
    def decrease_speed(self, mph):

        message = ""

        if self.current_speed - mph >= 0:
            self.__current_speed -= mph
            message = f"Speed decreased by {mph} mph\nCurrent speed is: {self.current_speed}"
        else:
            message = f"Not possible to decrease speed.\nCurrent speed is {self.current_speed} mph\nCan decrease speed by {self.current_speed} mph"
        return message
    
    # similar to water add per second, just increase and return a true or false value, don't return a message
    def speed_up(self, mph):
        current_to_max = self.__max_speed - self.__current_speed

        if current_to_max >= mph:
            self.__current_speed += mph
            return True
        else:
            return False
        

    def slow_down(self, mph):
        if self.__current_speed - mph >= 0:
            self.__current_speed -= mph
            return True
        else:
            return False
    
    def __str__(self):
        return f'Car HP: {self.__hp}\nMax speed: {self.__max_speed}\nCurrent speed: {self.current_speed}'
