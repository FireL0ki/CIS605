# Description: A class for a projectile object
# Developer: Sif Oberon
# Date Created: 10.28.2025
# Date Last Modified: 10.29.2025

# Create a module (projectile) for a Projectile class that has
# 1. 4 instance attributes
# a. initial height (private)
# b. initial velocity (private)
# c. maximum height (private)
# d. land time (private)
# Note: Assume the units of measurement for initial height will be feet and initial velocity will be
# feet per second
class Projectile:
    def __init__(self, initial_height, initial_velocity, max_height, land_time):
        self.__initial_height = initial_height
        self.__initial_velocity = initial_velocity
        self.__max_height = self.__calc_max_height()
        self.__land_time = self.__calc_land_time()

# b. set the maximum height attribute by calling the appropriate method (#4)
# c. set the land time attribute by calling the appropriate method (#5)

# 3. A private instance method to calculate and returns the height (in feet) of the projectile at a certain
# time (in seconds) after it has been thrown straight up into the air.
# b. the method should receive the time (in seconds) as a parameter
def __calc_height_at_time(self, time_in_seconds):
    # formula for calculating the height of a projectile at a certain time (t seconds) after it has been thrown up:
    # initial height + (initial velocity * t) – (16 * t^2)
    height = self.initial_height + (self.initial_velocity * time_in_seconds) - (16 * (time_in_seconds**2))

    return height
    # ex: if initial height of the projectile is 6 feet and its initial velocity is 100 feet / second
    # the height of the projectile at 3 seconds after it is thrown up would be:
    # 6 + (100 *3) – (16 * 3^2) = 162 feet


# private instance method to calculate and return the maximum height of the projectile
# a. this method should use the method described in #3
def __calc_max_height(self):
# b. a projectile will reach its maximum height at initial velocity/32 seconds (for example, if
# the initial velocity of the projectile is 100 feet per second, it will reach its maximum
# height at 100/32 = 3.125 seconds
# 5. A private instance method to determine and return the approximate time (in seconds) when the
# projectile will hit the ground
# a. this method should use the method described in #3
# b. hint: set up a loop to determine the height of the projectile after every 0.01 second; when
# the height is no longer a positive number you can assume the projectile has hit the
# ground.
# 6. A __str__ method that returns relevant information about a projectile object’s state (i.e.,
# its attributes and their current values) as a string with appropriate labels and formatting.
