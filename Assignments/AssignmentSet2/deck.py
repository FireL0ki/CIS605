# Description: Module that creates a Deck class object & its corresponding attributes & functions
# Developer: Sif Oberon
# Date Created: 9.19.2025
# Date Last Modified: 9.19.2025

class Deck:

    # initialize the Deck object
    def __init__(self, square_footage, cost_per_foot, cost_per_gallon):

        self.__square_footage = square_footage
        self.__cost_per_foot = cost_per_foot
        self.__cost_per_gallon = cost_per_gallon

    # getters to retrieve object values as properties
    @property
    def square_footage(self):
        return self.__square_footage
    
    @property
    def cost_per_foot(self):
        return self.__cost_per_foot
    
    @property
    def cost_per_gallon(self):
        return self.__cost_per_gallon
    
    # define methods calculate costs associated with building
    def calculate_lumber_cost(self):
        lumber_cost = self.square_footage * self.cost_per_foot
        return lumber_cost
    
    def calculate_stain_cost(self):
        FEET_COVERED_BY_GALLON_OF_STAIN = 297
        total_stain_cost = (self.square_footage/FEET_COVERED_BY_GALLON_OF_STAIN) * self.cost_per_gallon
        return total_stain_cost

    def calculate_labor_cost(self):
        # constant
        LABOR_COST_PER_SQUARE_FOOT = 31.25
        labor_cost = self.square_footage * LABOR_COST_PER_SQUARE_FOOT
        return labor_cost
    
    # method to calculate the total building costs
    def calculate_building_cost(self):
        # set the cost variables by calling the methods used to calculate them
        lumber_cost = self.calculate_lumber_cost()
        total_stain_cost = self.calculate_stain_cost()
        labor_cost = self.calculate_labor_cost()

        total_building_cost = lumber_cost + total_stain_cost + labor_cost
        return total_building_cost
    
    # create a str method to display the values of the object's attributes
    def __str__(self):
        return f'The cost of building a {self.square_footage:,} square foot deck with lumber costing ${self.calculate_lumber_cost():,.2f} per square foot and stain costing ${self.cost_per_gallon} per gallon is ${self.calculate_building_cost():,.2f}.'

    