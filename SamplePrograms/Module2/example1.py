# Project:          Module 2 - Program 1
# Description:      Gets the macronutrients for a food item and daily calories intake goal as user input
#                   Calls functions in the calories_calculator module and prints the returned values             
# Depends on:       calories_calculator
# Developed By:     LV
# Date:             August 2025

import calories_calculator as cc # import the calories_calculator module

#get user inputs, convert to integers and assign to variables

print('Calories Calculator for a Food Item by LV')

grams_of_fat = int(input("Enter the fat grams for food item: "))

grams_of_carbs = int(input("Enter the carbs grams for food item: "))

grams_of_protein = int(input("Enter the protein grams for food item: "))

calories_goal = int(input("Enter your daily calories intake goal: "))

# call functions in calc_calories module and assign returned values to variables

total_calories = cc.calc_total_calories(grams_of_fat,grams_of_carbs,grams_of_protein) 

fat_calories, fat_percentage = cc.calc_fat_calories(grams_of_fat,grams_of_carbs,grams_of_protein)

calories_to_goal = cc.calc_calories_to_goal(grams_of_fat,grams_of_carbs,grams_of_protein,calories_goal)

# format and print results

print(f'The total calories for food item with fat grams of {grams_of_fat:,}, carbs grams of {grams_of_carbs:,}, and protein grams of {grams_of_protein:,} is {total_calories:,}')

print(f'The fat calories for food item with fat grams of {grams_of_fat:,} is {fat_calories:,} and the fat calories as a percentage of total calories is {fat_percentage:,.2%}')

print(f'The total calories for food item as a percentage of daily calories intake is {calories_to_goal:,.2%}')