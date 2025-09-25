# Project: In class demo - Demo1
# Description: Demonstrates Class Level Attributes & Methods
# Date: September 2025

class Car3:

    # region class attributes

    __num_cars = 0
    __total_msrp = 0

    # endregion

    # region initializer

    def __init__(self, make, model, colour, msrp):
        # in other languages, you first declare attributes are, but in Python can do it directly in the initializer

        # two __underscores indicate these attributes are private
        self.__car_make = make
        self.__car_model = model
        self.__car_colour = colour
        self.__car_msrp = msrp
        # does not need a parameter, as we've already set the value
        self.__car_speed = 0
        
        # class method, prefixed with class name, using private attribute denoted by __
        Car3.__increment_totals(self)

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

    # region class methods

    # @ denotes a decorator, like a getter or setter | cls keyword for class
    @classmethod
    def __increment_totals(cls, self):
        cls.__num_cars += 1
        cls.__total_msrp += self.car_msrp

    # only need a reference to a class, as we are only using the class level variables, so we do not need the object level (self)
    @classmethod
    def __calc_average_msrp(cls):
        # preface with cls. for class level variables
        return cls.__total_msrp / cls.__num_cars
        # if you have not created any car objects and run this, it will be dividing by zero and throw an error

    # class level method to give information about class level attributes - similar to the string method
    # not __private, this is accessible outside the class
    @classmethod
    def summary_info(cls):
        # need to use __double underscore on the variables, as we do not have getters or setters for these class level variables
        return f'Number of Cars: {cls.__num_cars:,}\nTotal MSRP: ${cls.__total_msrp:,}\nAverage MSRP: ${cls.__calc_average_msrp():,.2f}'

    # endregion
