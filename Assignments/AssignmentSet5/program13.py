# Description: Allows user to choose from a menu to dispay information about championships from a .txt file
# Developer: Sif Oberon
# Date Created: 10.28.2025
# Date Last Modified: 10.29.2025

# import the Wimbledon_Champions class from the wimbledon_champions module
from wimbledon_champions import Wimbledon_Champions

# module level variable (for referencing a wimbledon champions object) initialized to “None”
a_champion = None


def main():
    # print program header
    print("Wimbledon Champions Information Retriever")
    # call function that gets data for a champions object
    get_champions_data()

def get_champions_data():


# 4. Has a function to
# a. get data from champions.txt and create a list of champions
# b. call the function (#5) that creates/instantiates a wimbledon champions object

# 5. Has a function (with an appropriate parameter) to
# a. create/instantiate a wimbledon champions object and assign it to the module level
# variable
# b. call the function (6) to display a menu

# 6. Has a function to
# a. display the following menu of options:
# 1) Display the number of times there have been back-to-back champions
# 2) Display the number of times a player has won the championship
# 3) Exit the application
# b. get the user’s choice (i.e., 1-3) with an appropriate prompt and validation
# c. call the function (#7) that calls the function associated with the user’s menu choice

# 7. Has a function (with appropriate parameter) to
# a. call the function associated with the user’s menu choice:
# 1 – function #8
# 2 – function #9
# 3 – function #10

# 8. Has a function to
# a. call the method that that returns the number of times there have been back-to-back
# champions and display the result with appropriate wording
# b. call the function (#6) to display the menu

# 9. Has a function to
# a. get user input (using an appropriate prompt) for a player’s name
# b. call the method that returns the number of times a player has won the championship and
# display the result with appropriate wording
# c. call the function (#6) to display the menu

# 10. Has a function to
# a. ask the user if they wish to exit the application
# b. if yes, exit the application
# c. else, call the function (#6) to display the menu

# TODO sample output
# Wimbledon Champions By LV
# ---- Menu ----
# 1 - Display the number of times there have been back-to-back champions
# 2 - Display the number of times a player has won the championship
# 3 - Exit the application
# Enter your choice (1-3): 1
# Players have won back-to-back championships 16 times
# ---- Menu ----
# 1 - Display the number of times there have been back-to-back champions
# 2 - Display the number of times a player has won the championship
# 3 - Exit the application
# Enter your choice (1-3): 2
# Enter a player's name: Steffi Graf
# Steffi Graf has won the championship 7 times
# ---- Menu ----
# 1 - Display the number of times there have been back-to-back champions
# 2 - Display the number of times a player has won the championship
# 3 - Exit the application
# Enter your choice (1-3): 2
# Enter a player's name: Venus Williams
# Venus Williams has won the championship 5 times
# ---- Menu ----
# 1 - Display the number of times there have been back-to-back champions
# 2 - Display the number of times a player has won the championship
# 3 - Exit the application
# Enter your choice (1-3): 2
# Enter a player's name: Coco Gauff
# Coco Gauff has won the championship 0 times
# ---- Menu ----
# 1 - Display the number of times there have been back-to-back champions
# 2 - Display the number of times a player has won the championship
# 3 - Exit the application
# Enter your choice (1-3): 3
# Do you wish to exit the application (Y or N)?: y