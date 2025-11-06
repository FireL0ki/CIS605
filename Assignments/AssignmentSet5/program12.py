# Description: Program to get user inputs to determine height & velocity of a projectile
# Developer: Sif Oberon
# Date Created: 10.28.2025
# Date Last Modified: 11.6.2025

# import Projectile class from the projectile module
from projectile import Projectile
from sys import exit


# declare module level variable (for referencing a projectile object) initialized to “None”
a_projectile = None

def main():
    # print header for the program
    print('Projectile Calculation Program')
    # call function that gets input for a projectile object
    get_user_projectile_inputs()

# get user inputs using prompts & vaidation for a projectile object
def get_user_projectile_inputs():
    try: 
        while True:
            #  projectile object initial height – int, minimum: 1, maximum: 15;
            initial_height = int(input("Enter an initial heigh for the projectile between 1 and 15: "))
            # if the initial_height is correctly within range, break out of the loop
            if 1 <= initial_height <= 15: break
        
        while True:
            # initial velocity – int, minimum: 10, maximum:500
            initial_velocity = int(input("Enter an initial velocity between 10 and 500 feet per second: "))
            # check if the initial_velocity is within range
            if 10 <= initial_velocity <= 500: break

    # if user inputs are not within range, print an error statement & re-run method to get corrected numbers
    except:
        print("Input Error")
        get_user_projectile_inputs()
    # if inputs are correctly within range, create the projectile object
    else:
        create_projectile_object(initial_height, initial_velocity)

def create_projectile_object(height, velocity):
    # access module level variable using global key word
    global a_projectile

    a_projectile = Projectile(initial_height=height, initial_velocity=velocity)
    # call the function to display the projectile object’s state 
    print_projectile_object()
    # call a function to check if the user wishes to enter input for another projectile
    check_for_additional_projectiles()

# function to print the projectile object’s state
def print_projectile_object():
    print(a_projectile)

# function to check if user would like to add additional projectiles
def check_for_additional_projectiles():
    # ask the user if they wish to create another projectile object
    create_additional_projectile = input("Do you wish to create another projectile (Y or N)?: ")
    #  if yes, call the function that gets input for a projectile object
    if create_additional_projectile.upper() == "Y":
        get_user_projectile_inputs()
    # if no, exit the application
    elif create_additional_projectile.upper() == "N":
        print("Program End.")
        exit()

main()

