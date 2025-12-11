# Project:          Module 10 - Example 1
# Description:      Class definition for an enumeration
# Demonstrates:     Enumerations
# Developed By:     LV
# Date:             November 2025

# From Gemini - An enumeration, or enum, in Python is a set of symbolic names (members) that are bound to unique, constant values. 
# They are created by subclassing enum.Enum to make code more readable, maintainable, and less error-prone by replacing "magic" numbers or strings with meaningful labels.

from enum import Enum

class Food_Group(Enum):

    GRAINS = 1
    VEGETABLES = 2
    FRUITS = 3
    PROTEIN = 4
    DAIRY = 5
    SWEETS = 6



