# Description: Functions that calculate the area & volume of a cylinder
# Dependencies: none
# Developer: Sif Oberon
# Date Created: 9.5.2025
# Date Last Modified: 9.5.2025

# import Python's built in math module to make use of its functions
import math

# a function that takes two parameters, height & radius, and uses them to calculate & returns the area of a cylinder
def calc_area(radius, height):
    # I am getting a different answer than 
    area = (2 * math.pi * radius) * (radius + height)
    return area

# a function that takes two parameters, height & radius, and uses them to calculate & returns the volume of a cylinder
def calc_volume(radius, height):
    volume = math.pi * radius**2 * height
    return volume
