# Project:          Module 6 - Example 1
# Description:      Class definition for Lotto Ticket
# Demonstrates:     Lists
# Developed By:     LV
# Date:             October 2025

# Python List - From Gemini

# Built-in, ordered, and mutable collection data type used to store multiple items in a single variable. 
# Lists are highly versatile and can contain elements of various data types, including integers, strings, booleans, and even other lists.
# 
# Key characteristics of Python lists:

# Ordered: Elements maintain the order in which they are added.
# Mutable: Elements can be modified, added, or removed after the list is created.
# Index-based: Elements are accessed using zero-based integer indices (e.g., my_list[0] for the first element).
# Heterogeneous: Lists can store elements of different data types within the same list.
# Dynamic: Lists can grow or shrink in size as elements are added or removed.

# import random module from Python's standard library

import random as rm

class Lotto_Ticket:

    # initializer

    def __init__(self):
        pass
        
    # instance methods to demo variations in creating lists

    # populating a list with randomly generated numbers using a while loop

    def pick_numbers1(self):

        # declare an empty list

        random_numbers = []

        NUM_NUMBERS = 6

        while len(random_numbers) < NUM_NUMBERS:   # len function returns the number of items in the list
            
            random_numbers.append(rm.randint(1, 40))    # randint function generates a random integer within a range; append function adds an item to a list
           
        random_numbers.sort()   # sort method rearranges the list elements in ascending order
        
        return random_numbers
    
     # populating a list with randomly generated numbers using a for loop
    
    def pick_numbers2(self):

        # the repetition operator, "*" is used to create copies of a list and join them together
        
        random_numbers = [0] * 6    # creates the following list: [0,0,0,0,0,0]

        for index in range(len(random_numbers)):
            
            # list elements can be accessed using an index number; the index of the first element is 0; the index of the last element is 1 less than the number of elements in the list
           
            random_numbers[index] = rm.randint(1, 40)   

        random_numbers.sort()

        return random_numbers
    
    # populating a list with randomly generated numbers that are unique

    def pick_numbers3(self):

        # declare an empty list

        random_numbers = []

        NUM_NUMBERS = 6

        while len(random_numbers) < NUM_NUMBERS:
            aNumber = rm.randint(1,40)
            if aNumber not in random_numbers:   # add the number if it is not already in the list (to avoid having duplicate numbers in the list)
                random_numbers.append(aNumber)
           
        random_numbers.sort()
        
        return random_numbers
    
    # populating a list with randomly generated numbers that are unique using the sample function

    def pick_numbers4(self):

       random_numbers = rm.sample(range(1,41),6)    # the sample function is used to generate 6 unique numbers between the range 1 and 40
        
       random_numbers.sort()
        
       return random_numbers