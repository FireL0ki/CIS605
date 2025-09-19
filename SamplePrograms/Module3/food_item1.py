# Project:          Module 3 - Example 1
# Description:      Class definition for a food item
# Demonstrates:     Data hiding; "private" attributes and "public" properties; gettors and settors; __str__ method
# Developed By:     LV
# Date:             September 2025

class Food_Item1:

    # an initializer method is typically the first method in a class
    # it executes immediately after an object of the class is created
    # it is used to initialize the object's attributes
    # in this example, it is used to initialize the attributes of a food item object
    # an attribute name can be preceded by a single underscore (to indicate the attribute should not be directly accessed from outside the class), or
    # double underscores (to make it difficult to directly access the attribute from outside the class through name mangling)

    def __init__(self, food_name, fat_grams, carbs_grams,protein_grams):
        
        self.__name = food_name
        self.__fat = fat_grams
        self.__carbs = carbs_grams
        self.__protein = protein_grams

    # getters and setters are created to control how attributes that are intended to be "private" can be accessed as "public" properties
    
    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, value):
        self.__name = value

    @property
    def fat(self):
        return self.__fat
    
    @fat.setter
    def fat(self, value):
        self.__fat = value

    @property
    def carbs(self):
        return self.__carbs
    
    @carbs.setter
    def carbs(self, value):
        self.__carbs = value
    
    @property
    def protein(self):
        return self.__protein
    
    @protein.setter
    def protein(self, value):
        self.__protein = value
   
   # calculates and returns the total calories for food item object

    def calc_calories(self):
        
        # constants

        FAT_CALORIES_PER_GRAM = 9
        CARBS_PROTEIN_CALORIES_PER_GRAM = 4
        
        calories = (self.fat * FAT_CALORIES_PER_GRAM) + ((self.carbs + self.protein) * CARBS_PROTEIN_CALORIES_PER_GRAM)

        return calories
    
    # the __str__ method is used to display an object's state (i.e., the current values of an object's attributes)

    def __str__(self):
        return f'{self.name} with {self.fat} grams of fat, {self.carbs} grams of carbs, and {self.protein} grams of protein has {self.calc_calories():,} calories.'