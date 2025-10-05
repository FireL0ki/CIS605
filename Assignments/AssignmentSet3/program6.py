# Description: program that calculates the miles walked based on the number of steps & length of step
# Developer: Sif Oberon
# Date Created: 9.26.2025
# Date Last Modified: 10.5.2025

# import the walk module
from walk import Walk

def main():
    # get the walker’s name, number of steps (int), and length of step in inches (int) as user inputs
    walker_name = input("Enter your name: ")
    number_steps = int(input("Enter the number of steps you took: "))
    step_length = int(input("Enter your average step length in inches: "))

    # create/instantiate a walker object
    my_walker = Walk(walker_name=walker_name, number_steps=number_steps, step_length=step_length)

    # calls the instance method that calculates the miles walked, and prints the result with appropriate wording and formatting 
    print(my_walker)

main()