# Description: A module that calculates the future value of a user's investment based on their inputs
# Developer: Sif Oberon
# Date Created: 9.16.2025
# Date Last Modified: 9.19.2025

import futurevalue_calculator

# get present investment value as user input string, may or may not include commas 
present_investment_value_input_string = input('Please enter the current value of your investment: ')
# remove the commas from the user input
cleaned_investment_value_input = present_investment_value_input_string.replace(",", "")
# convert to integer
present_investment_value_int = int(cleaned_investment_value_input)

# get investment duration as user input and convert to integer
investment_duration = int(input('Please enter the duration of your investment in years: '))
# get annual interest rate as user input and convert to float
annual_interest_rate = float(input('Please enter the annual interest rate: '))

# set future_value variable to the result of calling the futurevalue_calculator with the user inputs as parameters
future_value = futurevalue_calculator.calc_futurevalue(present_investment_value=present_investment_value_int, investment_duration=investment_duration, annual_interest_rate=annual_interest_rate)

# print statement to show user the result of the calculation that shows the future value of their investment based on their inputs
print(f'The future value of an investment of ${present_investment_value_int:,.2f} for a duration of {investment_duration} year(s) at an interest rate of {annual_interest_rate:.2f}% is ${future_value:,.2f}.')
