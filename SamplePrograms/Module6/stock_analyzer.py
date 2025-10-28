# Project:          Module 6 - Example 2
# Description:      Class definition for Stock Analyzer
# Demonstrates:     Lists
# Developed By:     LV
# Date:             October 2025

# import the statistics and math modules

import statistics as stat
import math

class Stock_Analyzer:

    # initializer

    def __init__(self, prices):
        
        self.stock_prices = prices
        
    # instance methods to demo list processing and functions

    # find minimum price

    def find_minimum_price(self):

        return f"The minimum price is ${min(self.stock_prices):.2f}"    # min function returns the smallest item in the list 
    
    # find maximum price
    
    def find_maximum_price(self):

        return f"The maximum price is ${max(self.stock_prices):.2f}"    # max function returns the largest item in the list
    
    # calculate average price manually

    def calc_average_price1(self):

        average_price = sum(self.stock_prices) / len(self.stock_prices) # sum function returns the sum of numeric items in the list

        return f"The average price (manual) is ${average_price:.2f}"
    
    # calculate average price using the statistics module

    def calc_average_price2(self):

       average_price = stat.mean(self.stock_prices)
       
       return f"The average price (statistics) is ${average_price:.2f}"
    
    # find median price manually

    def find_median_price1(self):

        median_price = 0.0
       
       # create a copy of the stock_prices list

        sorted_prices = [] + self.stock_prices

        # sort the copy - rearrange the prices in ascending order

        sorted_prices.sort()

        # find the number of elements

        num_elements = len(sorted_prices)
        
        # if the number of elements in the list is even
        # the median is the average of the middle two prices
        # if the number of elements in the list is odd
        # it is the midddle price
        
        if num_elements % 2 == 0:
            median_price = (sorted_prices[num_elements // 2] + sorted_prices[num_elements // 2 - 1]) / 2
        else:
            median_price = sorted_prices[num_elements // 2]

        return f"The median price (manual) is ${median_price:.2f}"
    
    # find median price using the statistics module

    def find_median_price2(self):

        median_price = stat.median(self.stock_prices)
        
        return f"The median price (statistics) is ${median_price:.2f}"

    # calculate sample standard deviation of the prices manually

    def calc_standard_deviation1(self):

        # calculate the average price

        average_price = sum(self.stock_prices) / len(self.stock_prices)

        # squared_deviations = []

        # for price in self.stock_prices:
        #     squared_deviations.append(price - average_price) ** 2

        # the above "for loop" can be rewritten using list comprehension

        # List comprehension - from Gemini

        # Is a concise and efficient way to create new lists based on existing iterables (like lists, tuples, or strings). 
        # It provides a more compact and often more readable alternative to traditional for loops for list creation and manipulation.
        # The basic syntax of a list comprehension is:

        # new_list = [expression for item in iterable if condition]

        # expression: This defines what value will be added to the new_list for each item. It can be the item itself, a modification of the item, or a result of a function call on the item.
        # for item in iterable: This is the core iteration part, similar to a for loop. It iterates through each item in the iterable.
        # if condition (optional): This is a conditional filter. If present, only items for which the condition evaluates to True will be processed by the expression and included in the new_list.
        
        squared_deviations = [(price - average_price) ** 2 for price in self.stock_prices]

        # (price - average_price) ** 2 is the "expression"; the difference between price and average price is squared
        # for price in self.stock_prices is the "for item in iterable" 

        # calculate variance

        variance = sum(squared_deviations) / (len(self.stock_prices) - 1)

        # calculate standard deviation

        standard_deviation = math.sqrt(variance)
        
        return f"The standard deviation of the prices (manual) is ${standard_deviation:.2f}"
    
    # calculate sample standard deviation of the prices using the statistics module

    def calc_standard_deviation2(self):

        # calculate standard deviation

        standard_deviation = stat.stdev(self.stock_prices)
        
        return f"The standard deviation of the prices (statistics) is ${standard_deviation:.2f}"