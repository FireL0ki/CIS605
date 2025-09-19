# Project:          Module 3 - Example 1
# Description:      Gets the macronutrients for a food item and daily calories intake goal as user input
#                   Creates a food item object; calls methods of the food item object, and prints the returned values             
# Depends on:       food_item1
# Developed By:     LV
# Date:             September 2025

import food_item1 as fi # import the food_item class (module)

#get user inputs, convert to integers and assign to variables

print('Calories Calculator for a Food Item by LV')

food_name = input("The food item's name: ")

grams_of_fat = int(input("Enter the fat grams for food item: "))

grams_of_carbs = int(input("Enter the carbs grams for food item: "))

grams_of_protein = int(input("Enter the protein grams for food item: "))

# create a food item object and initialize its data attributes

my_food_item = fi.Food_Item1(food_name,grams_of_fat,grams_of_carbs,grams_of_protein)

# call method on food item object and assign returned values to variable

calories = my_food_item.calc_calories()

# format and print result

print(f'The total calories for food item {my_food_item.name} is {calories:,}')

# print the object's state

print(my_food_item)