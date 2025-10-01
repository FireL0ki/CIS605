# Description: 
# Developer: Sif Oberon
# Date Created: 9.26.2025
# Date Last Modified:

# • Import the walk module
from walk import Walk

def main():
    # • Using appropriate prompts, gets the walker’s name, number of steps (int), and length of step in inches (int)
    # as user input, and assigns the values to variables
    walker_name = input("Enter your name: ")
    number_steps = int(input("Enter the number of steps you took: "))
    step_length = int(input("Enter your average step length in inches: "))

    # • Create/instantiate a walker object
    my_walker = Walk(walker_name=walker_name, number_steps=number_steps, step_length=step_length)

    # calls the instance method that calculates the miles walked, and prints the result with appropriate wording and formatting 
    # (e.g., Beth Walker's walk with 9,876 steps averaging 30
    # inches per step equates to 4.68 miles.)
    print(my_walker)

main()