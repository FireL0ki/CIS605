
# Description: 
# Developer: Sif Oberon
# Date Created: 11.17.2025
# Date Last Modified: 


# Stock Analyzer class with initializer to initialize the two instance attributes  (ticker symbol & stock prices) with parameter values
class Stock_Analyzer:
    def __init__(self, ticker_symbol, stock_prices):
        self.ticker_symbol = ticker_symbol
        self.stock_prices = stock_prices


    # public method to find and return the smallest price change (up or down) between two consecutive trading days
    # o Example, for day 1 and day 2, the absolute price change will be abs(day 2 price – day 1 price)
    def find_smallest_price_change(self):
        # loop through the all of the trading
        
        pass


    # public method to find and return the largest percentage gain in price between two consecutive trading days.
    # o Example, for day 1 and day 2, the percentage change in price will be (day 2 price – day 1
    # price) / day 1 price.
    def find_largest_price_change(self):
        pass

    # public method to find and return the number of times there is a positive change in price
    # between two consecutive trading days.
    # o Example, for day 1 and day 2, there is a positive change in price, if day 2 price is greater
    # than day 1 price.
    def find_number_times_positive_price_change(self):
        pass

    # public method to find and return the longest period (in days) of continuous price decline.
    # o Example, for day 1 and day 2, there is a decline in price, if day 2 price is less than day 1
    # price.
    def find_longest_continuous_price_decline(self):
        pass

    # 7. A __str__ method that returns relevant information about a stock_analyzer object’s state (i.e., its
    # attributes and their current values) as a string with appropriate labels and formatting.
    def __str__(self): # TODO
        return f"Prices between"


