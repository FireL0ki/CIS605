# Description: Uses the scorecard class to provide golf score information to users
# Developer: Sif Oberon
# Date Created: 11.17.2025
# Date Last Modified: 11.25.2025

from scorecard import Scorecard

# module level variable (for referencing a scorecard object) initialized to “None”
a_scorecard = None

def main():
    # print program header
    print("Scorecard Program")
    # call function to get user inputs
    get_user_score_input()

# function to get user input (using an appropriate prompt and validation) for a scorecard object
def get_user_score_input():
    # (player name – str, letters only, each name after the first is prefaced by space or hyphen)
    player_name = input("Enter a name: ")
    try:
        while True:
            # ensure player name is only characters
            if player_name.strip().isalpha(): break
    except:
        print("Input error.")
        get_user_score_input()
    else:
        # capitalize 1st letter of each name (first name, last name) & assign the input value to a variable
        # break names out by spaces
        name_parts = player_name.split()

        # create list to hold capitalized parts of names
        capitalized_parts = []
        # iterate over the split up parts of names (first, last)
        for name in name_parts:
            hyphen_parts = name.split('-')  # split names by hyphehs

            # Create empty list to store capitalized hyphenated parts of names
            capitalized_hyphen_parts = []

            # iterate over each part of the hyphenated name
            for hyphen_part in hyphen_parts:
                # Capitalize the first letter and add to the new list
                capitalized_hyphen_parts.append(hyphen_part.capitalize())
            # reconnect hyphenated aprts of names
            capitalized_parts.append('-'.join(capitalized_hyphen_parts))

        # reconnect everything back with spaces
        capitalized_name = ' '.join(capitalized_parts)

        # open the pars.txt file, read, split, convert, and append the data to a list
        pars_list = []
        try:
            # open pars.txt & read (r)
            with open('pars.txt', 'r') as infile:
                # read lines from the file and return as a list of strings
                line = infile.readline().strip()
                # iterate over the lines in the file, putting the scores into a list
                items = line.split(",") # split up lines by comma
            # convert each part to an integer and append to the list
            for item in items:
                item = item.strip()  # remove spaces
                par_value = int(item)
                pars_list.append(par_value)

        # error handling
        except FileNotFoundError as e:
            print(e)
        except ValueError as e:
            print(e)
        except Exception as e:
            print(e)

        # open the lee_scores.txt file, read, split, convert and append the data to a nested list
        nested_scores_list = []
        try:
            with open('lee_scores.txt', 'r') as infile:
                for line in infile:
                    # remove any excess whitespace
                    line = line.strip()
                    # split scores by comma
                    score_strings = line.split(",")

                    round_scores = []
                    for score_string in score_strings:
                        score_string = score_string.strip()
                        score_value = int(score_string)
                        round_scores.append(score_value)

                    nested_scores_list.append(round_scores)
                    
        # error handling
        except FileNotFoundError as e:
            print(e)
        except ValueError as e:
            print(e)
        except Exception as e:
            print(e)

        # call the function (#5) that creates/instantiates a scorecard object
        create_scorecard_object(capitalized_name, pars_list, nested_scores_list)

# function to create a stock analyzer object and assign it to the module level variable
def create_scorecard_object(player_name, course_pars, scores_by_round):
    # modify module level variable - must be declared as a global within the function
    global a_scorecard
    # create object
    a_scorecard = Scorecard(player_name, course_pars, scores_by_round)
    # call the function to display a menu
    display_menu()

# function to display the menu options
def display_menu():
    print("\n--------- Menu ---------")
    print("1) Display scorecard object’s state")
    print("2) Status after each hole for round")
    print("3) Average score for holes of a specific par")
    print("4) Number of holes with same score")
    print("5) Performance by score type")
    print("6) Exit the application")
    
    # get the user’s choice (i.e., 1-6) with an appropriate prompt and validation
    try:
        while True:
            user_selection = int(input("Enter your choice (1-6): "))
            if 1 <= user_selection <= 6: 
                break
    except:
        print("Input error")
    # call function that calls the function associated with the user’s menu choice
    call_menu_function(user_selection)

# function to call function associated with user selection
def call_menu_function(user_selection):
    match user_selection:
        case 1: print_scorecard_object_state()
        case 2: get_user_input_for_round()
        case 3: get_user_input_for_par()
        case 4: find_number_of_holes_with_consistent_score()
        case 5: calc_player_overall_score_by_type()
        case 6: exit_application()

# function to print stock analyzer object state
def print_scorecard_object_state():
    print(a_scorecard)
    # call function to display menu
    display_menu()

# function to get user input (using an appropriate prompt and validation) for the round (int, minimum: 1, maximum: 4)
def get_user_input_for_round():
    # access module level variable
    global a_scorecard
    while True:
        try:
            round_number = int(input("Enter the round number (1-4): "))
            if 1 <= round_number <= 4:
                break
            else:
                print("Round number must be between 1 and 4.")
        except ValueError:
            print("Invalid input. Please enter an integer between 1 and 4.")

    # call method that calculates the player’s status for the given round
    player_status = a_scorecard.calc_player_status(round_number)
    # display results to user
    print(f"Status after each hole for round {round_number} is: {player_status}")
    # call function to display menu
    display_menu()

# function to get user input (using an appropriate prompt and validation) for the par (int, values: 3, 4 or 5)
def get_user_input_for_par():
    global a_scorecard
    while True:
        try:
            selected_par = int(input("Enter a par (3, 4, or 5): "))
            if 3 <= selected_par <= 5:
                break
            else:
                print("The par must be either 3, 4, or 5.")
        except ValueError:
            print("Invalid input. Please enter an integer between 3 and 5.")
    # call the method that calculates and returns the player’s average score for holes of a specific par
    player_average_score = a_scorecard.calc_player_average_score_for_specific_par_hole(selected_par)
    # display the result with appropriate wording and formatting
    print(f"Average score for holes of par {selected_par} is: {player_average_score}")
    # call the function to display the menu
    display_menu()

# function to call the method that finds and returns the number of holes for which the player’s score
# was consistent and display the result with appropriate wording and formatting
def find_number_of_holes_with_consistent_score():
    global a_scorecard
    consistent_scored_holes = a_scorecard.check_if_player_score_consistent()
    print(f"The number of holes for which {a_scorecard.player_name}'s score was consistent: {consistent_scored_holes}")
    # call the function to display the menu
    display_menu()

# function to call the method that calculates and returns the player’s overall performance by score type
# and display the returned value
def calc_player_overall_score_by_type():
    overall_score = a_scorecard.calc_player_performance_by_score_type()
    print(f"{a_scorecard.player_name}'s performance by score type:\n{overall_score}")
    # call the function to display the menu
    display_menu()

# function to ask the user if they wish to exit the application
def exit_application():
    user_response = input("Would you like to exit the application? (Y / N): ")
    if user_response.upper() == "Y":
        # if yes, exit the application
        exit()
    else:
        # else, call the function to display the menu
        display_menu()


# call main() function to start program
main()