# Project:          Module 4 - Example 1
# Description:      Class definition for Loan Application
# Demonstrates:     If, elif, else and match statements
# Developed By:     LV
# Date:             September 2025

class Loan_Application:

    # initializer

    def __init__(self, name, income, debt, type):
        
        self.applicant_name = name
        self.applicant_income = income
        self.applicant_debt = debt
        self.loan_type = type

    #getters and setters
    
    @property
    def loan_type(self):
        return self.__loan_type
    
    @loan_type.setter
    def loan_type(self, value):
        self.__loan_type = value.upper()
    
    @property
    def credit_rating(self):
        return self.__calc_credit_rating()
    
    @property
    def credit_score(self):
        return self.__calc_credit_score()
    
    #private instance methods

    def __calc_debt_to_income_ratio(self):
        
        return self.applicant_debt / self.applicant_income
    
    def __calc_credit_rating(self):

        # constants

        POOR = 0.50
        FAIR = 0.45
        GOOD = 0.40
        VERY_GOOD = 0.35
        EXCELLENT = 0.30
        
        # get debt to income ratio

        ratio = self.__calc_debt_to_income_ratio()

        rating = ""
        
        # if..elif..else statements
        
        if ratio <= EXCELLENT:
            rating = "A"
        elif ratio <=VERY_GOOD:
            rating = "B"
        elif ratio <= GOOD:
            rating = "C"
        elif ratio <= FAIR:
            rating = "D"
        elif ratio <= POOR:
            rating = "E"
        else:
            rating = "F"
        
        return rating

    def __calc_credit_score(self):

        score = 0

        # match statement
        
        match self.credit_rating:
            case "A":
                score = 760
            case "B":
                score = 680
            case "C":
                score = 520
            case "D":
                score = 450
            case "E":
                score = 370
            case _:
                score = 300
        
        return score
    
    # public instance methods

    def check_pre_qualification(self):

        # constant ratio for prequalification

        PRE_QUAL_RATIO = 0.425
        
        outcome = ""
        
        # get debt to income ratio

        ratio = self.__calc_debt_to_income_ratio()

        # if..else statements

        if ratio <= PRE_QUAL_RATIO:
            outcome = "Let's do business"
        else:
            outcome = "Sorry, we'll need more documentation"

        return outcome
    
    def is_pre_approved(self):

        # constant ratio for preapproval

        PRE_QUAL_RATIO = 0.375

        # get debt to income ratio

        ratio = self.__calc_debt_to_income_ratio()

        # ternary if
        
        outcome = "Yes" if ratio < PRE_QUAL_RATIO else "No"

        return outcome
    
    def determine_interest_rate(self):
        
        AUTO_LOW, HOME_LOW = 0.055, 0.05
        AUTO_MID, HOME_MID = 0.075, 0.07
        AUTO_HIGH, HOME_HIGH = 0.095, 0.09
                       
        rate = 0

        # nested if
        
        if self.loan_type == "AUTO":
            if self.credit_score >= 620:
                rate = AUTO_LOW
            elif self.credit_score >= 550:
                rate = AUTO_MID
            else:
                rate = AUTO_HIGH
        else:
            if self.credit_score >= 620:
                rate = HOME_LOW
            elif self.credit_score >= 550:
                rate = HOME_MID
            else:
                rate = HOME_HIGH

        return rate
    
    # alternate method with same functionality as above
    # if and elif statements with two conditions combined with the "and" operator

    def ascertain_interest_rate(self):
        
        AUTO_LOW, HOME_LOW = 0.055, 0.05
        AUTO_MID, HOME_MID = 0.075, 0.07
        AUTO_HIGH, HOME_HIGH = 0.095, 0.09
                       
        rate = 0

        if self.loan_type == "AUTO" and self.credit_score >= 620:
                rate = AUTO_LOW
        elif self.loan_type == "AUTO" and self.credit_score >= 550:
                rate = AUTO_MID
        elif self.loan_type == "AUTO" and self.credit_score < 550:
                rate = AUTO_HIGH
        elif self.loan_type == "HOME" and self.credit_score >= 620:
                rate = HOME_LOW
        elif self.loan_type == "HOME" and self.credit_score >= 550:
                rate = HOME_MID
        elif self.loan_type == "HOME" and self.credit_score < 550:
                rate = HOME_HIGH

        return rate
    
    def __str__(self):
         return f'Applicant Name: {self.applicant_name}\nApplicant Income: ${self.applicant_income:,}\nApplicant Debt: ${self.applicant_debt:,}\nLoan Type: {self.loan_type}\nCredit Rating: {self.credit_rating}\nCredit Score: {self.credit_score}'