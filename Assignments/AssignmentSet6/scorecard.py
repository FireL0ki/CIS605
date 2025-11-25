# Description: 
# Developer: Sif Oberon
# Date Created: 11.17.2025
# Date Last Modified: 

# Scorecard class
class Scorecard:
    def __init__(self, player_name, course_pars, scores_by_round):
        self.player_name = player_name
        self.course_pars = course_pars
        self.scores_by_round = scores_by_round


# public method to calculate and return the player’s status after each hole for a given round
# (note: the round (i.e., 1-4) will be passed to the method as a parameter).
def calc_player_status(self, round_number):
    # o status after hole 1 = score for hole 1 – par for hole 1
    status = 0
    # for round in round_number:

    # o status after holes 2 through 18 = status after previous hole + (score for current hole – par for current hole

# public method to calculate and return the player’s average score for holes of a specific par
# (note: the par (i.e., 3, 4 or 5) will be passed to the method as a parameter)
def calc_player_average_score_for_specific_par_hole(self, round_number):
    # o player’s average score for holes of a specific par = player's total score for holes of a
    # specific par for all 4 rounds / (total number of holes of a specific par * number of rounds (i.e., 4))
    # o note: do not use a manual count of the number of holes of a specific par; instead, write
    # code to find the number of holes of a specific par.
    pass

# public method to find and return the number of holes for which the player's score was “consistent". 
# The player's score for a given hole is "consistent" if it is the same for all four rounds.
def check_if_player_score_consistent(self):
    pass

# public method to calculate and return the player's overall performance by score type (i.e.,
# number of eagles, birdies, pars, bogeys, and double bogeys). 
# Format and return the result with appropriate wording.
def calc_player_performance_by_score_type(self):
    # o number of eagles = count of number of times player's score is two strokes below par
    # o number of birdies = count of number of times player's score is one stroke below par
    # o number of pars = count of number of times player's score is equal to par
    # o number of bogeys = count of number of times player's score is one stroke above par
    # o number of double bogeys = count of number of times player's score is two strokes above par
    pass

# __str__ method that returns relevant information about a scorecard object’s state (i.e., its
# attributes and their current values) as a string with appropriate labels and formatting.
def __str__(self):
    return f"TODO"