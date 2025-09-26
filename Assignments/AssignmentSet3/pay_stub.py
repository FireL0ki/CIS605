# Description: 
# Developer: Sif Oberon
# Date Created: 9.26.2025
# Date Last Modified:

# Create a module (pay_stub.py) for a class (Pay_Stub) that has
# • 3 class attributes
# o Total number of pay stubs (private)
# o Total gross pay (private)
# o Total net pay (private)
# • 4 instance attributes
# o Employee name (private)
# o Hours worked (private)
# o Pay rate (private)
# o Net pay (private)
# • An initializer that
# o initializes the employee’s name, hours worked, and pay rate attributes of a newly created pay
# stub object.
# o sets the net pay attribute’s value by calling the instance method that calculates net pay (see
# below).
# • A private instance method that
# o Calculates net pay
#  Net pay = Gross Pay – Federal Income Tax – State Income Tax - Social Security Tax –
# Medicare Tax
# • Gross Pay = hours worked * pay rate
# • Federal Income Tax = gross pay * 11.49%
# • State Income Tax = gross pay * 5.81%
# • Social Security Tax = gross pay * 6.20%
# • Medicare Tax = gross pay * 1.45%
# o Calls the class method that increments the three class attributes (see below).
# o Returns the net pay.
# • A __str__ method that returns relevant information about a pay_stub object’s state (i.e., its attributes and
# their current values) as a string with appropriate labels and formatting.
# • A private class method that
# o Increments the three class attributes.
# • A private class method that
# o Calculates and returns the average net pay.
# • A public class method that
# o Returns summary information (i.e., total number of pay stubs, total gross pay, total net pay, and
# the average net pay) as a string with appropriate labels and formatting.
