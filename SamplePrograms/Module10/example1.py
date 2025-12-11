# Project:          Module 10 - Example 1
# Description:      Creates food manager object; calls methods and prints results             
# Depends on:       food_group, food_manager, food
# Developed By:     LV
# Date:             November 2025

from food_group import Food_Group as FG
from food import Food
from food_manager import Food_Manager as FM

import sys
import re

# declare a module-level variable

a_manager: FM = None

# entry point for program

print('Food Manager by LV')

def main() -> None:

   # call function to instantiate food manager object
    
    create_food_manager_object()

# function to create a food manager object

def create_food_manager_object() -> None:

    global a_manager

    a_manager = FM()

    display_menu()
    
# function to display a menu of options

def display_menu() -> None:

    print("\n---- Menu ----")
    print("1 - Add food")
    print("2 - Display a food")
    print("3 - Display all food")
    print("4 - How many food?")
    print("5 - How many food of a type?")
    print("6 - Remove a food")
    print("7 - Remove all food")
    print("8 - Display total calories")
    print("9 - Display average calories")
    print("10 - Display lowest calories")
    print("11 - Save food items")
    print("12 - Exit")

    try:
        while True:
            
            selection: int = int(input("Enter your choice (1-12): "))

            if 1 <= selection <= 12: break 
    except:
        print("Input Error")
        display_menu()
    else:
        print()
        call_function(selection)

# function to call the appropriate function

def call_function(choice: int) -> None:

    match choice:
        case 1: get_food_data()
        case 2: display_a_food()
        case 3: display_all_food()
        case 4: food_count()
        case 5: food_count_of_type()
        case 6: remove_a_food()
        case 7: remove_all_food()
        case 8: total_calories()
        case 9: average_calories()
        case 10: lowest_calories()
        case 11: save_food()
        case 12: exit_app()

# function to get inputs for a food object

def get_food_data() -> None:

    try:

        while True:

            food_name: str = input("Enter food name (letters, spaces and hyphens only): ").strip()

            if re.match(r"^[A-Za-z]+([ -][A-Za-z]+)*$", food_name): break
        
        while True:

            food_type_num: int = int(input("Enter 1-6 for the food's group (1-Grains, 2-Vegetable, 3-Fruit, 4-Protein, 5-Dairy, 6-Sweet): "))
           
            if 1 <= food_type_num <= 6: break

        while True:

            fat_grams: int = int(input("Enter the fat content in grams (0-500): "))
           
            if 0 <= fat_grams <= 500: break

        while True:

            carbs_grams: int = int(input("Enter the carbs content in grams (0-500): "))
           
            if 0 <= carbs_grams <= 500: break

        while True:

            protein_grams: int = int(input("Enter the protein content in grams (0-500): "))
           
            if 0 <= protein_grams <= 500: break

    except:
        print("Input Error")
        get_food_data()
    else:
        create_add_food_object(food_name, food_type_num, fat_grams, carbs_grams, protein_grams)

# function to create and add a food object

def create_add_food_object(name: str, type_num: int, fat: int, carbs: int, protein: int) -> None:

    # assign appropriate enumeration member
    
    food_type: FG = FG(type_num)
    
    print()

    # create and add food object
    
    a_food: Food = Food(name, food_type, fat, carbs, protein)

    print(a_manager.add_food(a_food))

    # or, pass food data to the overloaded add_food method to create and add food object
    
    # print(a_manager.add_food(name, food_type, fat, carbs, protein))

    display_menu()
    
# function to display a food object

def display_a_food() -> None:
   try:
        food_name: str = input("Enter food name: ").strip()
   except:
        print("Input Error")
        display_a_food()
   else:
        print()
        print(a_manager.get_a_food(food_name))
        display_menu()

# function to display all food objects

def display_all_food() -> None:
   
   print()
   print(a_manager.get_all_food())

   display_menu()
   
# function to display the number of food objects

def food_count() -> None:
    
    print()
    print(a_manager.get_food_count())

    display_menu()

# function to display the number of food objects of a specific type

def food_count_of_type() -> None:
   
   try:
        while True:

            type_num: int = int(input("Enter 1-6 for the food's group (1-Grains, 2-Vegetable, 3-Fruit, 4-Protein, 5-Dairy, 6-Sweet): "))
           
            if 1 <= type_num <= 6: break
   except:
        print("Input Error")
        food_count_of_type()
   else:
        
        # assign appropriate enumeration member
    
        food_type: FG = FG(type_num)
    
        print()
        print(a_manager.get_food_count(food_type))

        display_menu()
 
# function to remove a food item

def remove_a_food() -> None:
    
    try:
       food_name: str = input("Enter food name: ").strip()
    except:
        print("Input Error")
        remove_a_food()
    else:
        print()
        print(a_manager.remove_food(food_name))
        display_menu()

# function to remove all food items

def remove_all_food() -> None:
    
    print()
    print(a_manager.clear_all_food())
    display_menu()

# function to get total calories

def total_calories() -> None:
    
    print()
    print(a_manager.get_total_calories())
    display_menu()

# function to get average calories

def average_calories() -> None:
    
    print()
    print(a_manager.get_average_calories())
    display_menu()

# function to get lowest calories

def lowest_calories() -> None:
    
    print()
    print(a_manager.get_lowest_calories())
    display_menu()

# function to save the food objects to a file

def save_food() -> None:
    
    save: str = input('Do you wish to save the food items to a file (Y or N)?: ')

    if save.upper() == "Y":
        print()
        print(a_manager.save_food_objects())
   
    display_menu()

def exit_app() -> None:
    
    exit: str = input('Do you wish to exit the application (Y or N)?: ')

    if exit.upper() == "Y":
        sys.exit()
    else:
        display_menu()

main()