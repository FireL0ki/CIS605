# Description: A pay stub class that contains class attributes & instance attributes to track pay rate & hours worked information, and methods to calculate net pay and track totals
# Developer: Sif Oberon
# Date Created: 9.26.2025
# Date Last Modified: 10.5.2025

class Pay_Stub:
    # class attributes are common to all objects/instances
    # declare 3 class attributes: Total number of pay stubs (private), Total gross pay (private), Total net pay (private)
    __total_number_pay_stubs = 0
    __total_gross_pay = 0
    __total_net_pay = 0

    # initializer that initializes the employee’s name, hours worked, and pay rate attributes of a newly created pay stub object
    def __init__(self, employee_name, hours_worked, pay_rate):
        self.__employee_name = employee_name
        self.__hours_worked = hours_worked
        self.__pay_rate = pay_rate
        # set the net pay attribute’s value by calling the instance method that calculates net pay
        self.__net_pay = self.__calc_net_pay()

        # call the class method that increments the three class attributes - must be called on the class
        Pay_Stub.__increment_class_attributes(self)

    # region getters
    # create getters to access private attributes as properties
    @property
    def employee_name(self):
        return self.__employee_name
    
    @property
    def hours_worked(self):
        return self.__hours_worked

    @property
    def pay_rate(self):
        return self.__pay_rate
    
    @property
    def net_pay(self):
        return self.__net_pay

    # endregion

    # private instance method that calculates net pay | Net pay = Gross Pay – Federal Income Tax – State Income Tax - Social Security Tax – Medicare Tax
    def __calc_net_pay(self):
        # Gross Pay = hours worked * pay rate
        gross_pay = self.hours_worked * self.pay_rate
        # create constants
        # Federal Income Tax = gross pay * 11.49% | State Income Tax = gross pay * 5.81%
        # Social Security Tax = gross pay * 6.20% | Medicare Tax = gross pay * 1.45%
        FEDERAL_INCOME_TAX_RATE = .1149
        STATE_INCOME_TAX = .0581
        SOCIAL_SECURITY_TAX = .0620
        MEDICARE_TAX = .0145

        fed_income_tax = FEDERAL_INCOME_TAX_RATE * gross_pay
        state_income_tax = STATE_INCOME_TAX * gross_pay
        social_security_tax = SOCIAL_SECURITY_TAX * gross_pay
        medicare_tax = MEDICARE_TAX * gross_pay

        # calculate net pay
        net_pay = gross_pay - fed_income_tax - state_income_tax - social_security_tax - medicare_tax
        
        # return net pay
        return net_pay

    # __str__ method that returns relevant information about a pay_stub object’s state (its attributes and their current values)
    def __str__(self):
        return f'\nEmployee Name: {self.employee_name}\nHours Worked: {self.hours_worked}\nPay Rate: ${self.pay_rate:,.2f}\nNet Pay: ${self.net_pay:,.2f}\n'

    # private class method that increments the three class attributes
    @classmethod
    def __increment_class_attributes(cls, self):
        # increment number of pay stubs
        cls.__total_number_pay_stubs += 1
        # increment total gross pay
        cls.__total_gross_pay += (self.hours_worked * self.pay_rate)
        cls.__total_net_pay += self.net_pay
    
    # private class method that calculates and returns the average net pay
    @classmethod
    def __calc_average_net_pay(cls):
        average_net_pay = cls.__total_net_pay / cls.__total_number_pay_stubs
        
        return average_net_pay
    
    # public class method that returns summary info (total # pay stubs, total gross pay, total net pay, and average net pay) as a string
    @classmethod
    def summary_info(cls):
        return f'Total Number of Pay Stubs: {cls.__total_number_pay_stubs}\nTotal Gross Pay: ${cls.__total_gross_pay:,.2f}\nTotal Net Pay: ${cls.__total_net_pay:,.2f}\nAverage Net Pay: ${cls.__calc_average_net_pay():,.2f}\n'