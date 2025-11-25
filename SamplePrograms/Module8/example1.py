# Project:          Module 7 - Example 1
# Description:      Creates tennis champions object; calls methods and prints results             
# Depends on:       tennis_champions
# Developed By:     LV
# Date:             October 2025

# import Tennis_Champions class

from tennis_champions import Tennis_Champions as tc

import sys

# declare a module-level variable

champions = None

# entry point for program

print('Tennis Champions by LV')

def main():

   # call function to read data from files into lists
    
    read_data()
    
# read data from files into lists

def read_data():

    try:

        with open('WimbledonChampions.txt', 'r') as infile:
            lines = infile.readlines()
        
        wimbledon_champs = [item.strip() for item in lines]
        
        with open('USOpenChampions.txt', 'r') as infile:
            lines = infile.readlines()

        us_open_champs = [item.strip() for item in lines]
    
    except FileNotFoundError as e:
        print(e)

    except ValueError as e:
        print(e)

    except Exception as e:
        print(e)
    
    # call function to create a tennis champions object

    create_object(wimbledon_champs, us_open_champs)

# function to create a tennis champions object

def create_object(w_champs, us_champs):
     
    global champions

    champions = tc(w_champs, us_champs)

    display_menu()
    
# function to display a menu of options

def display_menu():

    print("\n---- Menu ----")
    print("1 - Common Set Functions and Methods")
    print("2 - Set Union")
    print("3 - Set Intersection")
    print("4 - Set Difference")
    print("5 - Set Symmetric Difference")
    print("6 - Set Supersets and Subsets")
    print("7 - Set Comprehension")
    print("8 - Exit")

    try:
        while True:
            
            selection = int(input("Enter your choice (1-8): "))

            if 1 <= selection <= 8: break 
    except:
        print("Input Error")
        display_menu()
    else:
        print()
        call_function(selection)

def call_function(choice):

    match choice:
        case 1: common()
        case 2: set_union()
        case 3: set_intersection()
        case 4: set_difference()
        case 5: set_symmetric_difference()
        case 6: set_super_sub()
        case 7: set_comprehension()
        case 8: exit_app()

def common():

    champions.common_functions_methods()

    display_menu()

def set_union():
    
    champions.find_union()

    display_menu()

def set_intersection():
    
    champions.find_intersection()

    display_menu()

def set_difference():

    champions.find_difference()

    display_menu()

def set_symmetric_difference():

    champions.find_symmetric_difference()

    display_menu()

def set_super_sub():

    champions.find_super_sub_sets()

    display_menu()

def set_comprehension():

    champions.set_comprehension()

    display_menu()

def exit_app():

    exit = input('Do you wish to exit the application (Y or N)?: ')

    if exit.upper() == "Y":
        sys.exit()
    else:
        display_menu()

# call main function

main()