# Description: Module that gets user input & returns the building costs formatted for the user
# Developer: Sif Oberon
# Date Created: 9.19.2025
# Date Last Modified: 9.19.2025

import deck

def main():

    # get inputs from user for deck square footage, lumber cost per square foot, and cost of a gallon of stain

    deck_square_footage = int(input('Enter the square footage of your deck: '))
    lumber_cost_per_square_foot = float(input('Enter the cost of lumber per square foot: '))
    cost_per_gallon_stain = float(input('Enter the cost per gallon of stain: '))

    # create deck object
    my_deck = deck.Deck(square_footage=deck_square_footage, cost_per_foot=lumber_cost_per_square_foot, cost_per_gallon=cost_per_gallon_stain)

    # print the results for the user using __str__ method
    print(my_deck)

main()