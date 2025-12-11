# Project:          Module 10 - Example 1
# Description:      Class definition for a food item
# Demonstrates:     Managing objects of a class
# Developed By:     LV
# Date:             November 2025

from food_group import Food_Group as FG

# From Gemini

# Python type hints are annotations that allow developers to indicate the expected data types of variables, function arguments, and return values. While Python remains a dynamically typed language and type hints are not enforced at runtime by the interpreter, they provide significant benefits for code clarity, maintainability, and error detection. 

# Syntax: Type hints are added using colons (:) after variable names or function arguments, and an arrow (->) for function return types.

    # def greet(name: str) -> str:
    #     return f"Hello, {name}!"

    # age: int = 30

# Benefits:

# Improved Readability: Type hints explicitly declare intended types, making code easier to understand for both the original developer and others.
# Enhanced Maintainability: Clear type information simplifies refactoring and debugging, as the expected data flow is readily apparent.
# IDE Support: Integrated Development Environments (IDEs) use type hints to offer better autocompletion, parameter suggestions, and early error detection, improving the development experience.
# Better Software Design: Explicitly defining types encourages a more structured approach to software design, leading to cleaner and more robust code.

class Food:
       
    def __init__(self, food_name: str, food_type: FG, fat_grams: int, carbs_grams: int, protein_grams: int) -> None:
        
        self.food_name = food_name
        self.fat = fat_grams
        self.carbs = carbs_grams
        self.protein = protein_grams
        self.food_type = food_type
                                
    @property
    def calories(self) -> int:
        return self.__calc_calories()
    
    def __calc_calories(self) -> int:
        
        # constants

        FAT_CALORIES_PER_GRAM: int = 9
        CARBS_PROTEIN_CALORIES_PER_GRAM: int = 4

        return (self.fat * FAT_CALORIES_PER_GRAM) + ((self.carbs + self.protein) * CARBS_PROTEIN_CALORIES_PER_GRAM)
                     
    def __str__(self) -> str:
        
        return f'Food Name: {self.food_name} Food Type: {self.food_type.name} Fat Grams: {self.fat} Carbs Grams: {self.carbs} Protein Grams: {self.protein} Calories: {self.calories:,}'