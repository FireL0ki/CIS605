# Project:          Module 6 - Example 3
# Description:      Class definition for Scorecard
# Demonstrates:     List of Lists or Nested Lists
# Developed By:     LV
# Date:             October 2025

# import the NumPy package

import numpy as np

class Scorecard:

    # initializer

    def __init__(self, name, pars, scores):
        
        self.course_pars = pars
        self.player_name = name
        self.scores_by_round = scores
        
    # instance methods to demo processing a matrix (a two-dimensional list where each inner list represents a row of the matrix)

    # calculate average score for each hole manually

    def calc_avg_score_by_hole1(self):

        num_rounds = len(self.scores_by_round) # number of rows
        num_holes = len(self.scores_by_round[0]) # number of columns

        hole_averages = [] # a list to store the averages for each hole
        
        # use nested loops to access the score for each hole in each round 
       
        for col in range(num_holes):    # for each hole
            hole_sum = 0                # variable to sum the scores for a hole across the four rounds
            for row in range(num_rounds):   # for each round
                hole_sum += self.scores_by_round[row][col]  # sum up the scores for a hole across the four rounds to get the total score for the hole
            
            # calculate the average score for a hole by dividing the total score for the hole by the number of rounds
            # append it to the hole_averages list

            hole_averages.append(hole_sum/num_rounds)

        # prepare output
        
        result = ""
        
        for item in range(num_holes):
            result += f"Hole {item+1}: {hole_averages[item]:.2f}\n"

        
        # alternative "for loop" using the enumerate function
        # from Gemini

        # The enumerate() function adds a counter to an iterable and returns it as an enumerate object. 
        # This object yields pairs of (index, value) for each item in the iterable. 
        # It is particularly useful when iterating over a sequence and needing both the item's value and its position (index). 
        
        # for index, item in enumerate(hole_averages):
        #     result += f"Hole {index+1}: {item:.2f}\n"
        
        return result
                                         
    # calculate average score for each hole using NumPy

    def calc_avg_score_by_hole2(self):
    
        # convert the list of lists to a NumPy 2-dimensional array

        scores_array = np.array(self.scores_by_round)

        # axis=0 represents the rows; in this case, the mean operation is performed across the rows for each column
        
        hole_averages = np.mean(scores_array, axis=0)
    
        result = [f"Hole {index+1}: {item:.2f}" for index, item in enumerate(hole_averages)]  # use list comprehension to prepare output

        return result
    
    # calculate total score for each round manually

    def calc_total_score_by_round1(self):

        num_rounds = len(self.scores_by_round) # number of rows
        num_holes = len(self.scores_by_round[0]) # number of columns
        
        round_totals = [] # a list to store the totals for each round
        
        # use nested loops to access the score for each hole in each round 
       
        for row in range(num_rounds):   # for each round
            round_sum = 0               # variable to sum the scores for a hole across the 18 holes
            for col in range(num_holes):   # for each hole
                round_sum += self.scores_by_round[row][col]  # add up the scores for a round across the 18 holes to get the total score for the round
            
           # append it to the round_totals list

            round_totals.append(round_sum)
             
        result = "Total Score for each round\n"
                
        for index, item in enumerate(round_totals):
            result += f"Round {index+1}: {item}\n"
        
        return result
    
    # calculate total score for each round manually (without indices)

    def calc_total_score_by_round2(self):

        round_totals = [] # a list to store the totals for each round
        
        # use nested loops to access the score for each hole in each round 
       
        for row in self.scores_by_round:    # for each round
            round_sum = 0                   # variable to sum the scores for a hole across the 18 holes
            for score in row:   # for each hole score in row
                round_sum += score  # add up the scores for a round across the 18 holes to get the total score for the round
            
           # append it to the round_totals list

            round_totals.append(round_sum)
             
        result = "Total Score for each round\n"
        
        for index, item in enumerate(round_totals):
            result += f"Round {index+1}: {item}\n"
        
        return result
        
    # calculate total score for each round using list comprehension

    def calc_total_score_by_round3(self):

        # use list comprehension to sum up the scores for each round
        
        round_totals = [sum(items) for items in self.scores_by_round]
             
        result = "Total Score for each round\n"
        
        for index, item in enumerate(round_totals):
            result += f"Round {index+1}: {item}\n"
        
        return result
    
    # calculate total score for each round using NumPy

    def calc_total_score_by_round4(self):

        # convert the list of lists to a NumPy array

        scores_array = np.array(self.scores_by_round)

        # axis=1 represents the columns; in this case, the sum operation is performed across the columns for each round
        
        round_totals = np.sum(scores_array, axis=1)
    
        result = [f"Round {index}: {item}" for index, item in enumerate(round_totals)]  # use list comprehension to prepare output

        return result
    
    # calculate total score for all rounds manually

    def calc_total_score1(self):

        total = 0

       # use nested loops to access the score for each hole in each round 
       
        for row in self.scores_by_round:    # for each round
            for score in row:   # for each hole score in a row
                total += score  # add up the score for each hole across the four rounds and 18 holes
            
        return f"The total score is: {total}"
        
    # calculate total score for each round using list comprehension

    def calc_total_score2(self):

        # use list comprehension to sum up the scores for each round
              
        total = sum([score for round in self.scores_by_round for score in round])
             
        return f"The total score is: {total}"
    
    # calculate total score for each round using NumPy

    def calc_total_score3(self):

        # convert the list of lists to a NumPy array

        scores_array = np.array(self.scores_by_round)

        total = np.sum(scores_array)
    
        return f"The total score is: {total}"
   
    def __str__(self):
        
        return f'Player: {self.player_name}\nCourse Pars: {self.course_pars}\nScorecard: {self.scores_by_round}'