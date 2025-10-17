# Project:          Module 5 - Example 1
# Description:      Gets user input for one or more investments using a loop
#                   Creates investment object; and prints its state             
# Depends on:       investment
# Developed By:     LV
# Date:             September 2025

# import Investment class

from investment import Investment as inv

# declare a module-level variable

an_investment = None

# entry point for program

print('Investment Calculator by LV')

def main():

   # call function to get user inputs

    get_user_inputs()
    
# function to get and check user inputs, and assign to variables

def get_user_inputs():
    
    try:

        while True:

            inv_amount = int(input("Enter an investment amount between $1,000 and $1,000,000: "))

            # check if amount is within the intended range; if it is, terminate the loop with the break statement
            
            if inv_amount >= 1000 and inv_amount <= 1000000: break 
    
        while True:
            
            inv_period = int(input("Enter the investment period (12 to 120 months): "))
            
            if inv_period >= 12 and inv_period <= 120: break

        while True:

            inv_rate = float(input("Enter the investment rate percentage (1 to 50): " ))
            
            if inv_rate >= 1 and inv_rate <= 50: break
    except:
        print("Input Error")
        get_user_inputs()
    else:
        # call function to create investment object

        create_object(inv_amount, inv_period, inv_rate)

# function to create an investment object

def create_object(amount, period, rate):
     
    # to modify the module-level variable, it must be declared as global within the function

    global an_investment

    an_investment = inv(amount, period, rate)

    # call method to print the object's state

    print_object()

# function to print the investment object's state

def print_object():

    print(an_investment)

# call main function

main()

# loop to continue creating more investments

while True:

    another = input("Would you like to enter another investment (Enter Y for Yes): ")
    
    if another.upper() == "Y": # if "Y", call main function
        main()
    else:
        break # terminate loop and program