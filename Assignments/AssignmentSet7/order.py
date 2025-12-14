# Description: Module for a combo menu class
# Developer: Sif Oberon
# Date Created: 12.7.2025
# Date Last Modified: 12.14.2025

from combo_menu import Combo_Menu

# module (order) for a class (Order) that has 4 instance attributes: 
# customer name (public), combo choice (public; type: Combo_Menu), quantity (public), order total (private, getter)
class Order:
    def __init__(self, customer_name: str, combo_choice: Combo_Menu, quantity: int):
        self.customer_name = customer_name
        self.combo_choice = combo_choice
        self.quantity = quantity
        self.__order_total = self.__calc_order_total()

    # getter for order total returns the order total by calling the method that calculates it
    @property
    def order_total(self):
        return self.__order_total
    
    # helper method for displaying combo choice enums as user friendly strings
    @property
    def combo_name(self):
        return self.combo_choice.name.title()
    
    # private method to calculate and return the order total
    # o order total = price of combo choice * quantity
    # o combo choice prices: box: $12.99, caniac: $17.29, fingers: $10.39, sandwich: $11.79, kids: $6.99
    def __calc_order_total(self):
        prices = {
            Combo_Menu.BOX: 12.99,
            Combo_Menu.CANIAC: 17.29,
            Combo_Menu.FINGERS: 10.39,
            Combo_Menu.SANDWICH: 11.79,
            Combo_Menu.KIDS: 6.99
        }
        price = prices[self.combo_choice]

        order_total = price * self.quantity
        return order_total

    # __str__ method that returns relevant information about an order object’s state 
    def __str__(self):
         return (
            f"Customer Name: {self.customer_name} "
            f"Combo Choice: {self.combo_choice.name.title()} "
            f"Quantity: {self.quantity} "
            f"Order Total: ${self.order_total:.2f} "
        )

