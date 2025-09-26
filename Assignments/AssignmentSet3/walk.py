# Description: 
# Developer: Sif Oberon
# Date Created: 9.26.2025
# Date Last Modified:

# Create a module (walk.py) for a class (Walk) that has


class Walk:
    # initializer & 3 private attributes: walker’s name, wumber of steps, length of typical step
    def __init__(self, walker_name, number_steps, step_length):
        self.__walker_name = walker_name
        self.__number_steps = number_steps
        self.__step_length = step_length

    # a getter and setter for each attribute
    @property
    def walker_name(self):
        return self.__walker_name
    
    @walker_name.setter
    def walker_name(self, value):
        self.__walker_name = value
    
    @property
    def number_steps(self):
        return self.__number_steps

    @number_steps.setter
    def number_steps(self, value):
        self.__number_steps = value
    
    @property
    def step_length(self):
        return self.__step_length

    @step_length.setter
    def step_length(self, value):
        self.__step_length = value


    # A public instance method to calculate and return the miles walked
    # miles walked = (number of steps * length of typical step) / 63360
    def calc_miles_walked(self):
        miles_walked = (self.number_steps * self.step_length) / 63360
        return miles_walked
    
    def __str__(self):
        return f'If you walked {self.number_steps} steps & have a step length of {self.step_length}, your miles walked would be: {self.calc_miles_walked()}'



