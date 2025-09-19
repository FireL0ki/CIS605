# Description: Modules that creates an Invesment class object & its corresponding attributes & functions
# Developer: Sif Oberon
# Date Created: 9.16.2025
# Date Last Modified: 9.16.2025

# create a class called Investment
class Investment:

    # create the initializer method for Investment objects to define its attributes
    def __init__(self, present_value, investment_duration, annual_interest):
        self.__present_value = present_value
        self.__duration = investment_duration
        self.__interest = annual_interest

    # create getters & setters for the Investment objects so their attributes can be accessed
    @property
    def present_value(self):
        return self.__present_value
    
    @present_value.setter
    def present_value(self, value):
        self.__present_value = value

    @property
    def duration(self):
        return self.__duration
    
    @duration.setter
    def duration(self, value):
        self.__duration = value

    @property
    def interest(self):
        return self.__interest
    
    @interest.setter
    def interest(self, value):
        self.__interest = value

    # function to calculate and return the future value of investment
    def calculate_future_value(self):
        future_value = self.present_value * (1 + self.__interest/100)** self.__duration
        return future_value
    
    # create __str__ method
    def __str__(self):
        return f'The future value of an investment of ${self.present_value:,.2f} for a duration of {self.duration} year(s) at an interest rate of {self.interest:.2f}% is ${self.calculate_future_value():,.2f}.'

