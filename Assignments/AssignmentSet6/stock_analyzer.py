
# Description: Stock Analyzer class with methods to calculate differences in stock prices
# Developer: Sif Oberon
# Date Created: 11.17.2025
# Date Last Modified: 11.25.2025

# Stock Analyzer class with initializer to initialize the two instance attributes  (ticker symbol & stock prices) with parameter values
class Stock_Analyzer:
    def __init__(self, ticker_symbol, stock_prices):
        self.ticker_symbol = ticker_symbol
        self.stock_prices = stock_prices

    # public method to find & return the smallest price change (up or down) between 2 consecutive trading days
    # example: for day 1 and day 2, the absolute price change will be abs(day 2 price – day 1 price)
    def find_smallest_price_change(self):
        stock_prices = self.stock_prices
        # set smallest change to the difference between the first two numbers
        smallest_change = abs(stock_prices[1] - stock_prices[0])
        # initialize i at the starting index
        i = 0
        # iterate over the list of stock_prices
        while i < len(stock_prices) - 1:
            # find the difference between the next day index[i + 1] and current day index[i] 
            # use abs() to find the absolute value difference 
            abs_difference = abs(stock_prices[i + 1] - stock_prices[i])
            # check if the new abs_difference is smaller than the previously stored smallest_change
            if abs_difference < smallest_change:
                # if yes, update smallest change using abs_difference
                smallest_change = abs_difference
            # iterate
            i += 1

        return smallest_change

    # public method to find & return the largest percentage gain in price between 2 consecutive trading days.
    # example: for day 1 and day 2, the % change in price will be (day 2 price – day 1 price) / day 1 price.
    def find_largest_consecutive_percentage_gain(self):
        stock_prices = self.stock_prices
        # set largest percentage change to the percentage change between the first two days
        largest_change_percentage = (stock_prices[1] - stock_prices[0]) / stock_prices[0]
        # initialize i at the starting index
        i = 0
        # iterate over the list of stock_prices
        while i < len(stock_prices) - 1:
            # calculate the change percentage between the following day and the current day
            percentage_change = (stock_prices[i + 1] - stock_prices[i]) / stock_prices[i]
            # check if the new percentage_change is smaller than the currently stored largest_change_percentage
            if percentage_change > largest_change_percentage:
                # if yes, update largest change percentage change using percentage_change
                largest_change_percentage = percentage_change
            # iterate
            i += 1
            
        return largest_change_percentage

    # public method to find and return the # of times there is a positive change in price between 2 consecutive trading days
    # example: for day 1 and day 2, there is a positive change in price, if day 2 price is greater
    # than day 1 price.
    def find_number_times_positive_price_change(self):
        stock_prices = self.stock_prices
        # create variable to track number of times there is a positive change
        number_positive_price_changes = 0
        # initialize i at the starting index
        i = 0
        # iterate over the list of stock_prices
        while i < len(stock_prices) - 1:
            # check if the following day is greater than the current index day (positive change)
            if stock_prices[i + 1] > stock_prices[i]:
                # if so, add to number of positive changes count
                number_positive_price_changes += 1
            # iterate
            i += 1
        return number_positive_price_changes

    # public method to find and return the longest period (in days) of continuous price decline
    # example: for day 1 and day 2, there is a decline in price, if day 2 price is less than day 1
    # price.
    def find_longest_continuous_price_decline(self):
        stock_prices = self.stock_prices
        # create variable to track the longest period of continuous price decline
        total_longest_decline = 0
        current_longest_decline = 0
        i = 0
        while i < len(stock_prices) - 1:
            # check if following day index value is less than current day index value
            if stock_prices[i + 1] < stock_prices[i]:
                # if so, add to longest_continous_price_decline variable
                current_longest_decline += 1
            # if following day is not lower than current set current longest decline to 0
            else:
                current_longest_decline = 0
            # check if current longest decline > total longest decline
            if current_longest_decline > total_longest_decline:
                # if so, update total longest to the value of current longest
                total_longest_decline = current_longest_decline
            # move to next iteration of loop
            i += 1
        return total_longest_decline

    # __str__ method that returns relevant information about a stock_analyzer object’s state (i.e., its
    # attributes and their current values) as a string with appropriate labels and formatting
    def __str__(self):
        return f"Ticker Symbols: {self.ticker_symbol}\nPrices: {self.stock_prices}"


