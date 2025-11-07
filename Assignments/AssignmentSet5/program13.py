# Description: Allows user to choose from a menu to dispay information about championships from a .txt file
# Developer: Sif Oberon
# Date Created: 10.28.2025
# Date Last Modified: 11.6.2025

# import the Wimbledon_Champions class from the wimbledon_champions module
from wimbledon_champions import Wimbledon_Champions
from sys import exit


# module level variable (for referencing a wimbledon champions object) initialized to “None”
a_champion = None

def main():
    # print program header
    print("Wimbledon Champions Information Retriever")
    # call function that gets data for a champions object
    get_champions_data()

# a function to get data from champions.txt and create a list of champions
def get_champions_data():
    # TODO this needs to be saved to the champions object or it will not persist
    champions_list = []

    try:
        # open champions.txt & read (r)
        with open('S:\CIS605\Assignments\AssignmentSet5\champions.txt', 'r') as infile:
            # read lines from the file and return as a list of strings
            champions = infile.readlines()

            # iterate over the lines in the file, putting the champions into a list
            for champion in champions:
                champion = champion.lower()
                # add champions to the champion list and strip white space
                champions_list.append(champion.strip())

    # error handling
    except FileNotFoundError as e:
        print(e)

    except ValueError as e:
        print(e)

    except Exception as e:
        print(e)

    # call the function that creates/instantiates a wimbledon champions object
    create_champion_object(champions_list=champions_list)

# function (with an appropriate parameter) to create/instantiate a wimbledon champions object and assign it to the module level variable
def create_champion_object(champions_list):
    global a_champion
    a_champion = Wimbledon_Champions(champions=champions_list)
    # call the function to display a menu
    display_menu()

# function to display the  menu
def display_menu():
    print("\n----- Menu -----")
    print("1) Display the number of times there have been back-to-back champions")
    print("2) Display the number of times a player has won the championship")
    print("3) Exit the application")

    try:
        while True:
            user_selection = int(input("Enter our choice (1-3): "))
            if 1 <= user_selection <= 3: break
    except:
        print("Input error")

    # call method to get user selection
    call_menu_function(user_selection)

# method to call appropriate function based on user selection
def call_menu_function(user_selection):
    match user_selection:
        case 1: get_number_of_back_to_back_champions()
        case 2: get_number_of_championship_wins_for_player()
        case 3: exit_application()

# function to call the method that that returns the number of times there have been back-to-back
# champions and display the result with appropriate wording
def get_number_of_back_to_back_champions():
    number_championships = a_champion.get_number_back_to_back_champions()
    print(f"Players have won back to back championships {number_championships} times")
    # call the function to display the menu
    display_menu()

# function to get user input (using an appropriate prompt) for a player’s name
def get_number_of_championship_wins_for_player():
    try:
        while True:
            player_name = input("Enter a player's name: ").lower()

            print(f"champions list: {a_champion.champions}")
            if player_name in a_champion.champions: 
                break
    except:
        print("Input error")
        get_number_of_championship_wins_for_player()
    else:
        # call the method that returns the number of times a player has won the championship and
        # display the result with appropriate wording
        number_championships = a_champion.get_player_championship_wins(player_name=player_name)
        print(f"{player_name} has won the championship {number_championships} times")
    # call the function to display the menu
    display_menu()

# function to ask the user if they wish to exit the application
def exit_application():
    user_response = input("Do you wish to exit the application (Y / N)? ")
    # if yes, exit the application
    if user_response.lower() == "y":
        print(f"Program End.")
        exit()
    # else, call the function to display the menu
    else:
        display_menu()

# main program call to start application
main()