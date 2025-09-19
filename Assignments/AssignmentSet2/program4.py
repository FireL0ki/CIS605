# Description: 
# Developer: Sif Oberon
# Date Created: 9.16.2025
# Date Last Modified: 9.16.2025

# import the investment module
import investment

print('Investment Calculator Program')

def main():
    # get values from a user as inputs & assign to variables

    # get present investment value as user input string, may or may not include commas 
    present_investment_value_input_string = input("Please enter the current value of your investment: ")
    # remove the commas from the user input
    cleaned_investment_value_input = present_investment_value_input_string.replace(",", "")
    # convert to integer
    present_investment_value_int = int(cleaned_investment_value_input)

    # get investment duration as user input and convert to integer
    investment_duration = int(input('Please enter the duration of your investment in years: '))
    # get annual interest rate as user input and convert to float
    annual_interest_rate = float(input('Please enter the annual interest rate: '))

    # create Investment object 
    my_investment = investment.Investment(present_value=present_investment_value_int, investment_duration=investment_duration, annual_interest=annual_interest_rate)

    # print formatted results using __str__ method
    print(my_investment)
 

# call main function to start program
main()