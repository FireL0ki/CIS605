# Description: A class for a projectile object
# Developer: Sif Oberon
# Date Created: 10.28.2025
# Date Last Modified: 11.6.2025

# a Projectile class that has attributes: initial height (private), initial velocity (private), maximum height (private), land time (private)
# Note: Assume the units of measurement for initial height will be feet and initial velocity will be feet per second
class Projectile:
    def __init__(self, initial_height, initial_velocity):
        self.__initial_height = initial_height
        self.__initial_velocity = initial_velocity
        self.__max_height = self.__calc_max_height()
        self.__land_time = self.__calc_land_time()
    
    @property
    def initial_height(self):
        return self.__initial_height
    
    @property
    def initial_velocity(self):
        return self.__initial_velocity

    # private instance method to calculate and returns the height (in feet) of the projectile at a certain
    # time (in seconds) after it has been thrown straight up into the air. Takes time (seconds) as parameter
    def __calc_height_at_time(self, time_in_seconds):
        # formula for calculating the height of a projectile at a certain time (t seconds) after it has been thrown up:
        # initial height + (initial velocity * t) – (16 * t^2)
        height = self.initial_height + (self.initial_velocity * time_in_seconds) - (16 * (time_in_seconds**2))

        return height

    # private instance method to calculate and return the maximum height of the projectile (should use __calc_height_at_time)
    # a projectile will reach its maximum height at initial velocity/32 seconds 
    # (for example, if the initial velocity of the projectile is 100 feet per second, it will reach its maximum
    # height at 100/32 = 3.125 seconds
    def __calc_max_height(self):
        seconds_to_max_height = self.__initial_velocity / 32
        max_height = self.__calc_height_at_time(seconds_to_max_height)
        # round height to two decimal places
        rounded_height = round(max_height, 2)
        return rounded_height
    
    # private instance method to determine and return the approximate time (in seconds) when the
    # projectile will hit the ground (this method should use the method __calc_height_at_time)
    # set up a loop to determine the height of the projectile after every 0.01 second; when
    # the height is no longer a positive number you can assume the projectile has hit the ground.
    def __calc_land_time(self):
        # initialize time variable
        time = 0
        # set up interval amount at .01 second
        interval = .01

        while True:
            # set height to the height calculated at current time given the iteration
            height = self.__calc_height_at_time(time)

            if height <= 0:
                # if the height is at 0 or lower, the object has hit the ground, break out of loop
                break

            # if not, increment time up by .01 seconds, and continue looping
            time += interval

        # round time to two decimal points
        rounded_time = round(time, 2)

        # return time
        return rounded_time

    # __str__ method that returns relevant information about a projectile object’s state 
    def __str__(self):
        return f"Initial Height: {self.initial_height} feet\nInitial Velocity: {self.initial_velocity} feet per second\nMaximum Height: {self.__max_height:,} feet\nLand Time: {self.__land_time} seconds"