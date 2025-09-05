# Project:          Module 2 - Program 2
# Description:      Gets the macronutrients for a food item and daily calories intake goal as user input
#                   Creates a food item object; calls methods of the food item object, and prints the returned values             
# Depends on:       food_item
# Developed By:     LV
# Date:             August 2025

import food_item as fi # import the food_item class (module)

#get user inputs, convert to integers and assign to variables

print('Calories Calculator for a Food Item by LV')

grams_of_fat = int(input("Enter the fat grams for food item: "))

grams_of_carbs = int(input("Enter the carbs grams for food item: "))

grams_of_protein = int(input("Enter the protein grams for food item: "))

calories_goal = int(input("Enter your daily calories intake goal: "))

# create a food item object and initialize its data attributes

my_food_item = fi.Food_Item(grams_of_fat,grams_of_carbs,grams_of_protein)

# call methods on food item object and assign returned values to variables

total_calories = my_food_item.calc_total_calories()

fat_calories, fat_percentage = my_food_item.calc_fat_calories()

calories_to_goal = my_food_item.calc_calories_to_goal(calories_goal)

# format and print results

print(f'The total calories for food item with fat grams of {my_food_item.fat:,}, carbs grams of {my_food_item.carbs:,}, and protein grams of {grams_of_protein:,} is {total_calories:,}')

print(f'The fat calories for food item with fat grams of {my_food_item.fat:,} is {fat_calories:,} and the fat calories as a percentage of total calories is {fat_percentage:,.2%}')

print(f'The total calories for food item as a percentage of daily calories intake is {calories_to_goal:,.2%}')