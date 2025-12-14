# Description: Module for the Order Manager class to save and manager order objects
# Developer: Sif Oberon
# Date Created: 12.7.2025
# Date Last Modified: 12.14.2025

import os
import pickle
from order import Order
from combo_menu import Combo_Menu

class Order_Manager:
    # class variable for the name of the file (ordersdata.dat) that will be used to store and retrieve order objects
    FILENAME: str ="ordersdata.dat"

    # initializer to that calls a private instance method to load order objects into the orders dictionary 
    def __init__(self):
        self.__orders_dictionary = self.__check_orders_dictionary()
    # 1 instance attribute: orders dictionary (private, getter) for storing order objects
    @property
    def orders_dictionary(self):
        return self.__orders_dictionary

    # private instance method to check if the file (ordersdata.dat) exists
    def __check_orders_dictionary(self):
        filename = Order_Manager.FILENAME
        # if the file exists, load the data into the orders dictionary
        if os.path.exists(filename):
            try:
                with open (filename, "rb") as file:
                    data = pickle.load(file)
                    return data
            except (EOFError, pickle.UnpicklingError):
                print("Could not read data file.")
        # if the file does not exist, assign an empty dictionary to orders dictionary
        else:
            return {}

    # public instance method (with appropriate parameters) to instantiate an order object and add it to the orders dictionary (use customer name as the key)
    def create_order_object(self, customer_name, combo_choice, quantity):
        new_order_object = Order(customer_name, combo_choice, quantity)
        # add to dictionary
        self.__orders_dictionary[customer_name] = new_order_object

        # return a confirmation message
        return f"Added - Customer Name: {customer_name}. Menu Choice: {new_order_object.combo_name} Combo Quantity: {new_order_object.quantity} Total: ${new_order_object.order_total:.2f}"


    # public instance method to return all the orders in the orders dictionary.
    def get_all_orders(self):
        # if there are no orders, return a suitable message
        if not self.__orders_dictionary:
            return "There are no orders to display."

        # empty list ot hold the orders from the dictionary
        orders = []
        # get all the orders from the dictionary and put them into a list
        for order in self.__orders_dictionary.values():
            orders.append(str(order))
        
        # return the list separated by new lines
        return "\n".join(orders)

    # public instance method to find and return the highest order total among all the orders in the orders dictionary
    def get_highest_order_total(self):
        # if there are no orders, return a suitable message
        if not self.__orders_dictionary:
            return "No orders currently in the system."

        highest = max(order.order_total for order in self.__orders_dictionary.values())
        return f"The highest order total among all the orders is: ${highest:.2f}"

    # public instance method to calculate and return the average order total for a particular combo menu item (e.g., box).
    def calc_average_order_total_for_combo_item(self, combo_choice):
        # if there are no orders, return a suitable message
        if not self.__orders_dictionary:
            return "No orders currently in the system."
        
        # get all orders for combo item
        combo_orders = [
            order.order_total
            for order in self.__orders_dictionary.values()
            if order.combo_choice == combo_choice
        ]
        if not combo_orders:
            return f"There are no orders for the combo item: {combo_choice}."
        # calculate average (sum of combo orders divided by the total number combo orders)
        avg_total = sum(combo_orders) / len(combo_orders)

        return f"The average order total for {combo_choice.name.title()} orders is: ${avg_total:.2f}"

    # public instance method to calculate and return the sum of all order totals for each combo menu item
    def sum_all_order_totals_per_combo_item(self):
        # if there are no orders, return a suitable message
        if not self.__orders_dictionary:
            return "No orders currently in the system."
        
        # initialize variables to store totals
        totals = {
            Combo_Menu.BOX: 0,
            Combo_Menu.CANIAC: 0,
            Combo_Menu.FINGERS: 0,
            Combo_Menu.SANDWICH: 0,
            Combo_Menu.KIDS: 0
        }

        # add up totals for each combo type
        for order in self.__orders_dictionary.values():
            totals[order.combo_choice] += order.order_total

        # create user friendly output of combo items totals
        orders = ["Sum of Order Totals:"]
        for combo, total in totals.items():
            orders.append(f"{combo.name} Combo: ${total:.2f}")

        return orders

    # public instance method to check if there are orders in the orders dictionary
    def check_if_orders(self):
        # if there are no orders, return a suitable message
        if not self.__orders_dictionary:
            return "There are no orders to save."
        # if there are orders, save the orders data to ordersdata.dat
        with open(self.FILENAME, "wb") as file:
            pickle.dump(self.__orders_dictionary, file)
        # return a confirmation message  
        return f"Orders have been saved to '{self.FILENAME}'."


