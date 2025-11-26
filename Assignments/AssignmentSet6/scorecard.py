# Description: A Scorecard class that has methods to calculate player score information
# Developer: Sif Oberon
# Date Created: 11.17.2025
# Date Last Modified: 11.25.2025

# Scorecard class
class Scorecard:
    def __init__(self, player_name, course_pars, scores_by_round):
        self.player_name = player_name
        self.course_pars = course_pars
        self.scores_by_round = scores_by_round


    # public method to calculate and return the player’s status after each hole for a given round
    # (note: the round (i.e., 1-4) will be passed to the method as a parameter).
    def calc_player_status(self, round_number):
        # status after holes 2 through 18 
        # = status after previous hole + (score for current hole – par for current hole
        # get the scores for the specified round, accounting for zero based index
        scores = self.scores_by_round[round_number - 1]

        # initialize cumulative status
        status = 0
        cumulative_status = []

        # loop through each hole
        for i in range(len(scores)):
            # get the score for the current hole
            hole_score = scores[i]
            # get the par for the current hole
            hole_par = self.course_pars[i]  
            # status for this hole = score - par
            status += (hole_score - hole_par)
            # add cumulative status to the list
            cumulative_status.append(status)

        return cumulative_status

    # public method to calculate and return the player’s average score for holes of a specific par
    # (note: the par (i.e., 3, 4 or 5) will be passed to the method as a parameter)
    def calc_player_average_score_for_specific_par_hole(self, par):
        # player’s average score for holes of a specific par = player's total score for holes of a
        # specific par for all 4 rounds / (total number of holes of a specific par * number of rounds (i.e., 4))
        # note: do not use a manual count of the number of holes of a specific par; 
        # instead, write code to find the number of holes of a specific par

        total_score_for_specific_par = 0
        total_holes_of_specific_par = 0
        # Loop through all rounds
        for round_scores in self.scores_by_round:
            # Loop through each hole in the round
            for i in range(len(round_scores)):
                # get score for specified hole
                hole_score = round_scores[i]
                # get the par for specified hole
                hole_par = self.course_pars[i]
                # If this hole matches the specified par, include it
                if hole_par == par:
                    total_score_for_specific_par += hole_score
                    total_holes_of_specific_par += 1
        # Calculate average score
        if total_holes_of_specific_par > 0:
            average_score = total_score_for_specific_par / total_holes_of_specific_par
        else:
            average_score = 0  # no holes of this par exist
        return average_score

    # public method to find and return the number of holes for which the player's score was “consistent". 
    # The player's score for a given hole is "consistent" if it is the same for all four rounds.
    def check_if_player_score_consistent(self):
        # Count of consistent holes
        consistent_holes_count = 0
        total_holes = len(self.course_pars)
        # loop through each hole
        for i in range(total_holes):
            # get the score for this hole in the first round
            first_round_score = self.scores_by_round[0][i]
            # assume the hole is consistent unless proven otherwise
            is_consistent = True
            # loop through the remaining rounds to check consistency
            for round_scores in self.scores_by_round[1:]:
                if round_scores[i] != first_round_score:
                    is_consistent = False
                    break  # no need to check further if one round differs
            # if consistent across all rounds, increment the count
            if is_consistent:
                consistent_holes_count += 1
        return consistent_holes_count

    # public method to calculate and return the player's overall performance by score type 
    # (i.e., number of eagles, birdies, pars, bogeys, and double bogeys)
    def calc_player_performance_by_score_type(self):
        # initialize variables to track each score type
        eagles = 0
        birdies = 0
        pars = 0
        bogeys = 0
        double_bogeys = 0

        # loop through each round
        for round_scores in self.scores_by_round:
            # loop through each hole by index
            for i in range(len(self.course_pars)):
                score = round_scores[i]
                par = self.course_pars[i]

                # number of eagles = count of number of times player's score is two strokes below par
                if score == par - 2:
                    eagles += 1
                # number of birdies = count of number of times player's score is one stroke below par
                elif score == par - 1:
                    birdies += 1
                # number of pars = count of number of times player's score is equal to par
                elif score == par:
                    pars += 1
                # number of bogeys = count of number of times player's score is one stroke above par
                elif score == par + 1:
                    bogeys += 1
                # number of double bogeys = count of number of times player's score is two strokes above par
                elif score == par + 2:
                    double_bogeys += 1

        # format and return the result with appropriate wording
        result = (
            f"# of Eagles: {eagles}\n"
            f"# of Birdies: {birdies}\n"
            f"# of Pars: {pars}\n"
            f"# of Bogeys: {bogeys}\n"
            f"# of Double Bogeys: {double_bogeys}"
        )
        return result

    # __str__ method that returns relevant information about a scorecard object’s state (i.e., its
    # attributes and their current values) as a string with appropriate labels and formatting.
    def __str__(self):
        return f"Player: {self.player_name}\nCourse Pars: {self.course_pars}\nScorecard: {self.scores_by_round}"