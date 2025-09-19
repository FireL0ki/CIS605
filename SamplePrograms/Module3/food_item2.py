squ# Project:          Module 3 - Example 2
# Description:      Class definition for a food item
# Demonstrates:     "Private" method
# Developed By:     LV
# Date:             September 2025

class Food_Item2:

    # an initializer method is typically the first method in a class
    # it executes immediately after an object of the class is created
    
    def __init__(self, food_name, fat_grams, carbs_grams, protein_grams):
        
        self.name = food_name
        self.fat = fat_grams
        self.carbs = carbs_grams
        self.protein = protein_grams
                        
    # the getter for the calories property is used to call the private method __calc_total_calories

    @property
    def calories(self):
       return self.__calc_calories()
           
    # the double underscores that precede the method name marks the method as "private" (i.e., for use only within the class)

    def __calc_calories(self):
        
        # constants

        FAT_CALORIES_PER_GRAM = 9
        CARBS_PROTEIN_CALORIES_PER_GRAM = 4
        
        return (self.fat * FAT_CALORIES_PER_GRAM) + ((self.carbs + self.protein) * CARBS_PROTEIN_CALORIES_PER_GRAM)

        
    # the __str__ method is used to display an object's state (i.e., the current values of an object's attributes)

    def __str__(self):
        return f'{self.name} with {self.fat} grams of fat, {self.carbs} grams of carbs, and {self.protein} grams of protein has {self.calories:,} calories.'