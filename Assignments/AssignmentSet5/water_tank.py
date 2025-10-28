# Create a module (water_tank) for a class (Water_Tank) that has 4 instance attributes:
# o radius (private), depth (private), current water level in gallons (private, getter), maximum water capacity in gallons (private)
# Note: Assume radius and depth measurements will be in feet
# 2. An initializer to
# o initialize the radius and height attributes with parameter values, o initialize the current water level attribute to 0
# o set the maximum water capacity attribute by calling the instance method below

# import libraries
import math

# Water_Tank class with 
class water_Tank:
    def __init__(self, radius, depth, current_water_level_gallons, max_water_capacity_gallons):
        self.__radius = radius
        self.__depth = depth
        self.__current_water_level_gallons = current_water_level_gallons
        self.__max_water_capacity_gallons = max_water_capacity_gallons
    
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
    capacity_available_in_tank = self.max_water_capacity_gallons - self.current_water_level_gallons
    # check if water_added is less than capacity left in tank
    if gallons_water_to_add <= capacity_available_in_tank:
        self.current_water_level_gallons += gallons_water_to_add
        # return an appropriate message a) confirming the gallons of water added, and b) the tank’s current water level
        return f"{gallons_water_to_add} were added to the tank. The tank's water level is now: {self.current_water_level_gallons}."
    
    elif gallons_water_to_add > capacity_available_in_tank:
        # return message indicating the tank will overflow, current water level, & maximum available capacity
        return f"Adding {gallons_water_to_add} gallons to the tank will cause the tank to overflow. The tank's current water level is {self.current_water_level_gallons}. The maximum number of gallons that can be added is: {capacity_available_in_tank}."

# public method (with one parameter for the gallons of water to withdraw) to withdraw water from the tank
def withdraw_water_from_tank(self, gallons_water_to_withdraw):
    # if the number of gallons to be withdrawn is available in the tank, withdraw the water from the tank. 
    
    # return message confirming gallons water withdrawn, tank's current water level

    # if the number of gallons to be withdrawn exceeds what the tank currently contains, do not withdraw the water
    # return message a) indicating not enough water, and b) the max # of gallons that can be withdrawn from the tank 
    # (i.e., the tank’s current water level).

# • A public method (with one parameter for the gallons of water to add per second) to fill the tank at
# a certain rate (i.e., gallons per second)
# o If the number of gallons that will fill the tank in a second will not cause the tank to
# overflow, fill the tank. Return a value of true.
# o If the number of gallons that will fill the tank in a second will cause the tank to overflow,
# do not fill the tank. Return a value of false.

# • A public method (with one parameter for the gallons of water to drain per second) to drain the
# tank at a certain rate (i.e., gallons per second)
# o If the number of gallons that will drain from the tank in a second is available in the tank,
# drain the tank. Return a value of true.
# o If the number of gallons that will drain from the tank in a second is not available in the
# tank, do not drain the tank. Return a value of false.

# 6. A __str__ method that returns relevant information about a water_tank object’s state (i.e.,
# its attributes and their current values) as a string with appropriate labels and formatting.