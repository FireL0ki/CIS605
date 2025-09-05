# Description:      Perform calculations
# Purpose:          Demonstrate type conversion, format specifiers
# Depends on:       abacus.py
# Developed By:     LV

import abacus as a # import the abacus module

print('A simple calculator for two integers')

number1 = int(input('Enter first integer: ')) # convert input value from string to integer

number2 = int(input('Enter second integer: ')) # convert input value from string to integer

print(f'The result of adding {number1:,} and {number2:,} is {a.add(number1, number2):,}') # format and display the result returned by the add function

print(f'The result of subtracting {number2:,} from {number1:,} is {a.subtract(number1, number2):,}') # format and display the result returned by the subtract function

print(f'The result of multiplying {number1:,} by {number2:,} is {a.multiply(number1, number2):,}') # format and display the result returned by the multiply function
12
print(f'The result of dividing {number1:,} by {number2:,} is {a.divide(number1, number2):,.2f}') # format and display the result returned by the divide function

print(f'The result of integer dividing {number1:,} by {number2:,} is {a.integer_divide(number1, number2):,}') # format and display the result returned by the integer_divide function

print(f'The result of a modulo operation of {number1:,} by {number2:,} is {a.modulo(number1, number2):,}') # format and display the result returned by the modulo function

print(f'The result of exponentiating {number1:,} by {number2:,} is {a.exponeniate(number1, number2):e}') # format and display the result returned by the exponentiate function