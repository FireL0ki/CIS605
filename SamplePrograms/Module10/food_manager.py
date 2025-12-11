# Project:          Module 10 - Example 1
# Description:      Class definition for a food items manager
# Demonstrates:     Managing objects of a class
# Developed By:     LV
# Date:             November 2025

from food import Food

from food_group import Food_Group as FG

from typing import Union

# objects can be serialized by converting them to a stream of bytes that can be saved to a file
# in Python, serializing objects is called pickling

import pickle

# for checking if a file exists

from pathlib import Path

class Food_Manager:

    # class variable
    # the file, fooddata.dat, will be used to store and retrieve serialized food objects 

    FILENAME: str = "fooddata.dat"
    
    def __init__(self) -> None:
        
        # call load_food_objects method to read data from file
            
        self.load_food_objects()
        
    @property
    def food_dict(self) -> dict[str, Food]:
        return self.__food_dict

    # overloaded method
    
    def add_food(self,*args) -> str:

        # if there is more than 1 argument, create a food object and assign to a_food
        # else, assign the food object (i.e., parameter value) to a_food
        
        if len(args) > 1:
            a_food = Food(*args)
        else:
            a_food = args[0]

        # add food object to the food dictionary as a key value pair

        # the "key" (in this case, the food name) is specified in square brackets
        # the "value" is the food object (i.e., a_food)
        
        self.food_dict[a_food.food_name] = a_food

        return f"Added - {a_food}"

    def get_a_food(self, food_name) -> Union[Food, str]: # can return either a Food object or a string

        # the get method returns the value associated with a specified key
        # if the key is not found, a default value (e.g., a not found message) is returned
        
        return self.food_dict.get(food_name, f"{food_name} not found")
    
    def get_all_food(self) -> str:
    
        result: str = ""
        
        # the values method returns all the values in the dictionary as a sequence of tuples
        
        if len(self.food_dict) > 0:
            for food in self.food_dict.values():
                result += str(food) + "\n"
        else: result = "There are no food items to display"           
        
        return result
    
    # overloaded method

    def get_food_count(self, a_type: Union[str, FG] = "all") -> str:

        # if no parameter value is received, return the count of all items in the food dictionary
        # else, find and return the count of items of a specific food type using a loop or dictionary comprehension
                    
        result: str = ""
        count: int = 0
        
        if a_type == "all":
            count = len(self.food_dict)
            result = f"There is/are {count} food item(s)"
        else:
            # count = 0
            # for a_food in self.food_dict.values:
            #     if a_food.food_type == a_type:
            #         count += 1
                    
            # the items method returns all the keys and their associated values as a sequence of tuples
            
            count = len({name: food.food_name for name, food in self.food_dict.items() if food.food_type == a_type})
           
            result = f"There is/are {count} food item(s) of type: {a_type.name}"
        
        return result
    
    def remove_food(self,food_name: str) -> str:

        # the pop method removes the key value pair from the dictionary and returns the value associated with the key
        # # if the key is not found, a default value (e.g., a not found message) is returned
        
        result: Union[str, Food]

        result = self.food_dict.pop(food_name, f"{food_name} not found")

        if isinstance(result, Food):
            result = f"Removed - {result}"
        
        return result
    
    def clear_all_food(self) -> str:

        # the clear method removes all items in a dictionary
        
        result: str = "There are no food items to clear"
        
        if len(self.food_dict) > 0:
            self.food_dict.clear()
            result = "All food items removed from dictionary"
               
        return result
    
    def get_total_calories(self) -> str:

        result: str = "There are no food items to calculate total calories"
        
        if len(self.food_dict) > 0:
            total_calories = 0
            for a_food in self.food_dict.values():
                total_calories += a_food.calories

            result = f"The total calories of all the food items is: {total_calories:,}"
        
        return result
            
    def get_average_calories(self) -> str:

        result: str = "There are no food items to calculate average calories"
        
        if len(self.food_dict) > 0:
            total_calories: int = 0
            for a_food in self.food_dict.values():
                total_calories += a_food.calories

            result = f"The average calories for all the food items is: {total_calories/len(self.food_dict):,.2f}"
        
        return result   
   
    def get_lowest_calories(self) -> str:

        result: str = "There are no food items to find the lowest calories"
        
        if len(self.food_dict) > 0:
            lowest: int = 10000000
            for a_food in self.food_dict.values():
                if a_food.calories < lowest:
                    lowest = a_food.calories

            result = f"The lowest calories among all the food items is: {lowest:,}"

        return result  
       
        # From Gemini, A Python lambda function is a small, anonymous function defined with the lambda keyword. 
        # It can take any number of arguments but can only have one expression. 
        # The result of this expression is implicitly returned by the lambda function.
        
        # Syntax: lambda arguments : expression

        # a lambda function to square a number
        # square = lambda x: x * x
        # print(square(5))

        # lambdas are frequently used with higher-order functions like map(), filter(), and sorted() where a function is passed as an argument.
        # in the statement below, lambda is used with min() to find the food (in the food dictionary) with the lowest calories 
        
        # return min(self.food_dict.values(), key=lambda food: food.calories)
    
    def load_food_objects(self) -> None:

        # From Gemini

        # A Python dictionary is a built-in data type that stores data in key-value pairs. Dictionaries are ordered, changeable, and do not allow duplicate keys. They are also known as hash maps or associative arrays in other programming languages.

        # Characteristics:
        # Key-Value Pairs: Each item in a dictionary consists of a key and its corresponding value.
        # Ordered: As of Python 3.7, dictionaries maintain insertion order.
        # Changeable (Mutable): You can add, remove, and modify key-value pairs after the dictionary is created.
        # No Duplicate Keys: Each key in a dictionary must be unique. If you try to add an item with an existing key, the old value associated with that key will be overwritten.
        # Keys Must Be Immutable: Dictionary keys must be immutable objects (e.g., strings, numbers, tuples). Values can be of any Python data type.
        
        # if fooddata.dat exists, read (load) data from the file and assign it to a dictionary
        # else, create an empty dictionary
        
        file_path: Path = Path(Food_Manager.FILENAME)

        if file_path.is_file():
            try:      
                with open(Food_Manager.FILENAME, "rb") as infile:
                    self.__food_dict = pickle.load(infile)
            except Exception as e:
                print(e)
        else:       
            self.__food_dict = {}

    def save_food_objects(self) -> str:

        result: str = "No food items to save"
        
        # if there are elements in the food dictionary, write (dump) the data to fooddata.dat
        
        if len(self.food_dict) > 0:
            try:
                with open(Food_Manager.FILENAME, "wb") as outfile:
                    pickle.dump(self.food_dict, outfile)
                    result = "Food items saved"
            except Exception as e:
                    print(e)
        
        return result