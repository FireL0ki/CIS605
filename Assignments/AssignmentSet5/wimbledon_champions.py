# Description: Class for a Wimbledon Champions object
# Developer: Sif Oberon
# Date Created: 10.28.2025
# Date Last Modified: 11.6.2025

# Wimebledon_Champions class with 1 instance attributes - champions (private)
class Wimbledon_Champions:
    def __init__(self, champions):
        self.__champions = champions

    @property
    def champions(self):
        return self.__champions

    # public method (with one parameter for the name of a tennis player) to check and return the number of times the player has won the championship
    def get_player_championship_wins(self, player_name):
        wins_count = 0
        # for each champion in the champions list
        for champion in self.__champions:
            (print(f" Champion: {champion}"))
            # check if the current index name matches the name entered by the user
            if champion.lower() == player_name.lower():
                # if so, add to the count
                wins_count +=1
        return wins_count


    # a public method to find and return the number of times there have been back-to-back champions
    def get_number_back_to_back_champions(self):
        back_to_back_count = 0
        champions = self.champions

        # initialize i at the starting index
        i = 0
        # iterate over the list of champions
        while i < len(champions) - 1:
            # compare current (index [i] and next winner to see if they match
            if champions[i] == champions[i +1]:
                # add to the count
                back_to_back_count += 1
                # skip to the next champion (since by comparing 1 & 2, champion 2 has already been counted if they were part of a back to back win)
                # while the current iteration plus 1 (comparing the index following the initial, every other)is less than the length of champions - 1 (don't need to go beyond the second to last index)
                # AND if the champion in the next index after the current is the same as the one after that
                # ex: on index 1 (which has already been compared and matched index 2) and the next index [2] also matches index [3], that is 3 wins in a row, and the first back to back has already been counted
                # while i + 1 < len(champions) - 1 and champions[i + 1] == champions[i + 2]:
                #     # skip to the next champion / index
                #     i += 1
            # move to next index
            i += 1
        return back_to_back_count