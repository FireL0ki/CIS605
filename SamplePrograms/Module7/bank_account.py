# Project:          Module 7 - Example 1
# Description:      Class definition for Bank Account (parent class)
# Demonstrates:     Inheritance
# Developed By:     LV
# Date:             October 2025

from datetime import date as dt

class Bank_Account:

    # initializer

    def __init__(self, customer_name, initial_deposit):
        
        self.customer_name = customer_name
        
        self.__account_balance = 0

        self.deposit(initial_deposit) # call the deposit method

        self.__account_date_opened = dt.today()
        
    # getters

    @property
    def account_balance(self):
        return self.__account_balance
    
    @property
    def account_date_opened(self):
        return self.__account_date_opened
    
    # instance methods

    def deposit(self, amount):

        self.__account_balance += amount

        return f"${amount:,.2f} credited to {self.customer_name}'s account\nCurrent Balance: ${self.account_balance:,.2f}"
    
    def withdraw(self, amount):

        # if the amount to be withdrawn is less than or equal to the available balance, withdraw that amount
        # else, withdraw the available balance

        withdraw_amount = amount if amount <= self.account_balance else self.account_balance 
    
        self.__account_balance -= withdraw_amount

        return f"${withdraw_amount:,.2f} debited from {self.customer_name}'s account\nCurrent Balance: ${self.account_balance:,.2f}"
    
    def __str__(self):
         
         return f'Customer Name: {self.customer_name}\nDate Account Opened: {self.account_date_opened}\nAccount Balance: ${self.account_balance:,.2f}'