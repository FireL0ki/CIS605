# Description: 
# Developer: Sif Oberon
# Date Created: 9.26.2025
# Date Last Modified:

class Car_Rental:
    # initialize the attributes (i.e., customer name, ending odometer reading, beginning odometer 
    # reading, and number of days rented, rental charge - private) of a newly created car rental object
    def __init__(self, customer_name, begin_odometer_reading, ending_odometer_reading, days_rented):
        self.customer_name = customer_name
        self.begin_odometer_reading = begin_odometer_reading
        self.ending_odometer_reading = ending_odometer_reading
        self.days_rented = days_rented
        self.__rental_charge = self.__calc_rental_charge()

    # create getter for private attribute
    # call the private instance method & return the rental charge
    @property
    def rental_charge(self):
        return self.__rental_charge


    # private instance method that calculates & returns the rental charge | Rental charge = $62.50 per day + $0.57 per mile
    def __calc_rental_charge(self):
        RENTAL_CHARGE_PER_DAY = 62.50
        CHARGE_PER_MILE = .57

        miles_driven = self.ending_odometer_reading - self.begin_odometer_reading
        rental_charge = (self.days_rented * RENTAL_CHARGE_PER_DAY) + (miles_driven * CHARGE_PER_MILE)

        return rental_charge

    # __str__ method that returns relevant information about a car_rental object’s state (i.e., its attributes
    # and their current values) as a string with appropriate labels and formatting.
    def __str__(self):
        # return f'For a car rented for {self.days_rented} with an odometer that started on {self.begin_odometer_reading} and ended on {self.ending_odometer_reading} for a total of {self.ending_odometer_reading - self.begin_odometer_reading} miles driven, the rental charge would be {self.rental_charge}'
        return f'Customer Name: {self.customer_name}\nNumber of Rental Days: {self.days_rented}\nMiles Driven: {self.ending_odometer_reading - self.begin_odometer_reading:,}\nRental Charge:${self.rental_charge:,.2f}'