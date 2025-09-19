# Project:          Module 3 - Example 2
# Description:      Gets the macronutrients for a food item and daily calories intake goal as user input
#                   Creates a food item object; prints its state             
# Depends on:       food_item2
# Developed By:     LV
# Date:             September 2025

import food_item2 as fi # import the food_item class (module)

#get user inputs, convert to integers and assign to variables

print('Calories Calculator for a Food Item by LV')

food_name = input("The food item's name: ")

grams_of_fat = int(input("Enter the fat grams for food item: "))

grams_of_carbs = int(input("Enter the carbs grams for food item: "))

grams_of_protein = int(input("Enter the protein grams for food item: "))

# create a food item object and initialize its data attributes

my_food_item = fi.Food_Item2(food_name,grams_of_fat,grams_of_carbs,grams_of_protein)

# print the object's state

print(my_food_item)