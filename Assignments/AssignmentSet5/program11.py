# Description: Gets user inputs to fill or drain a water tank
# Developer: Sif Oberon
# Date Created: 10.28.2025
# Date Last Modified: 10.31.2025


# imports the Water_Tank class from the water_tank module
from water_tank import Water_Tank

# declare a module level variable (for referencing a water tank object) initialized to “None”
a_water_tank = None

def main():
    # print header for the program
    print("Water Tank Program")
    # call function that gets input for a water tank object
    get_user_input_for_watertank()

# function to get user input (with prompts & validation) for a water tank object 
# (radius – int, minimum: 5, maximum: 50; depth – int, minimum: 10, maximum: 100)
def get_user_input_for_watertank():
    try:
        # always true
        while True:
            radius = input(int("Enter a tank radius between 5 and 50: "))
            # check radius is within range, if it is, terminate loop with break
            if radius >= 50 and radius >= 5: break
        while True:
            depth = input(int("Enter a tank depth between 10 and 100: "))
            # check depth is within range
            if depth >= 100 and depth >= 10: break

    except:
        print("Input Error")
        # run get use inputs again to get correct values
        get_user_input_for_watertank()
    
    # if values are within range, create the water tank object
    else:
        create_watertank_object(radius, depth)

# function to create a watertank object
def create_watertank_object(radius, depth):
    # modify module level variable - must be declared as a global within the function
    global a_water_tank
    # create object
    a_water_tank = Water_Tank(radius, depth)
    # call method to print watertank object's state
    print_watertank_object()

# function to print the watertank object's state
def print_watertank_object():
    print(a_water_tank)
    # call function to display the menu
    display_menu()
    
# function to display the menu to user
def display_menu():
    print("\n--------- Menu ---------")
    print("1) Display water tank state")
    print("2) Add water to tank")
    print("3) Withdraw water from tank")
    print("4) Fill water tank")
    print("5) Drain water tank")
    print("6) Enter inputs for another water tank")
    print("7) Exit the application")
    
    try:
        while True:
            user_selection = int(input("Enter our choice (1-7): "))
            if 1 <= user_selection <= 7: break
    except:
        print("Input error")
        # call method to get user selection
        call_menu_function(user_selection)

# method to call appropriate function based on user selection
def call_menu_function(user_selection):
    match user_selection:
        case 1: print_watertank_object()
        case 2: add_water_to_tank()
        case 3: withdraw_water_from_tank()
        case 4: Water_Tank.fill_water_per_second()
        case 5: Water_Tank.drain_water_per_second()
        case 6: get_user_input_for_watertank()
        case 7: exit_program()

def exit_program():
    print("Program complete")

# function to get user input (using an appropriate prompt and validation) for the gallons of water to add
# to the tank (int, minimum: 1, maximum: 6,000,000)
def add_water_to_tank():
    try:
        while True:
            gallons_water_to_add = input(int("Enter the number of gallons of water to add (between 1 and 6,000,000): "))
            # if user input is within range, break out of loop
            if 1 <= gallons_water_to_add <= 6000000: break
    except:
        print("Input error")
        add_water_to_tank()
    else:
        # call the method to add water and display the returned message
        print(a_water_tank.add_water_to_tank())
    # call the function to display the menu
    display_menu()

# function to get user input (using an appropriate prompt and validation) for the gallons of water to
# withdraw from the tank (int, minimum: 1, maximum: 6,000,000)
def withdraw_water_from_tank():
    try:
        while True:
            gallons_water_to_withdraw = input(int("Enter the number of gallons of water to withdraw (between 1 and 6,000,000): "))
            # if user input is within range, break out of loop
            if 1 <= gallons_water_to_withdraw <= 6000000: break
    except:
        print("Input error")
        withdraw_water_from_tank()
    else:
        # call the method to add water and display the returned message
        print(a_water_tank.withdraw_water_from_tank())
    # call the function to display the menu
    display_menu()

# function get user input (using an appropriate prompt and validation) for the rate (i.e.,
# gallons/second) at which to fill the tank (int, minimum: 1, maximum: 5000)
def fill_water_per_second():
    try:
        while True:
            gallons_to_add_per_second = input(int("Enter the number of gallons of water to fill per second (between 1 and 6,000,000): "))
            # if user input is within range, break out of loop
            if 1 <= gallons_to_add_per_second <= 6000000: break
    except:
        print("Input error")
        fill_water_per_second()
    else:
        # call the method to add water and display the returned message
        print(a_water_tank.fill_water_per_second())
    # call the function to display the menu
    display_menu()

# b. call the method to fill water within the body of a loop; to keep things simple, assume each
# loop iteration takes a second; the loop should execute as long as the method returns a
# value of true; after each iteration display the current water level of the tank
# c. call the function (#6) to display the menu

# 18. Has a function to
# a. get user input (using an appropriate prompt and validation) for the rate (i.e.,
# gallons/second) at which to drain the tank (int, minimum: 1, maximum: 5000)
# b. call the method to drain water within the body of a loop; to keep things simple, assume
# each loop iteration takes a second; the loop should execute as long as the method returns
# a value of true; after each iteration display the current water level of the tank
# c. call the function (#6) to display the menu

# 19. Has a function to
# a. ask the user if they wish to create another water tank object
# b. if yes, call the function (#4) that gets input for a water tank object
# c. else, call the function (#6) to display the menu

# 20. Has a function to
# a. ask the user if they wish to exit the application
# b. if yes, exit the application (hint: import the sys module and use the exit function)
# c. else, call the function (#6) to display the menu

# 21. Calls the “main” function
main()


# TODO sample output
# Water Tank By LV
# Enter a radius between 5 and 50 feet: 10
# Enter a depth between 10 and 100 feet: 20
# ---- Menu ----
# 1 - Display water tank's state
# 2 - Add water to tank
# 3 - Withdraw water from tank
# 4 - Fill water tank
# 5 - Drain water tank
# 6 - Enter inputs for another water tank
# 7 - Exit the application
# Enter your choice (1-7): 1
# Tank radius: 10 feet
# Tank depth: 20 feet
# Max capacity: 46,998 gallons
# Current water level: 0 gallons
# ---- Menu ----
# 1 - Display water tank's state
# 2 - Add water to tank
# 3 - Withdraw water from tank
# 4 - Fill water tank
# 5 - Drain water tank
# 6 - Enter inputs for another water tank
# 7 - Exit the application
# Enter your choice (1-7): 2
# Enter the gallons of water to add to the tank (1-6,000,000): 20000
# 20,000 gallons of water added
# Current water level of tank: 20,000 gallons
# ---- Menu ----
# 1 - Display water tank's state
# 2 - Add water to tank
# 3 - Withdraw water from tank
# 4 - Fill water tank
# 5 - Drain water tank
# 6 - Enter inputs for another water tank
# 7 - Exit the application
# Enter your choice (1-7): 3
# Enter the gallons of water to withdraw from the tank (1-6,000,000): 10000
# 10,000 gallons of water withdrawn
# Current water level of tank: 10,000 gallons
# ---- Menu ----
# 1 - Display water tank's state
# 2 - Add water to tank
# 3 - Withdraw water from tank
# 4 - Fill water tank
# 5 - Drain water tank
# 6 - Enter inputs for another water tank
# 7 - Exit the application
# Enter your choice (1-7): 4
# Enter the rate (gallons of water/second) to fill the tank (1-5,000): 1000
# 11,000 gallons
# 12,000 gallons
# 13,000 gallons
# 14,000 gallons
# 15,000 gallons
# 16,000 gallons
# 17,000 gallons
# 18,000 gallons
# 19,000 gallons
# 20,000 gallons
# 21,000 gallons
# 22,000 gallons
# 23,000 gallons
# 24,000 gallons
# 25,000 gallons
# 26,000 gallons
# 27,000 gallons
# 28,000 gallons
# 29,000 gallons
# 30,000 gallons
# 31,000 gallons
# 32,000 gallons
# 33,000 gallons
# 34,000 gallons
# 35,000 gallons
# 36,000 gallons
# 37,000 gallons
# 38,000 gallons
# 39,000 gallons
# 40,000 gallons
# 41,000 gallons
# 42,000 gallons
# 43,000 gallons
# 44,000 gallons
# 45,000 gallons
# 46,000 gallons
# Tank is either full or cannot add another 1,000 gallons
# ---- Menu ----
# 1 - Display water tank's state
# 2 - Add water to tank
# 3 - Withdraw water from tank
# 4 - Fill water tank
# 5 - Drain water tank
# 6 - Enter inputs for another water tank
# 7 - Exit the application
# Enter your choice (1-7): 1
# Tank radius: 10 feet
# Tank depth: 20 feet
# Max capacity: 46,998 gallons
# Current water level: 46,000 gallons
# ---- Menu ----
# 1 - Display water tank's state
# 2 - Add water to tank
# 3 - Withdraw water from tank
# 4 - Fill water tank
# 5 - Drain water tank
# 6 - Enter inputs for another water tank
# 7 - Exit the application
# Enter your choice (1-7): 5
# Enter the rate (gallons of water/second) at which to drain the tank (1-5,000): 1000
# 45,000 gallons
# 44,000 gallons
# 43,000 gallons
# 42,000 gallons
# 41,000 gallons
# 40,000 gallons
# 39,000 gallons
# 38,000 gallons
# 37,000 gallons
# 36,000 gallons
# 35,000 gallons
# 34,000 gallons
# 33,000 gallons
# 32,000 gallons
# 31,000 gallons
# 30,000 gallons
# 29,000 gallons
# 28,000 gallons
# 27,000 gallons
# 26,000 gallons
# 25,000 gallons
# 24,000 gallons
# 23,000 gallons
# 22,000 gallons
# 21,000 gallons
# 20,000 gallons
# 19,000 gallons
# 18,000 gallons
# 17,000 gallons
# 16,000 gallons
# 15,000 gallons
# 14,000 gallons
# 13,000 gallons
# 12,000 gallons
# 11,000 gallons
# 10,000 gallons
# 9,000 gallons
# 8,000 gallons
# 7,000 gallons
# 6,000 gallons
# 5,000 gallons
# 4,000 gallons
# 3,000 gallons
# 2,000 gallons
# 1,000 gallons
# 0 gallons
# Tank is either empty or cannot drain another 1,000 gallons
# ---- Menu ----
# 1 - Display water tank's state
# 2 - Add water to tank
# 3 - Withdraw water from tank
# 4 - Fill water tank
# 5 - Drain water tank
# 6 - Enter inputs for another water tank
# 7 - Exit the application
# Enter your choice (1-7): 1
# Tank radius: 10 feet
# Tank depth: 20 feet
# Max capacity: 46,998 gallons
# Current water level: 0 gallons
# ---- Menu ----
# 1 - Display water tank's state
# 2 - Add water to tank
# 3 - Withdraw water from tank
# 4 - Fill water tank
# 5 - Drain water tank
# 6 - Enter inputs for another water tank
# 7 - Exit the application
# Enter your choice (1-7): 6
# Do you wish to create another water tank (Y or N)?: n
# ---- Menu ----
# 1 - Display water tank's state
# 2 - Add water to tank
# 3 - Withdraw water from tank
# 4 - Fill water tank
# 5 - Drain water tank
# 6 - Enter inputs for another water tank
# 7 - Exit the application
# Enter your choice (1-7): 7
# Do you wish to exit the application (Y or N)?: y

