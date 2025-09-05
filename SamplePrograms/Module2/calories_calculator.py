# Project:          Module 2 - Program 1
# Description:      Functions to calculate calories for a food item
# Developed By:     LV
# Date:             August 2025

 # global constants

FAT_CALORIES_PER_GRAM = 9
CARBS_PROTEIN_CALORIES_PER_GRAM = 4

# calculates and returns the total calories for a food item based on its macronutrients

def calc_total_calories(fat_grams, carbs_grams, protein_grams):
   
    # calculate and return total calories for food item
    
    total_calories = (fat_grams * FAT_CALORIES_PER_GRAM) + ((carbs_grams + protein_grams) * CARBS_PROTEIN_CALORIES_PER_GRAM)

    return total_calories

# calculates and returns the calories from fat for a food item and its contribution to total calories

def calc_fat_calories(fat_grams, carbs_grams, protein_grams):
    
    fat_calories = fat_grams * FAT_CALORIES_PER_GRAM

    total_calories = calc_total_calories(fat_grams, carbs_grams, protein_grams)

    fat_calories_percentage = fat_calories / total_calories

    return fat_calories, fat_calories_percentage

# can create functions similar to above for carbs and protein

# calculates and returns the calories of a food item as a proportion of daily calories intake goal

def calc_calories_to_goal(fat_grams, carbs_grams, protein_grams, calories_goal=2000):
    
    total_calories = calc_total_calories(fat_grams, carbs_grams, protein_grams)

    calories_to_goal = total_calories / calories_goal

    return calories_to_goal