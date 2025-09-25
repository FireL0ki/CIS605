# Project: In class demo - Demo1
# Description: Demonstrate attributes & values
# Date: September 2025

class Car1:

    # region initializer

    def __init__(self, make, model, colour, msrp):
        # in other languages, you first declare attributes are, but in Python can do it directly in the initializer
        self.car_make = make
        self.car_model = model
        self.car_colour = colour
        self.car_msrp = msrp
        # do not need a parameter, as we've already set the value
        self.car_speed = 0

    def sample(self):
        test = self.car_colour
        return test

    # endregion

    # region instance methods

    # provide a default value, used if there is no increase_by_amount parameter passed in
    def accelerate(self, increase_by_amount=5):
        # new_speed = self.car_speed + increase_by_amount

        # shortened version, equivalent of above
        self.car_speed += increase_by_amount

        # return new_speed

    def __str__(self):

        return f'Make: {self.car_make}\nModel: {self.car_model}\nColor: {self.car_colour}\nMSRP: ${self.car_msrp:,}\nSpeed: {self.car_speed} mph'
    
    # endregion
