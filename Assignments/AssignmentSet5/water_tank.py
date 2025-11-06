# Description: Class for a water tank object
# Developer: Sif Oberon
# Date Created: 10.28.2025
# Date Last Modified: 10.31.2025

# import libraries
import math

# Water_Tank class with 4 instance attributes, all private: radius, depth, current water level & max water capacity in gallons
class Water_Tank:
    def __init__(self, radius, depth, __current_water_level_gallons=0):
        self.__radius = radius
        self.__depth = depth
        self.__current_water_level_gallons = __current_water_level_gallons
        self.__max_water_capacity_gallons = self.__calc_max_water_capacity()

    # region getters
    @property
    def radius(self):
        return self.__radius
    
    @property
    def depth(self):
        return self.__depth
    
    @property
    def current_water_level_gallons(self):
        return self.__current_water_level_gallons
    
    @current_water_level_gallons.setter
    def current_water_level_gallons(self, value):
        self.current_water_level_gallons = value
    
    @property
    def max_water_capacity_gallons(self):
        return self.__max_water_capacity_gallons

    # method to calculate and return the maximum water capacity of a tank
    def __calc_max_water_capacity(self):
        # define constants
        GALLONS_IN_ONE_CUBIC_FOOT = 7.48
        # capacity = Pi * radius^2 * depth * 7.48 (1 cubic feet is approximately 7.48 gallons)
        # capacity calculation results in value of type float. Use int() or math.floor() to convert to an integer
        capacity = int(math.pi * (self.radius**2) * self.depth * GALLONS_IN_ONE_CUBIC_FOOT)

        return capacity

    # public method (with one parameter for the gallons of water to add) to add water to the tank if there is capacity
    def add_water_to_tank(self, gallons_water_to_add):
        capacity_available_in_tank = self.max_water_capacity_gallons - self.__current_water_level_gallons
        # check if water_added is less than capacity left in tank
        if gallons_water_to_add <= capacity_available_in_tank:
            # if so, add the gallons_water_to_add to the current wanter in tank
            self.__current_water_level_gallons += gallons_water_to_add
            # return a message confirming the gallons of water added & the tank’s current water level
            return f"{gallons_water_to_add:,} gallons were added to the tank.\nThe tank's water level is now: {self.__current_water_level_gallons:,} gallons."
        
        elif gallons_water_to_add > capacity_available_in_tank:
            # return message indicating the tank will overflow, current water level, & maximum available capacity
            return f"Adding {gallons_water_to_add:,} gallons to the tank will cause the tank to overflow.\nThe tank's current water level is {self.__current_water_level_gallons:,}.\nThe maximum number of gallons that can be added is: {capacity_available_in_tank:,}."

    # public method (with one parameter for the gallons of water to withdraw) to withdraw water from the tank
    def withdraw_water_from_tank(self, gallons_water_to_withdraw):
        # check if the number of gallons to be withdrawn is available in the tank
        if gallons_water_to_withdraw <= self.__current_water_level_gallons:
            # withdraw the water & return message confirming amount withdrawn, tank's current water level
            self.__current_water_level_gallons -= gallons_water_to_withdraw
            return f"Withdrawing {gallons_water_to_withdraw:,} gallons from the tank.\nThe current water level is now: {self.__current_water_level_gallons:,}."
        
        # if the number of gallons to be withdrawn exceeds what the tank currently contains, do not withdraw the water
        elif gallons_water_to_withdraw > self.__current_water_level_gallons:
        # return message indicating not enough water, & the max # of gallons that can be withdrawn from the tank 
            return f"There are not {gallons_water_to_withdraw:,} gallons available in the water tank.\nThe max amount available to withdraw is {self.__current_water_level_gallons:,} gallons."

    # public method (with one parameter for the gallons of water to add per second) to fill the tank at
    # a certain rate (i.e., gallons per second)
    def fill_water_per_second(self, gallons_to_add_per_second):
        capacity_available_in_tank = self.max_water_capacity_gallons - self.__current_water_level_gallons
        # check if the # of gallons that will fill the tank in a second will not cause the tank to overflow
        if gallons_to_add_per_second <= capacity_available_in_tank:
            self.__current_water_level_gallons += gallons_to_add_per_second
            # return a value of true
            return True
        # if gallons per second added will cause the tank to overflow, do not fill the tank
        else:
            # return a value of false.
            return False

    # public method (with one parameter for the gallons of water to drain per second) to drain the
    # tank at a certain rate (i.e., gallons per second)
    def drain_water_per_second(self, gallons_to_drain_per_second):
        # check if the # of gallons to be drained is <= the current tank water level
        if gallons_to_drain_per_second <= self.__current_water_level_gallons:
            self.__current_water_level_gallons -= gallons_to_drain_per_second
            # return a value of true
            return True
        # if the number of gallons that will drain from the tank in a second is available in the tank, drain the tank. 
        else:
            # return a value of false.
            return False

    # __str__ method that returns relevant information about a water_tank object’s state (i.e.,
    # its attributes and their current values) as a string with appropriate labels and formatting.
    def __str__(self): # TODO
        return f"Tank Radius: {self.radius:} feet\nTank Depth: {self.depth} feet\nMax Capacity: {self.__max_water_capacity_gallons:,} gallons\nCurrent Water Level: {self.__current_water_level_gallons:,} gallons"