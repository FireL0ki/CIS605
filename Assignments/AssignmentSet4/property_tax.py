# Description: Class for a property tax object
# Developer: Sif Oberon
# Date Created: 10.16.2025
# Date Last Modified: 10.17.2025

from datetime import date

class Property_Tax:
    def __init__(self, property_owner_name, building_square_footage, land_square_footage, year_built, location):
        self.property_owner_name = property_owner_name
        self.building_square_footage = building_square_footage
        self.land_square_footage = land_square_footage
        self.year_built = year_built
        self.location = location
        self.__building_age = self.building_age
        self.__building_tax = self.__calc_building_tax()
        self.__land_tax = self.__calc_land_tax()
        self.__building_tax_deduction = self.__calc_building_tax_deduction()
        self.__land_tax_deduction = self.__calc_land_tax_deduction()
        self.__total_property_tax = self.__calc_total_property_tax()

    # region getters
    @property
    def building_age(self):
        current_year = date.today().year
        self.__building_age = current_year - self.year_built
        return self.__building_age
    
    @property
    def building_tax(self):
        return self.__building_tax
    
    @property
    def land_tax(self):
        return self.__land_tax
    
    @property
    def building_tax_deduction(self):
        return self.__building_tax_deduction
    
    @property
    def land_tax_deduction(self):
        return self.__land_tax_deduction
    
    @property
    def total_property_tax(self):
        return self.__total_property_tax
    
    # endregion getters

    # region instance methods
    def __calc_building_tax(self):

        PRICE_0_TO_1000_FEET_RATE = .72
        PRICE_OVER_1000_FEET_RATE = .74
        PRICE_OVER_2000_FEET_RATE = .76
        PRICE_OVER_3000_FEET_RATE = .78
        PRICE_OVER_4000_FEET_RATE = .80

        BASE_CHARGE_1001_TO_2000_FEET = 720
        BASE_CHARGE_2001_TO_3000_FEET = 1460
        BASE_CHARGE_3001_TO_4000_FEET = 2220
        BASE_CHARGE_OVER_4000_FEET = 3000

        TOTAL_COST_FIRST_1000_SQUARE_FEET = 1000 * PRICE_0_TO_1000_FEET_RATE
        TOTAL_COST_1001_TO_2000_SQUARE_FEET = 1000 * PRICE_OVER_1000_FEET_RATE
        TOTAL_COST_2001_TO_3000_SQUARE_FEET = 1000 * PRICE_OVER_2000_FEET_RATE
        TOTAL_COST_3001_TO_4000_SQUARE_FEET = 1000 * PRICE_OVER_3000_FEET_RATE

        if self.building_square_footage <= 1000:
            building_tax = self.building_square_footage * PRICE_0_TO_1000_FEET_RATE
            return building_tax
        
        elif self.building_square_footage <= 2000:
            # number of square feet over 1000
            amount_square_footage_over_1000 = self.building_square_footage - 1000
            # calculate cost of the number of square feet over 1000 square feet
            calculated_cost_of_square_feet_over_1000 = amount_square_footage_over_1000 * PRICE_OVER_1000_FEET_RATE
            # Building tax = base_charge + square footage cost for 0 to 1000 + square footage cost for any footage over 1000 square feet
            building_tax = BASE_CHARGE_1001_TO_2000_FEET + TOTAL_COST_FIRST_1000_SQUARE_FEET + calculated_cost_of_square_feet_over_1000

            return building_tax
        
        elif self.building_square_footage <= 3000:
            amount_square_footage_over_2000 = self.building_square_footage - 2000
            calculated_cost_of_square_feet_over_2000 = amount_square_footage_over_2000 * PRICE_OVER_2000_FEET_RATE

            first_2000_feet_cost = TOTAL_COST_FIRST_1000_SQUARE_FEET + TOTAL_COST_1001_TO_2000_SQUARE_FEET
            building_tax = BASE_CHARGE_2001_TO_3000_FEET + first_2000_feet_cost + calculated_cost_of_square_feet_over_2000

            return building_tax
        
        elif self.building_square_footage <= 4000:
            amount_square_footage_over_3000 = self.building_square_footage - 3000
            calculated_cost_of_square_feet_over_3000 = amount_square_footage_over_3000 * PRICE_OVER_3000_FEET_RATE

            first_3000_feet_cost = TOTAL_COST_FIRST_1000_SQUARE_FEET + TOTAL_COST_1001_TO_2000_SQUARE_FEET + TOTAL_COST_2001_TO_3000_SQUARE_FEET

            building_tax = BASE_CHARGE_3001_TO_4000_FEET + first_3000_feet_cost + calculated_cost_of_square_feet_over_3000
            
            return building_tax

        elif self.building_square_footage > 4000:
            amount_square_footage_over_4000 = self.building_square_footage - 4000
            calculated_cost_of_square_feet_over_4000 = amount_square_footage_over_4000 * PRICE_OVER_4000_FEET_RATE

            first_4000_square_feet_cost = TOTAL_COST_FIRST_1000_SQUARE_FEET + TOTAL_COST_1001_TO_2000_SQUARE_FEET + TOTAL_COST_2001_TO_3000_SQUARE_FEET + TOTAL_COST_3001_TO_4000_SQUARE_FEET

            building_tax = BASE_CHARGE_OVER_4000_FEET + first_4000_square_feet_cost + calculated_cost_of_square_feet_over_4000

            return building_tax
        
    def __calc_land_tax(self):
        TIER_0_RATE = .03  # 1 to 10000
        TIER_1_RATE = .05  # 10001 to 20000
        TIER_2_RATE = .07  # 20001 to 30000
        TIER_3_RATE = .09  # 30001 to 40000
        TIER_4_RATE = .11  # > 40000

        BASE_CHARGE_TIER_1 = 300   # 10001 to 20000
        BASE_CHARGE_TIER_2 = 800   # 20001 to 30000
        BASE_CHARGE_TIER_3 = 1500  # 30001 to 40000
        BASE_CHARGE_TIER_4 = 2400  # > 40000

        TOTAL_COST_FIRST_10000_SQUARE_FEET = 10000 * TIER_0_RATE
        TOTAL_COST_10001_TO_20000_SQUARE_FEET = 10000 * TIER_1_RATE
        TOTAL_COST_20001_TO_30000_SQUARE_FEET = 10000 * TIER_2_RATE
        TOTAL_COST_30001_TO_40000_SQUARE_FEET = 10000 * TIER_3_RATE

        if self.land_square_footage <= 10000:
            land_tax = self.land_square_footage * TIER_0_RATE
            return land_tax
        
        elif self.land_square_footage <= 20000:
            amount_square_footage_over_10000 = self.land_square_footage - 10000
            calculated_cost_square_footage_over_10000 = amount_square_footage_over_10000 * TIER_1_RATE

            land_tax = BASE_CHARGE_TIER_1 + TOTAL_COST_10001_TO_20000_SQUARE_FEET + calculated_cost_square_footage_over_10000

            return land_tax
        
        elif self.land_square_footage <= 30000:
            amount_square_footage_over_20000 = self.land_square_footage - 20000
            calculated_cost_square_footage_over_20000 = amount_square_footage_over_20000 * TIER_2_RATE

            first_20000_square_feet_cost = TOTAL_COST_FIRST_10000_SQUARE_FEET + TOTAL_COST_10001_TO_20000_SQUARE_FEET

            land_tax = BASE_CHARGE_TIER_2 + first_20000_square_feet_cost + calculated_cost_square_footage_over_20000

            return land_tax
        
        elif self.land_square_footage <= 40000:
            amount_square_footage_over_30000 = self.land_square_footage - 30000
            calculated_cost_square_footage_over_30000 = amount_square_footage_over_30000 * TIER_3_RATE

            first_30000_square_feet_cost = TOTAL_COST_FIRST_10000_SQUARE_FEET + TOTAL_COST_10001_TO_20000_SQUARE_FEET + TOTAL_COST_20001_TO_30000_SQUARE_FEET

            land_tax = BASE_CHARGE_TIER_3 + first_30000_square_feet_cost + calculated_cost_square_footage_over_30000

            return land_tax
        
        elif self.land_square_footage > 40000:
            amount_square_footage_over_40000 = self.land_square_footage - 40000
            calculated_cost_square_footage_over_40000 = amount_square_footage_over_40000 * TIER_4_RATE

            first_40000_square_feet_cost = TOTAL_COST_FIRST_10000_SQUARE_FEET + TOTAL_COST_10001_TO_20000_SQUARE_FEET + TOTAL_COST_20001_TO_30000_SQUARE_FEET + TOTAL_COST_30001_TO_40000_SQUARE_FEET

            land_tax = BASE_CHARGE_TIER_4 + first_40000_square_feet_cost + calculated_cost_square_footage_over_40000

            return land_tax

    def __calc_building_tax_deduction(self):
        if self.building_age > 10:
            # 1/2 of 1 percent of the building tax is deducted for each eyar of the building's age
            PERCENTAGE = .005
            deduction_amount = self.building_age * (PERCENTAGE * self.building_tax)
            return deduction_amount
        return 0

    def __calc_land_tax_deduction(self):
        DEDUCTION_PERCENT_RATE_1 = .00245  # land sizes <=30000 square feet
        DEDUCTION_PERCENT_RATE_2 = .00175  # land sizes > 30000 square feet

        if self.location.upper() == "RURAL":
            if self.land_square_footage <= 30000:
                # calculate the deduction amount by multiplying the percentage rate * the land tax amount
                land_tax_deduction = self.land_tax * DEDUCTION_PERCENT_RATE_1
                return land_tax_deduction
            else:
                land_tax_deduction = self.land_tax * DEDUCTION_PERCENT_RATE_2
                return land_tax_deduction
        return 0
            
    def __calc_total_property_tax(self):
        # total property tax = building tax + land tax - building tax deduction - land tax deduction
        total_property_tax = self.building_tax + self.land_tax - self.building_tax_deduction - self.land_tax_deduction

        return total_property_tax
    
    def __str__(self):
        return f'Owner Name: {self.property_owner_name}\nBuilding Square Footage: {self.building_square_footage:,}\nLand Square Footage: {self.land_square_footage:,}\nYear Built: {self.year_built}\nProperty Location: {self.location}\nBuilding Age: {self.building_age}\nBuilding Tax: ${self.building_tax:,.2f}\nLand Tax: ${self.land_tax:,.2f}\nBuilding Tax Deduction: ${self.building_tax_deduction:,.2f}\nLand Tax Deduction: ${self.land_tax_deduction:,.2f}\nTotal Property Tax: ${self.total_property_tax:,.2f}'
            
# endregion instance methods
    


    

        