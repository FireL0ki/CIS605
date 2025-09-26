# Project: In class demo - Demo1
# Description: Demonstrate attributes & values
# Date: September 2025

class Car2:

    # region initializer

    def __init__(self, make, model, colour, msrp):
        # in other languages, you first declare attributes are, but in Python can do it directly in the initializer

        # two __underscores indicate these attributes are private
        self.__car_make = make
        self.__car_model = model
        self.__car_colour = colour
        self.__car_msrp = msrp
        # do not need a parameter, as we've already set the value
        self.__car_speed = 0

    # endregion

    # region properties (getters & setters)

    # getter use to get the private attribute value, and setter to set the private attribute value from outside the class

    # getter for getting access to car_make -- cannot access the __car_make attribute in __init__ directly, this 'getter' can be used to 'get' access to the private attribute from outside the class
    @property
    def car_make(self):
        return self.__car_make
    
    @property
    def car_model(self):
        return self.__car_model
    
    @property
    def car_colour(self):
        return self.__car_colour
    
    @car_colour.setter
    def car_colour(self,value):
        self.__car_colour = value
    
    # not needed - want to keep this private, not changeable from the outside
    @property
    def car_msrp(self):
        return self.__car_msrp    
        
    @property
    def car_speed(self):
        return self.__car_speed
    
    # endregion


    # region instance methods

    # provide a default value, used if there is no increase_by_amount parameter passed in
    def accelerate(self, increase_by_amount=5):
        # new_speed = self.__car_speed + increase_by_amount
        
        # should use the __property name to access the attribute

        # shortened version, equivalent of above
        self.__car_speed += increase_by_amount

    def __str__(self):

        return f'Make: {self.car_make}\nModel: {self.car_model}\nColor: {self.car_colour}\nMSRP: ${self.car_msrp:,}\nSpeed: {self.car_speed} mph'
    
    # endregion
