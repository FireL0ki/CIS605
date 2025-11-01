# Description: Class for a Wimbledon Champions object
# Developer: Sif Oberon
# Date Created: 10.28.2025
# Date Last Modified: 10.31.2025

# Wimebledon_Champions class with 1 instance attributes - champions (private)
class Wimbledon_Champions:
    def __init__(self, champions):
        self.__champions = champions

    @property
    def champions(self):
        return self.__champions

    # public method (with one parameter for the name of a tennis player) to check and return the number of times the player has won the championship
    def get_player_championship_wins(player_name):
        try:
            # open champions.txt & read (r)
            with open('champions.txt', 'r') as infile:
                lines = infile.readlines()

                # iterate over the lines in the file, finding all instances of the input player's name
                for line in lines:
                    count = 0
                    if line == player_name:
                        count + 1
                        print(f"Count tracker: {count}")
                return count
            
        except FileNotFoundError as e:
            print(e)

        except ValueError as e:
            print(e)

        except Exception as e:
            print(e)


    # a public method to find and return the number of times there have been back-to-back champions
    def get_number_back_to_back_champions(self):
        pass