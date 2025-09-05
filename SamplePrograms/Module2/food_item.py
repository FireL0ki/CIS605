# Project:          Module 2 - Program 2
# Description:      Class definition for a food item
# Demonstrates:     Object-Oriented Programming 
#                   Contrasts OO approach to procedural programming
# Developed By:     LV
# Date:             August 2025

class Food_Item:

    # global constants

    FAT_CALORIES_PER_GRAM = 9
    CARBS_PROTEIN_CALORIES_PER_GRAM = 4

    # an initializer method is typically the first method in a class
    # it executes immediately after an object of the class is created
    # it is used to initialize the object's data attributes
    # in this example, it is used to initialize the data attributes of a food item object

    def __init__(self, fat_grams, carbs_grams,protein_grams):
        
        self.fat = fat_grams
        self.carbs = carbs_grams
        self.protein = protein_grams

    # calculates and returns the total calories for food item object

    def calc_total_calories(self):
        
        total_calories = (self.fat * Food_Item.FAT_CALORIES_PER_GRAM) + ((self.carbs + self.protein) * Food_Item.CARBS_PROTEIN_CALORIES_PER_GRAM)

        return total_calories

    # calculates and returns the calories from fat for food item object and its contribution to total calories

    def calc_fat_calories(self):
        
        fat_calories = self.fat * Food_Item.FAT_CALORIES_PER_GRAM

        total_calories = self.calc_total_calories()

        fat_calories_percentage = fat_calories / total_calories

        return fat_calories, fat_calories_percentage

    # can create methods similar to above for carbs and protein
    
    # calculates and returns the calories for food item object as a proportion of daily calories intake goal

    def calc_calories_to_goal(self, calories_goal=2000):
        
        total_calories = self.calc_total_calories()

        calories_to_goal = total_calories / calories_goal

        return calories_to_goal