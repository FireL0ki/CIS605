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

  

# Write a function (with a parameter for number of seconds) that prints:
# the number of seconds if number < 60
# the number of minutes and seconds if number < 3,600
# the number of hours, minutes and seconds if number < 86,400
# the number of days, hours, minutes, and seconds if number >= 86,400

