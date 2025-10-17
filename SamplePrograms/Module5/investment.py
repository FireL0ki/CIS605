# Project:          Module 5 - Example 1
# Description:      Class definition for Investment
# Demonstrates:     Looping
# Developed By:     LV
# Date:             September 2025

class Investment:

    # initializer

    def __init__(self, amount, period, rate):
        
        self.__invest_amount = amount
        self.__invest_period = period
        self.__invest_rate = rate
    
    # getters
    
    @property
    def invest_amount(self):
        return self.__invest_amount
           
    @property
    def invest_period(self):
        return self.__invest_period
    
    @property
    def invest_rate(self):
        return self.__invest_rate
    
    @property
    def invest_future_value(self):
        
        # call private method to return the investment's future value property
        # the three methods (see below) demonstrate variations in loop statements
        
        # return self.__calc_fv_using_for_loop1()
        # return self.__calc_fv_using_for_loop2()
        return self.__calc_fv_using_while_loop()
            
    # private instance methods

    # for loop using the range function (with start and stop arguments)

    def __calc_fv_using_for_loop1(self):

        fv = self.invest_amount
        rate = self.invest_rate / 100 # convert percentage to decimal value

        # the range function generates a sequence of numbers 
        # the start value is the first number in the sequence; if start value is not specified, the sequence starts at 0
        # the stop value indicates the upper limit of the sequence; note: the sequence will stop before reaching this upper limit
        
        for p in range(1, self.invest_period + 1): # why is 1 added to the stop value? hint: see note above 
            
            interest = fv * rate # calculate interest for a period
            fv += interest # add the interest
            
            # the above two statements can be merged into one

            # fv += fv * rate
           
        return fv
 
    # for loop using the range function (with just stop argument)
    # demonstrates what happens within each iteration of the loop

    def __calc_fv_using_for_loop2(self):

        starting = self.invest_amount
        rate = self.invest_rate / 100

        print(f'Period\tStarting Balance\tInterest\tEnding Balance') # headers for the output

        for p in range(self.invest_period): # why is 1 not added to the stop value?
            
            interest = starting * rate # interest earned for a period = balance at the start of each period * interest rate
            ending = starting + interest # balance at the end of each period = starting balance + interest earned for the period
            
            # prints the state of variables (i.e., p, starting, interest, ending) in each iteration
            
            print(f'{p:>}\t{starting:>16.2f}\t{interest:>8.2f}\t{ending:>10.2f}') 

            starting = ending # starting balance for next period = ending balance for current period

        return ending
    
    # while loop

    def __calc_fv_using_while_loop(self):

        fv = self.invest_amount
        rate = self.invest_rate / 100
        
        n = 1 # counter variable to control the number of iterations

        while n <= self.invest_period:

            fv += fv * rate
            
            n += 1 # increment the counter variable by 1
        
        return fv
    
    def __str__(self):
         return f'Investment Amount: ${self.invest_amount:,.2f}\nInvestment Period: {self.invest_period:,} months\nInvestment Rate: {self.invest_rate:.2f}%\nFuture Value of Investment: ${self.invest_future_value:,.2f}'