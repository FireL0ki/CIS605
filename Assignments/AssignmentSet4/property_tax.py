# Description: Class for a property tax object
# Developer: Sif Oberon
# Date Created: 10.16.2025
# Date Last Modified: 10.17.2025

from datetime import date

class Property_Tax:
    def __init__(self, property_owner_name, building_square_footage, land_square_footage, year_built, location, building_tax, land_tax, building_tax_deduction, land_tax_deduction, total_property_tax):
        self.property_owner_name = property_owner_name
        self.building_square_footage = building_square_footage
        self.land_square_footage = land_square_footage
        self.year_built = year_built
        self.location = location
        self.__building_age = self.__building_age
        self.__building_tax = self.__calc_building_tax()
        self.__land_tax = self.__calc_land_tax
        self.__building_tax_deduction = self.__calc_building_tax_deduction
        self.__land_tax_deduction = self.__calc_land_tax_deduction
        self.__total_property_tax = self.__calc_total_property_tax

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


    def __calc_building_tax(self):
        base_charge = 0
        price_per_square_foot = 0

        PRICE_0_TO_1000_FEET_RATE = .72
        PRICE_OVER_1000_FEET_RATE = .74
        PRICE_OVER_2000_FEET_RATE = .76
        PRICE_OVER_3000_FEET_RATE = .78
        PRICE_OVER_4000_FEET_RATE = .80

        BASE_CHARGE_0_TO_1000_FEET = 0
        BASE_CHARGE_1000_TO_2000_FEET = 720
        BASE_CHARGE_2000_TO_3000_FEET = 1460
        BASE_CHARGE_3000_TO_4000_FEET = 2220
        BASE_CHARGE_OVER_4000_FEET = 3000

        TOTAL_COST_FIRST_1000_SQUARE_FEET = 1000 * PRICE_0_TO_1000_FEET_RATE
        TOTAL_COST_1000_TO_2000_SQUARE_FEET = 1000 * PRICE_OVER_1000_FEET_RATE
        TOTAL_COST_2000_TO_3000_SQUARE_FEET = 1000 * PRICE_OVER_2000_FEET_RATE
        TOTAL_COST_3000_TO_4000_SQUARE_FEET = 1000 * PRICE_OVER_3000_FEET_RATE
        TOTAL_COST_OVER_4000_SQUARE_FEET = 1000 * PRICE_OVER_4000_FEET_RATE

        if self.building_square_footage < 1000:
            building_tax = self.building_square_footage * PRICE_0_TO_1000_FEET_RATE
            return building_tax
        
        elif self.building_square_footage < 2000:
            # number of square feet over 1000
            amount_square_footage_over_1000 = self.building_square_footage - 1000
            # calculate cost of the number of square feet over 1000 square feet
            calculated_cost_of_square_feet_over_1000 = amount_square_footage_over_1000 * PRICE_OVER_1000_FEET_RATE
            # Building tax = base_charge + square footage cost for 0 to 1000 + square footage cost for any footage over 1000 square feet
            building_tax = BASE_CHARGE_1000_TO_2000_FEET + TOTAL_COST_FIRST_1000_SQUARE_FEET + calculated_cost_of_square_feet_over_1000

            return building_tax
        
        elif self.building_square_footage < 3000:
            amount_square_footage_over_2000 = self.building_square_footage - 2000
            calculated_cost_of_square_feet_over_2000 = amount_square_footage_over_2000 * PRICE_OVER_2000_FEET_RATE

            first_2000_feet_cost = TOTAL_COST_FIRST_1000_SQUARE_FEET + TOTAL_COST_1000_TO_2000_SQUARE_FEET
            building_tax = BASE_CHARGE_2000_TO_3000_FEET + first_2000_feet_cost + calculated_cost_of_square_feet_over_2000

            return building_tax
        
        elif self.building_square_footage < 4000:
            amount_square_footage_over_3000 = self.building_square_footage - 3000
            calculated_cost_of_square_feet_over_3000 = amount_square_footage_over_3000 * PRICE_OVER_3000_FEET_RATE

            first_3000_feet_cost = TOTAL_COST_FIRST_1000_SQUARE_FEET + TOTAL_COST_1000_TO_2000_SQUARE_FEET + TOTAL_COST_2000_TO_3000_SQUARE_FEET

            building_tax = BASE_CHARGE_3000_TO_4000_FEET + first_3000_feet_cost + calculated_cost_of_square_feet_over_3000
            
            return building_tax

        elif self.building_square_footage > 4000:
            
