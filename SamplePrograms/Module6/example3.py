# Project:          Module 6 - Example 3
# Description:      Creates scorecard object; calls methods and and prints results             
# Depends on:       scorecard
# Developed By:     LV
# Date:             October 2025

# import scorecard class

from scorecard import Scorecard as sc

# import Python's inspect module

import inspect

# declare a module-level variable

a_card = None

# entry point for program

print('Scorecard by LV')

def main():

   # call function to get data
    
    get_data()
    
# get data for scorecard

def get_data():

    try:

        name = input("Enter the player's name: ")
        
        # declare pars and scores list
        
        pars = []
        scores = []
        
        with open('pars.csv', 'r') as infile: # open the pars.csv in read mode
            line = infile.readline()
            line = line.strip().split(',') #strip any leading or trailing characters, split the line into individual values using "," as the delimiter

        # convert the elements in the line list to int
        # append to pars list

        for item in line:
            pars.append(int(item))

        # or, use list comprehension
             
        # pars = [int(item) for item in line]

        with open('scheffler_scores.csv', 'r') as infile: # open the scheffler_scores.csv in read mode
            lines = infile.readlines()
                
        for line in lines:  #for each line in lines
            line = line.strip().split(',')  #strip any leading or trailing characters, split the line into individual values using "," as the delimiter
            line = [int(item) for item in line] # convert the elements in each line list to int
            scores.append(line) # append the line list to scores list to create a 2-dimensional list (a list of lists)
                   
    except FileNotFoundError as e:
        print(e)

    except ValueError as e:
        print(e)

    except Exception as e:
        print(e)
    
    # call function to create a scorecard object

    create_object(name, pars, scores)

# function to create a scorecard object

def create_object(name, pars, scores):
     
    # to modify the module-level variable, it must be declared as global within the function

    global a_card

    a_card = sc(name, pars, scores)

    # view the object
    
    print(a_card)
    print()

    # call methods on object and print returned values

    call_methods()

# function to call methods on object and print returned values

def call_methods():

   # the getmembers function returns all the members (e.g., attributes, methods) and their names of an object
   
   for name, member in inspect.getmembers(a_card):
      if inspect.ismethod(member) and not name.startswith('__'):    # if the member is a method and it's name does not start with '__"
         print(member())
         print()

# call main function

main()