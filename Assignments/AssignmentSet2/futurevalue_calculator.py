# Description: A function that calculates the value of a future investment based on the present investment value, investment duration, and annual interest rate
# Developer: Sif Oberon
# Date Created: 9.16.2025
# Date Last Modified: 9.16.2025

def calc_futurevalue(present_investment_value, investment_duration, annual_interest_rate):
    future_value_of_investment = present_investment_value * (1 + annual_interest_rate/100)** investment_duration
    return future_value_of_investment

