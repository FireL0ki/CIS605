# Description: A series of functions that return different favorite items
# Dependencies: my_favorites.py
# Developer: Sif Oberon
# Date Created: 9.5.2025
# Date Last Modified: 9.5.2025

import my_favorites as favorite

# set my_name variable to string literal 'Sif'
my_name = 'Sif'

# prints a formatted string containing the variable value in my_name
print(f'Here are a few of {my_name}\'s favorite things')

# prints formatted strings that include function calls from my_favorites.py
print(f'{my_name}\'s favorite color is {favorite.favorite_color()}.')
print(f'{my_name}\'s favorite movie is {favorite.favorite_movie()}.')
print(f'{my_name}\'s favorite activity is {favorite.favorite_activity()}.')