# Description: A module for a catering event class
# Developer: Sif Oberon
# Date Created: 10.16.2025
# Date Last Modified: 10.17.2025

class Catering_Event:
    # initialize attributes of new object
    def __init__(self, event_name, number_guests, entree_choice, open_bar, wine_with_dinner):
        self.event_name = event_name
        self.number_guests = number_guests
        self.entree_choice = entree_choice
        self.open_bar = open_bar
        self.wine_with_dinner = wine_with_dinner
        self.__entree_charge = self.__calc_entree_charge()
        self.__drinks_charge = self.__calc_drinks_charge()
        self.__surcharge = self.__calc_surcharge()
        self.__total_charge = self.__calc_total_charge()

    # region getters
    @property
    def entree_charge(self):
        return self.__entree_charge
    
    @property
    def drinks_charge(self):
        return self.__drinks_charge
    
    @property
    def surcharge(self):
        return self.__surcharge
    
    @property
    def total_charge(self):
        return self.__total_charge
    
    # # data validation for user inputs of entree_choice
    # @entree_choice.setter
    # def entree_choice(self, value):
    #     if self.entree_choice.upper() != "CHICKEN" or "STEAK" or "PASTA":
    #         raise ValueError("Entree choice must either be chicken, steak, or pasta.")
    #     self.entree_choice = value
    
    # endregion
    

    # region instance methods

    # get the entree cost per guest based on guest entree choice
    def __get_entree_charge_per_guest(self):   
        STEAK_COST = 63.94
        CHICKEN_COST = 45.27
        PASTA_COST = 28.51

        guest_entree_cost = 0

        match self.entree_choice:
            case "steak":
                guest_entree_cost = STEAK_COST
            case "chicken":
                guest_entree_cost = CHICKEN_COST
            case "pasta":
                guest_entree_cost = PASTA_COST
        
        return guest_entree_cost
    

    def __calc_entree_charge(self):
        entree_charge = self.number_guests * self.__get_entree_charge_per_guest()

        return entree_charge
    
    def __calc_drinks_charge(self):
        open_bar_charge = 56.87 * self.number_guests if self.open_bar else 0
        wine_with_dinner_charge = 39.24 * self.number_guests if self.wine_with_dinner else 0
        drinks_charge = open_bar_charge + wine_with_dinner_charge

        return drinks_charge
    
    def __calc_surcharge(self):

        if self.number_guests > 40 and self.open_bar is True:
            guests_over_40 = self.number_guests - 40
            surcharge = 25 * guests_over_40
            return surcharge
        else:
            return 0
        
    def __calc_total_charge(self):
        total_charge = self.entree_charge + self.drinks_charge + self.surcharge

        return total_charge
    
    def __str__(self):
        return f'Event Name: {self.event_name}\nNumber of Guests: {self.number_guests}\nEntree Choice: {self.entree_choice}\nOpen Bar: {self.open_bar}\nWine with Dinner: {self.wine_with_dinner}\nEntree Charge: ${self.entree_charge:,.2f}\nDrinks Charge: ${self.drinks_charge:,.2f}\nSurcharge: ${self.surcharge:,.2f}\nTotal Charge: ${self.total_charge:,.2f}'
        
    # endregion
        

    
