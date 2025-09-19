# Project:          Module 3 - Example 3
# Description:      Class definition for a food item
# Demonstrates:     Class attributes/properties and methods
# Developed By:     LV
# Date:             September 2025

class Food_Item3:

    # class attributes are common to all objects/instances
    # the double underscores preceding the names mark the attributes as "private" (i.e., accessible only within the class)
    
    __num_food_items = 0
    __total_calories = 0
    
    # an initializer method is typically the first method in a class
    # it executes immediately after an object of the class is created
    
    def __init__(self, food_name, fat_grams, carbs_grams, protein_grams):
        
        self.__name = food_name
        self.__fat = fat_grams
        self.__carbs = carbs_grams
        self.__protein = protein_grams
        self.__calories = self.__calc_calories()

        # call to a class method

        Food_Item3.__increment_totals(self)
                        
    # getters for retrieving object's attribute values as properties

    @property
    def name(self):
        return self.__name
    
    @property
    def fat(self):
        return self.__fat
    
    @property
    def carbs(self):
        return self.__carbs
    
    @property
    def protein(self):
        return self.__protein
    
    @property
    def calories(self):
       return self.__calories
           
    # the double underscores preceding the method name mark the method as "private" (i.e., for use only within the class)

    def __calc_calories(self):
        
        # constants

        FAT_CALORIES_PER_GRAM = 9
        CARBS_PROTEIN_CALORIES_PER_GRAM = 4

        return (self.fat * FAT_CALORIES_PER_GRAM) + ((self.carbs + self.protein) * CARBS_PROTEIN_CALORIES_PER_GRAM)
                     
    # the __str__ method is used to display an object's state (i.e., the current values of an object's attributes)

    def __str__(self):
        return f'{self.name} with {self.fat} grams of fat, {self.carbs} grams of carbs, and {self.protein} grams of protein has {self.calories:,} calories.'
    
    # class methods are common to all object/instances
    # the double underscores preceding a method name mark the method as "private" (i.e., for use only within the class)
    
    @classmethod
    def __increment_totals(cls, self):
        cls.__num_food_items += 1
        cls.__total_calories += self.calories

    @classmethod
    def __calc_average_calories(cls):
        return cls.__total_calories / cls.__num_food_items

    @classmethod
    def summary_info(cls):
        return f'Number of food items: {cls.__num_food_items:,}\nTotal Calories: {cls.__total_calories:,}\nAverage Calories: {cls.__calc_average_calories():,.2f}'