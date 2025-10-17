# Project:          In-class Exercise 1
# Purpose:          Practice for Selection Statements
# Developed By:     LV
# Date:             September 2025

# Write a function (with a parameter for package weight) that determines and returns the shipping charge based on the weight of a package.
# <= 2 pounds: $2.25 per pound
# > 2 and <= 6 pounds: $3.50 per pound
# > 6 and <= 10 pounds: $4.75 per pound
# > 10 pounds: $5 per pound

def calc_shipping_charge(package_weight):
    price_per_pound = 0

    if package_weight <= 2:
        price_per_pound = 2.25
    elif package_weight <= 6:
        price_per_pound = 3.50
    elif package_weight <= 10:
        price_per_pound = 4.75
    else:
        price_per_pound = 5
    
    shipping_charge = package_weight * price_per_pound
    
    return shipping_charge


# Write a function (with a parameter for roulette number) that returns the color of a number on a roulette wheel. The colors of the pockets are follows:
# 0: Green
# 1-10: odd numbers are red; even numbers are black
# 11-18: odd numbers are black; even numbers are red
# 19-28: odd numbers are red; even numbers are black
# 29-36: odd numbers are black; even numbers are red
# < 0 or > 36: Invalid number

def determine_roulette_color(roulette_number):
    if roulette_number < 0 or roulette_number > 36:
        color = "invalid"
    elif roulette_number == 0:
        color = "green"
    elif (roulette_number <= 10):
        color = "black" if odd_number(roulette_number) else "red"
    elif (roulette_number <= 18):
        color = "red" if odd_number(roulette_number) else "black"
    elif (roulette_number <= 28):
        color = "black" if odd_number(roulette_number) else "red"
    elif (roulette_number <= 36):
        color = "red" if odd_number(roulette_number) else "black"

    return color
    
# create function to determine if roulette number is odd
def odd_number(roulette_number):
    return False if (roulette_number % 2) == 0 else True
  

# Write a function (with a parameter for number of seconds) that prints:
# the number of seconds if number < 60
# the number of minutes and seconds if number < 3,600
# the number of hours, minutes and seconds if number < 86,400
# the number of days, hours, minutes, and seconds if number >= 86,400
def convert_from_seconds(seconds):
    if seconds < 60:
        print(f'Number of seconds: {seconds}')
        return seconds
    elif seconds < 3600:
        minutes = seconds // 60
        # then use remainder to get the remaining seconds
        remainder_seconds = seconds % 60
        return minutes, remainder_seconds

    elif seconds < 86400:
        hours = seconds // 3600
        remainder = seconds % 60
        minutes = remainder // 60
        seconds = remainder % 60
        print(f'Hours: {hours} Minutes: {minutes} Seconds: {seconds}')
        return hours, minutes, seconds
        
    elif seconds >= 86400:
        days = seconds // 86400
        remainder = seconds % 60
        hours = remainder // 60
        remainder %= 3600
        minutes = remainder // 60
        seconds = remainder % 60

        print(f'Days: {days}\nHours: {hours}\nMinutes: {minutes}\nSeconds: {seconds}')
        return days, hours, minutes, seconds
        
        
    


