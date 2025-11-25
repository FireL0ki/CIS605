# Description: 
# Developer: Sif Oberon
# Date Created: 11.17.2025
# Date Last Modified: 

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
            if player_name.isalpha(): break
    except:
        print("Input error.")
        get_user_score_input()
    else:
        # capitalize the first letter of each name (i.e., first name, last name) and assign the input value to a variable
        for name in names:
            name.capitalize()

        # open the pars.txt file, read, split, convert, and append the data to a list
        pars_list = []
        try:
            # open pars.txt & read (r)
            with open('pars.txt', 'r') as infile:
                # read lines from the file and return as a list of strings
                pars = infile.readlines()
                # iterate over the lines in the file, putting the scores into a list
                for item in pars:
                    # add prices to the price list and strip white space
                    pars_list.append(item.strip())
        # error handling
        except FileNotFoundError as e:
            print(e)
        except ValueError as e:
            print(e)
        except Exception as e:
            print(e)

        # open the lee_scores.txt file, read, split, convert and append the data to a nested list
        # TODO NESTED LIST
        nested_scores_list = []
        try:
            # open lee_scores.txt & read (r)
            with open('lee_scores.txt', 'r') as infile:
                # read lines from the file and return as a list of strings
                scores = infile.readlines()
                # iterate over the lines in the file, putting the scores into a list
                for score in scores:
                    # add prices to the price list and strip white space
                    nested_scores_list.append(score.strip())
        # error handling
        except FileNotFoundError as e:
            print(e)
        except ValueError as e:
            print(e)
        except Exception as e:
            print(e)

        # call the function (#5) that creates/instantiates a scorecard object
        create_scorecard_object(player_name, course_pars, scores_by_round)

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
            user_selection = int(input("Enter our choice (1-6): "))
            if 1 <= user_selection <= 6: break
    except:
        print("Input error")
    # call function that calls the function associated with the user’s menu choice
    call_menu_function(user_selection)

# b. get the user’s choice (i.e., 1-6) with an appropriate prompt and validation
# c. call the function (#7) that calls the function associated with the user’s menu choice
def call_menu_function(user_selection):
    match user_selection:
        case 1: print_scorecard_object_state()
        case 2: get_user_input_for_round()
        case 3: get_user_input_for_par()
        case 4: find_number_of_holes_with_consistent_score()
        case 5: cal_player_overall_score_by_type()
        case 6: exit_application()

# function to print stock analyzer object state
def print_scorecard_object_state():
    print(a_scorecard)
    
    # call function to display menu
    display_menu()

# function to get user input (using an appropriate prompt and validation) for the round (int, minimum: 1, maximum: 4)
def get_user_input_for_round():
    pass
    # call the method that calculates and returns the player’s status after each hole for a given
    # round and display the result with appropriate wording.
    # TODO

    # call the function to display the menu
    display_menu()

# function to get user input (using an appropriate prompt and validation) for the par (int, values: 3, 4 or 5)
def get_user_input_for_par():
    pass
    # b. call the method that calculates and returns the player’s average score for holes of a
    # specific par and display the result with appropriate wording and formatting
    # TODO
    # call the function to display the menu
    display_menu()

# function to call the method that finds and returns the number of holes for which the player’s score
# was consistent and display the result with appropriate wording and formatting
def find_number_of_holes_with_consistent_score():
    pass
    # call the function to display the menu
    display_menu()

# function to call the method that calculates and returns the player’s overall performance by score type
# and display the returned value
def cal_player_overall_score_by_type():
    pass
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