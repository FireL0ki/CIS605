# Project:          Module 3 - Example 3
# Description:      Gets the macronutrients for a food item and daily calories intake goal as user input
#                   Creates a food item object; prints its state & summary information for all food item objects             
# Depends on:       food_item3
# Developed By:     LV
# Date:             September 2025

# import a specific element (i.e., the Food_Item3 class) instead of the entire module

from food_item3 import Food_Item3 as fi

print('Calories Calculator for a Food Item by LV')

def main():

    # get user inputs, convert to integers and assign to variables

    food_name = input("The food item's name: ")

    grams_of_fat = int(input("Enter the fat grams for food item: "))

    grams_of_carbs = int(input("Enter the carbs grams for food item: "))

    grams_of_protein = int(input("Enter the protein grams for food item: "))

    # create a food item object and initialize its data attributes

    my_food_item = fi(food_name,grams_of_fat,grams_of_carbs,grams_of_protein)

    # print the object's state

    print(my_food_item)

    # print summary information

    print(fi.summary_info())

# call main function 

main()

# call main function to check if summary info is correctly updated
# later, we'll use a loop instead of repeating code

main()