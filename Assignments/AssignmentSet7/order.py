# Description: 
# Developer: Sif Oberon
# Date Created: 12.7.2025
# Date Last Modified: 

from combo_menu import Combo_Menu
# Create a module (order) for a class (Order) that has 4 instance attributes: 
# customer name (public), combo choice (public; type: Combo_Menu), quantity (public), order total (private, getter)
class Order:
    def __init__(self, customer_name: str, combo_choice: Combo_Menu, quantity: int, __order_total: float):
        self.customer_name = customer_name
        self.combo_choice = combo_choice
        self.quantity = quantity
        self.__order_total = self.__calc_order_total()


    # getter for order total should return the order total by calling the method that calculates it
    @property
    def order_total(self):
        return self.__order_total
    
    # private method to calculate and return the order total
    # o order total = price of combo choice * quantity
    # o combo choice prices: box: $12.99, caniac: $17.29, fingers: $10.39, sandwich: $11.79, kids: $6.99
    def __calc_order_total(self):
        # TODO
        BOX = 12.99
        CANIAC = 17.29
        FINGERS = 10.39
        SANDWICH = 11.79
        KIDS = 6.99

        order_total = self.combo_choice * self.quantity

        return order_total


    # __str__ method that returns relevant information about an order object’s state (i.e., its attributes and their current values) as a string with appropriate labels and formatting
    def __str__(self):
        # TODO
         return (
            f"Customer Name: {self.customer_name}\n"
            f"Combo Choice: {self.combo_choice.name.title()}\n"
            f"Quantity: {self.quantity}\n"
            f"Order Total: ${self.order_total:.2f}"
        )

