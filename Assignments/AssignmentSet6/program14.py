# Description: Program that makes use of the Stock Analyzer class to provide stock analysis to user
# Developer: Sif Oberon
# Date Created: 11.17.2025
# Date Last Modified: 11.25.2025

from stock_analyzer import Stock_Analyzer

# module level variable
a_stock_analyzer = None

def main():
    print(f"Stock Analyzer Program")
    get_user_stock_analysis_input()

# function to get user input (using an appropriate prompt and validation) for a stock analyzer object
def get_user_stock_analysis_input():
    try:
        while True:
            # ticker symbol – str, 1 to 5 letters
            ticker_symbol = input("Enter the stock's ticker symbol (1-5 characters): ")
            if len(ticker_symbol) > 0 and len(ticker_symbol) < 6: break
    except:
        print("Input error.")
        get_user_stock_analysis_input()
    else: 
        # capitalize and assign the input value to a variable
        capitalized_ticker_symbol = ticker_symbol.capitalize()
    
        # open the arm_prices.txt file, read, convert, and append the data to a list
        stock_prices_list = []
        try:
            # open arm_prices.txt & read (r)
            with open('arm_prices.txt', 'r') as infile:
                # read lines from the file and return as a list of strings
                prices = infile.readlines()
                # iterate over the lines in the file, putting the prices into a list
                for price in prices:
                    # add prices to the price list and strip white space
                    stock_prices_list.append(float(price.strip()))
        # error handling
        except FileNotFoundError as e:
            print(e)
        except ValueError as e:
            print(e)
        except Exception as e:
            print(e)

        # call the function that creates/instantiates a stock analyzer object
        create_stock_analyzer_object(capitalized_ticker_symbol, stock_prices_list)

# function to create a stock analyzer object and assign it to the module level variable
def create_stock_analyzer_object(ticker_symbol, stock_prices):
    # modify module level variable - must be declared as a global within the function
    global a_stock_analyzer
    # create object
    a_stock_analyzer = Stock_Analyzer(ticker_symbol, stock_prices)
    # call the function to display a menu
    display_menu()

# function to display the menu options
def display_menu():
    print("\n--------- Menu ---------")
    print("1) Display stock analyzer object’s state")
    print("2) Smallest absolute price change")
    print("3) Largest percentage gain in price")
    print("4) Number of times positive change in price")
    print("5) Longest price decline streak")
    print("6) Exit the application")
    
    # get the user’s choice (i.e., 1-6) with an appropriate prompt and validation
    try:
        while True:
            user_selection = int(input("Enter your choice (1-6): "))
            if 1 <= user_selection <= 6:
                break
    except:
        print("Input error")
    # call function that calls the function associated with the user’s menu choice
    call_menu_function(user_selection)

def call_menu_function(user_selection):
    match user_selection:
        case 1: print_stock_analyzer_state()
        case 2: find_smallest_absolute_price_change()
        case 3: find_largest_percentage_price_gain()
        case 4: find_number_times_positive_price_change()
        case 5: find_longest_consecutive_price_decline()
        case 6: exit_application()

# function to print stock analyzer object state
def print_stock_analyzer_state():
    print(a_stock_analyzer)
    
    # call function to display menu
    display_menu()

# function to call the method that finds the smallest absolute price change and display the returned
# value with appropriate wording and formatting
def find_smallest_absolute_price_change():
    smallest_price_change = a_stock_analyzer.find_smallest_price_change()
    print(f"The smallest absolute price change between two consecutive trading days is: {smallest_price_change}")
    # call the function to display the menu
    display_menu()

# function to call the method that finds the largest percentage gain in price and display the returned
# value with appropriate wording and formatting
def find_largest_percentage_price_gain():
    largest_percentage_gain = a_stock_analyzer.find_largest_consecutive_percentage_gain()
    print(f"The largest percentage gain between two consecutive trading days is: {largest_percentage_gain}")
    # call the function to display the menu
    display_menu()

# function to call the method that finds the number of times there is a positive change in price and
# display the returned value with appropriate wording and formatting
def find_number_times_positive_price_change():
    number_times_pos_change = a_stock_analyzer.find_number_times_positive_price_change()
    print(f"The number of times there is a positive change in price is: {number_times_pos_change}")
    # call the function to display the menu
    display_menu()

# function to call the method that finds the longest price decline streak and display the returned value
# with appropriate wording and formatting
def find_longest_consecutive_price_decline():
    longest_price_decline = a_stock_analyzer.find_longest_continuous_price_decline()
    print(f"The longest period of continuous price decline is {longest_price_decline} days")
    # call the function to display the menu
    display_menu()

# function to ask the user if they wish to exit the application
def exit_application():
    user_response = input("Would you like to exit the application? (Y / N): ")

    if user_response.upper() == "Y":
        # if yes, exit the application
        exit()
    else:
        # else, call the function to display the menu
        display_menu()

# call the “main” function
main()



