# Description: A program that takes user input of a cylinder's height & radius, and prints the resulting volume & area of the cylinder
# by calling functions from cylinder.py
# Dependencies: cylinder.py
# Developer: Sif Oberon
# Date Created: 9.5.2025
# Date Last Modified: 9.5.2025

import cylinder

# set the height & radius variables to values received by user input, and convert them to integers
height =int(input('Please enter the cylinder\'s height: '))
radius = int(input('Please enter the cylinder\'s radius: '))


# assign the returned values of the area & volume functions to variables
cylinder_area = cylinder.calc_area(radius, height)
cylinder_volume = cylinder.calc_volume(radius, height)

# print formatted strings that include the height & radius variable values & values of the functions called from cylinder.py
print(f'The area of a cylinder with a height of {height} and a radius of {radius} is {cylinder_area}.')
print(f'The volume of a cylinder with a height of {height} and a radius of {radius} is {cylinder_volume}.')