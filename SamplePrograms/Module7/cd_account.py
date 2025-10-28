# Project:          Module 7 - Example 1
# Description:      Class definition for CD Account (Child class)
# Demonstrates:     Inheritance
# Developed By:     LV
# Date:             October 2025

from datetime import date as dt

from dateutil.relativedelta import relativedelta as rd  # to add months to a date

from bank_account import Bank_Account

# the relationship between parent and child classes is indicated by including the parent's name in parentheses after the child's name

class CD_Account (Bank_Account):

    # initializer

    def __init__(self, customer_name, initial_deposit, rate, duration):
        
        # using super(), the parent's initializer method is called and the arguments needed to initialize the parent's attributes are passed
        
        super().__init__(customer_name, initial_deposit)
        
        # in addition to the properties inherited from its parent, a child can have properties that are specific to it.
        
        self.__cd_rate = rate
        self.__cd_duration = duration
       
    # instance methods
    
    # the child's withdraw method extends the parent's withdraw method 
    
    def withdraw(self, amount):

        EARLY_WITHDRAWL_PENALTY = 50
        
        # if the CD has not matured, a penalty is assessed

        if dt.today() < self.account_date_opened + rd(months=self.__cd_duration):
            
            # if the amount to be withdrawn + the penalty is less than or equal to the available balance, allow the withdrawal

            if (total_amount := amount + EARLY_WITHDRAWL_PENALTY) <= self.account_balance:

                # call the parent's withdraw method

                return super().withdraw(total_amount)
            
            # else, deny the withdrawl

            else:

                return f"Insufficient funds in {self.customer_name}'s account\nCurrent Balance: ${self.account_balance:,.2f}"
        
        # if the CD has matured, allow the withdrawal without a penalty

        else:

            return super().withdraw(amount)
        
    def calc_days_to_maturity(self):

        # get the difference between today's date and the CD maturity date

        time_difference = (self.account_date_opened + rd(months=self.__cd_duration)) - dt.today()

        return f"{self.customer_name}'s CD account matures in {time_difference.days} days"
    
    def __str__(self):
         
         return f'{super().__str__()}\nCD Rate: {self.__cd_rate:.2f}%\nCD Duration: {self.__cd_duration:} months'