# Description: Gets user inputs to fill or drain a water tank
# Developer: Sif Oberon
# Date Created: 10.28.2025
# Date Last Modified: 11.6.2025


# imports the Water_Tank class from the water_tank module
from water_tank import Water_Tank
from sys import exit

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
        while True:
            radius = int(input("Enter a tank radius between 5 and 50: "))
            # check radius is within range, if it is, terminate loop with break
            if 5 <= radius <= 50: break
        while True:
            depth = int(input("Enter a tank depth between 10 and 100: "))
            # check depth is within range
            if 10 <= depth <= 100: break
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
        case 4: fill_water_per_second()
        case 5: drain_water_per_second()
        case 6: create_additional_watertank()
        case 7: exit_application()

# function to get user input (using an appropriate prompt and validation) for the gallons of water to add
# to the tank (int, minimum: 1, maximum: 6,000,000)
def add_water_to_tank():
    try:
        while True:
            gallons_water_to_add = int(input("Enter the number of gallons of water to add (between 1 and 6,000,000): "))
            # if user input is within range, break out of loop
            if 1 <= gallons_water_to_add <= 6000000: break
    except:
        print("Input error")
        add_water_to_tank()
    else:
        # call the method to add water and display the returned message
        print(a_water_tank.add_water_to_tank(gallons_water_to_add))
    # call the function to display the menu
    display_menu()

# function to get user input (using an appropriate prompt and validation) for the gallons of water to
# withdraw from the tank (int, minimum: 1, maximum: 6,000,000)
def withdraw_water_from_tank():
    try:
        while True:
            gallons_water_to_withdraw = int(input("Enter the number of gallons of water to withdraw (between 1 and 6,000,000): "))
            # if user input is within range, break out of loop
            if 1 <= gallons_water_to_withdraw <= 6000000: break
    except:
        print("Input error")
        withdraw_water_from_tank()
    else:
        # call the method to withdraw water and display the returned message
        print(a_water_tank.withdraw_water_from_tank(gallons_water_to_withdraw))
    # call the function to display the menu
    display_menu()

# function get user input (using an appropriate prompt and validation) for the rate (i.e.,
# gallons/second) at which to fill the tank (int, minimum: 1, maximum: 5000)
def fill_water_per_second():
    try:
        while True:
            gallons_to_add_per_second = int(input("Enter the number of gallons of water to fill per second (between 1 and 6,000,000): "))
            # if user input is within range, break out of loop
            if 1 <= gallons_to_add_per_second <= 6000000: break
    except:
        print("Input error")
        fill_water_per_second()
    else:
        # call the method to fill water and display the returned message
        while a_water_tank.fill_water_per_second(gallons_to_add_per_second):
            # print current water level each loop
            print(f"{a_water_tank.current_water_level_gallons:,} gallons")

        # print message to user when tank is full
        print(f"Tank is either full or cannot add another {gallons_to_add_per_second:,} gallons")
    # call the function to display the menu
    display_menu()

# function to get user input (using an appropriate prompt and validation) for the rate (i.e.,
# gallons/second) at which to drain the tank (int, minimum: 1, maximum: 5000)
def drain_water_per_second():
    try:
        while True:
            gallons_to_drain_per_second = int(input("Enter the number of gallons of water to drain per second (between 1 and 6,000,000): "))
            # if user input is within range, break out of loop
            if 1 <= gallons_to_drain_per_second <= 6000000: break
    except:
        print("Input error")
        drain_water_per_second()
    else:
        # call the method to drain water within the body of a loop; to keep things simple, assume
        # each loop iteration takes a second; the loop should execute as long as the method returns
        # a value of true; after each iteration display the current water level of the tank
        while a_water_tank.drain_water_per_second(gallons_to_drain_per_second):
            print(f"{a_water_tank.current_water_level_gallons:,} gallons")
    
    # when loop is finished due to tank capacity, print message to user
    print(f"Tank is either empty or cannot drain another {gallons_to_drain_per_second:,} gallons")

    # call the function to display the menu
    display_menu()


# function to ask the user if they wish to create another water tank object
# b. if yes, call the function that gets input for a water tank object
def create_additional_watertank():
    user_response = input("Would you like to create another water tank object? (Y / N): ")

    if user_response.upper() == "Y":
        get_user_input_for_watertank()
    else:
        # else, call the function to display the menu
        display_menu()

# function to ask the user if they wish to exit the application
def exit_application():
    user_response = input("Would you like to exit the application? (Y / N): ")

    if user_response.upper() == "Y":
        # if yes, exit the application
        exit()
    else:
        # else, call the function to display the menu
        display_menu()

# 21. Calls the “main” function
main()