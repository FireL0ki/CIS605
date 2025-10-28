# Project:          Module 7 - Example 1
# Description:      Creates bank account or cd account object, calls methods, and prints results             
# Depends on:       bank_account, cd_account
# Developed By:     LV
# Date:             October 2025

import sys

# import parent and child classes

from bank_account import Bank_Account as ba
from cd_account import CD_Account as ca

import re # import the regular expression module for validating user input with pattern matching

# declare a module-level variable

an_account = None

# entry point for program

def main():

    print("Bank/CD Account by LV")
    
    # call function to display menu
    
    display_menu()

# function to display a menu of options

def display_menu():

    print("\n---- Menu ----")
    print("1 - Create Bank/CD account")
    print("2 - Make a deposit")
    print("3 - Make a withdrawl")
    print("4 - Calculate number of days to CD maturity")
    print("5 - Display account information")
    print("6 - Exit the application")

    try:
        while True:
            
            selection = int(input("Enter your choice (1-6): "))

            if 1 <= selection <= 6: break 
    except:
        print("Input Error")
        display_menu()
    else:
        print()
        call_function(selection)

# function to call the appropriate function

def call_function(choice):

        match choice:
            case 1: check_account_type()    # check account type to be created prior to calling the function to get user input
            case 2: make_deposit()
            case 3: make_withdrawl()
            case 4: check_maturity()
            case 5: print_object()
            case 6: exit_app()

# function to check if user wishes to create an ordinary bank account or CD account

def check_account_type():

    try:
        
        while True:
            
            account_type = input('Do you wish to open an ordinary bank account or CD account (R or CD)?: ').upper()
            
            if account_type in ("R", "CD"): break 
    except:
        print("Input Error")
        display_menu()
    else:
        print()
        get_user_inputs(account_type)

# function to get user inputs for ordinary or CD account
        
def get_user_inputs(acct_type):
    
    try:

        while True:

            cust_name = input("Enter the customer's name (letters, spaces and hyphens only): ").strip()

            if re.match(r"^[A-Za-z]+([ -][A-Za-z]+)*$", cust_name): break # validation using regular expression
            
            # https://www.w3schools.com/python/python_regex.asp
    
        while True:
            
            amount = int(input("Enter an initial deposit amount between $100 and $100,000: "))

            if 100 <= amount <= 100000: break 

        # if it's a CD account, get two more inputs
        
        if acct_type == "CD":

            while True:

                cd_rate = float(input("Enter the interest rate on the CD (1.00 to 8.00): "))

                if 1 <= cd_rate <= 8: break
    
            while True:
            
                duration = int(input("Enter the duration of the CD in months (3 to 60): "))

                if 3 <= duration <= 60: break 
    
    except:
        print("Input Error")
        get_user_inputs(acct_type)
    else:
        # call the create_object function with either 2 (for ordinary bank account) or 4 (for CD account) of arguments
        create_object(cust_name, amount, cd_rate, duration) if acct_type == "CD" else create_object(cust_name, amount)

# function to create an object

# Python does not explicitly support method/function overloading 
# (i.e., having multiple methods/functions with the same name but different set of parameters)
# One way to get around this limitation is to have a method/function accept a variable number of positional arguments

# the *args syntax indicates that the variable number of positional arguments passed to this function is collected as a single tuple

def create_object(*args):
     
    global an_account

    # if the number of arguments is 2)

    if len(args) == 2:
        
        # the * operator "unpacks" the tuple and calls the __init__ method with either 2 (for a bank account) or 4 arguments (for a CD account)
        
        an_account = ba(*args)
        
        # alternatively, an_account = ba(args[0], args[1])  
    
    else:
        
        an_account = ca(*args)
        
        # alternatively, an_account = ca(args[0], args[1], args[2], args[3])  
    
    display_menu()

# function to make a deposit

def make_deposit():

    # if the object has been instantiated
    
    if an_account is not None: 
    
        try:
            while True:
                
                amount = int(input("Enter the amount you would like to deposit (1-100000): "))

                if 1 <= amount <= 100000: break
        except:
            print("Input Error")
            make_deposit()

        print(an_account.deposit(amount))  
            
    else:
        print("Please create an account first")
    
    display_menu()

#function to make a withdrawl

def make_withdrawl():
     
    # if the object has been instantiated
    
    if an_account is not None: 
    
        try:
            while True:
                        
                amount = int(input("Enter the amount you would like to withdraw (1-100000): "))

                if 1 <= amount <= 100000: break
        except:
            print("Input Error")
            make_withdrawl()

        print(an_account.withdraw(amount))  
            
    else:
        print("Please create an account first")
       
    display_menu()

# function to check maturity date for a CD account

def check_maturity():

    # if object is a CD Account

    if isinstance(an_account, ca):
        print(an_account.calc_days_to_maturity())

    else:
        print("Please create a CD account first")
        
    display_menu()

# function to display object information

def print_object():

    # if the object has been instantiated
    
    if an_account is not None: 
        print(an_account)
    else:
        print("Please create an account first")
       
    display_menu()

# function to check if user wishes to exit the application

def exit_app():

    exit = input('Do you wish to exit the application (Y or N)?: ')

    if exit.upper() == "Y":
        sys.exit()
    else:
        display_menu()

main()
