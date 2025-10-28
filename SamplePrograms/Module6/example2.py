# Project:          Module 6 - Example 2
# Description:      Creates stock analyzer object; calls methods and and prints results             
# Depends on:       stock_analyzer
# Developed By:     LV
# Date:             October 2025

# import stock_analyzer class

from stock_analyzer import Stock_Analyzer as sa

# import Python's inspect module

import inspect

# declare a module-level variable

a_stock = None

# entry point for program

print('Stock Analyzer by LV')

def main():

   # call function to read price data from a file into a list
    
    read_data()
    
# read price data from a file into a list

def read_data():

    try:

        with open('nvidia_prices.txt', 'r') as infile: # open the prices.txt in read mode
            prices = infile.readlines() #read all lines from a file and return them as a list of strings
        
        for i in range(len(prices)):
            prices[i] = float(prices[i])

        # alternative to using indices
        # new_prices = []

        # for price in prices:
        #     new_prices.append(float(price))

        # a list comprehension is a concise expression for creating a new list by iterating over the elements of an existing list
        # it can be used instead of a traditional for loop (above)
        # in the list comprehension below, 
        # "float(price)" is the "result expression"
        # "for price in prices" is the "iteration expression"
        # each item in the existing prices list is converted to a float and added to the new prices list
        
        # prices = [float(price) for price in prices]

    except FileNotFoundError as e:
        print(e)

    except ValueError as e:
        print(e)

    except Exception as e:
        print(e)
    
    # call function to create a stock_analyzer object

    create_object(prices)

# function to create a stock_analyzer object

def create_object(prices):
     
    # to modify the module-level variable, it must be declared as global within the function

    global a_stock

    a_stock = sa(prices)

    # view the list by printing the object's stock_prices property
    
    print(a_stock.stock_prices)
    print()

    # call methods on object and print returned values

    call_methods()

# function to call methods on object and print returned values

def call_methods():

   # the getmembers function returns all the members (e.g., attributes, methods) and their names of an object
   
   for name, member in inspect.getmembers(a_stock):
      if inspect.ismethod(member) and not name.startswith('__'):    # if the member is a method and it's name does not start with '__"
         print(member())
         print()

# call main function

main()