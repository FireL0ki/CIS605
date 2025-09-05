# Description: A series of functions that return different favorite items
# Dependencies: my_favorites.py
# Developer: Sif Oberon
# Date Created: 9.5.2025
# Date Last Modified: 9.5.2025

import my_favorites as favorite

my_name = 'Sif'

print(f'Here are a few of {my_name}\'s favorite things')
print(f'{my_name}\'s favorite color is {favorite.favorite_color()}.')
print(f'{my_name}\'s favorite movie is {favorite.favorite_movie()}.')
print(f'{my_name}\'s favorite activity is {favorite.favorite_activity()}.')