# Description: 
# Developer: Sif Oberon
# Date Created: 9.26.2025
# Date Last Modified:

# Create another module (program7.py) that
# • Imports the Car_Rental class from the class_rental module.

from car_rental import Car_Rental

# declare module-level variable
my_rental_charge = None

def main():
    # print title for program
    print("Car Rental Fee Calculator")
    
    # call function to get user inputs
    get_user_inputs()

# get customer name, beginning odometer reading (int), ending odometer reading (int), and days rented (int) as user input
def get_user_inputs():
    customer_name = input("Please enter your name: ")
    begin_odometer_reading = int(input("Enter your starting odometer reading: "))
    end_odometer_reading = int(input("Enter your ending odometer reading: "))
    days_rented = int(input("Enter the number of days you are renting the car: "))

    # call function to create rental charge object
    create_rental_charge_object(customer_name, begin_odometer_reading, end_odometer_reading, days_rented)

# function to create rental charge object
def create_rental_charge_object(name, begin_odometer_reading, end_odometer_reading, days_rented):
    # declare the module level variable as global within function in order to modify it
    global my_rental_charge

    # create my rental charge instance
    my_rental_charge = Car_Rental(customer_name=name, begin_odometer_reading=begin_odometer_reading, ending_odometer_reading=end_odometer_reading, days_rented=days_rented)

    # print the object's state by calling the existing __str__ method within this method
    print_object()

# function to call the __str__ method to print the object's state
def print_object():
    print(my_rental_charge)


# call main method to start program
main()
