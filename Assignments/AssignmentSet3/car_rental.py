# Description: 
# Developer: Sif Oberon
# Date Created: 9.26.2025
# Date Last Modified:


class Car_Rental:
    # initialize the attributes (i.e., customer name, ending odometer reading, beginning odometer 
    # reading, and number of days rented, rental charge - private) of a newly created car rental object
    def __init__(self, customer_name, ending_odometer_reading, beginning_odometer_reading, days_rented, rental_charge):
        self.customer_name = customer_name
        self.ending_odometer_reading = ending_odometer_reading
        self.beginning_odometer_reading = beginning_odometer_reading
        self.days_rented = days_rented
        self.__rental_charge = rental_charge

    @property
    def rental_charge(self):
        return self.__rental_charge

# The getter for rental charge should call the private instance method (see below) and return the rental charge


    # A private instance Method
    # To calculate and return the rental charge | Rental charge = $62.50 per day + $0.57 per mile
    def __calc_rental_charge(self):
        RENTAL_CHARGE_PER_DAY = 62.50
        CHARGE_PER_MILE = .57


        # return rental_charge

# __str__ method that returns relevant information about a car_rental object’s state (i.e., its attributes
# and their current values) as a string with appropriate labels and formatting.
