# Project:          Module 4 - Example 1
# Description:      Gets user input for a loan application
#                   Creates a loan application object; calls methods on the object, and prints its state             
# Depends on:       loan_application
# Developed By:     LV
# Date:             September 2025

# import Loan_Application class

from loan_application import Loan_Application as la

# declare a module-level variable

my_application = None

# entry point for program

def main():

    print('Loan Application by LV')

    # call function to get user inputs
    
    get_user_inputs()
    
# function to get user inputs and assign to variables

def get_user_inputs():
    
    app_name = input("Enter the applicant's name: ")

    app_income = int(input("Enter the applicant's income: "))

    app_debt = int(input("Enter the applicant's debt: "))

    loan_type = input("Enter the purpose (Auto or Home) for the loan: ")

    # call function to create loan application object

    create_object(app_name, app_income, app_debt, loan_type)

# function to create a loan application object

def create_object(name,income,debt,type):
     
    # to modify the module_level variable, it must be declared as global within the function

    global my_application

    my_application = la(name,income,debt,type)

    # call method to print the object's state

    print_object()

    # call function to invoke methods on object

    invoke_object_methods()

# function to print the loan application object's state

def print_object():

    print(my_application)

# function to invoke methods on the loan application object and print results

def invoke_object_methods():

    print(my_application.check_pre_qualification())
    print(my_application.is_pre_approved())
    print(my_application.determine_interest_rate())
    print(my_application.ascertain_interest_rate())

    # call function to check if user wishes to modify loan application details

    modify_object()

# function to check if user wishes to modify loan application details

def modify_object():
    
    modify = input('Do you wish to modify loan details? Enter Y or N: ')

    if modify.upper() == "Y":

        # call method to update loan object

        update_object()

# function to get new inputs and update loan object

def update_object():
   
    # get inputs to update the loan application object
    # for each input, if the user enters a value, update the appropriate attribute of the loan application object
    
    # new_income = input("Enter the applicant's income: ")

    # if new_income != "": my_application.applicant_income = int(new_income)

    # the code above can be written more concisely using the walrus operator ":="
    # the walrus operator assigns a value to a variable and simultaneously returns the value
    # the assignment expression with the walrus operator can be used to simultaneously assign a value to a variable and evaluate the value 
       
    if (new_income := (input("Enter the applicant's income: "))) != "": my_application.applicant_income = int(new_income)

    if (new_debt := (input("Enter the applicant's debt: "))) != "": my_application.applicant_debt = int(new_debt)

    if (new_type := input("Enter the purpose (Auto or Home) for the loan: ")) != "": my_application.loan_type = new_type

     # call method to print the object's state

    print_object()

    # call function to invoke methods on object

    invoke_object_methods()

# call main function 

main()