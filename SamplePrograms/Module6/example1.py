# Project:          Module 6 - Example 1
# Description:      Creates lotto ticket object; calls methods and and prints results             
# Depends on:       lotto_ticket
# Developed By:     LV
# Date:             October 2025

# import Lotto_Ticcket class

from lotto_ticket import Lotto_Ticket as lt

# import Python's inspect module

import inspect

# declare a module-level variable

a_ticket = None

# entry point for program

print('Lotto Ticket Numbers Generator by LV')

def main():

   # call function to create object
    
    create_object()
    
# function to create a lotto_ticket object

def create_object():
     
    # to modify the module-level variable, it must be declared as global within the function

    global a_ticket

    a_ticket = lt()

    # call methods on object and print returned values

    call_methods()

# function to call methods on object and print returned values

def call_methods():

   # the getmembers function returns all the members (e.g., attributes, methods) and their names of an object
   
   for name, member in inspect.getmembers(a_ticket):
      if inspect.ismethod(member) and not name.startswith('__'):    # if the member is a method and it's name does not start with "__"
         print(member())

# call main function

main()

# loop to call the methods again

while True:

    another = input("Would you like to call the methods again (Enter Y for Yes): ")
    
    if another.upper() == "Y": # if "Y", call the call_methods function
        call_methods()
    else:
        break # terminate loop and program