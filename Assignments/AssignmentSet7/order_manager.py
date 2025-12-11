# Description: 
# Developer: Sif Oberon
# Date Created: 12.7.2025
# Date Last Modified: 

# Create a module (order_manager) for a class (Order_Manager) that has
# 1. 1 class variable for the name of the file (ordersdata.dat) that will be used to store and retrieve order objects

# 2. 1 instance attribute
# o orders dictionary (private, getter) for storing order objects

# 3. An initializer to
# o that calls a private instance method to load order objects into the orders dictionary (see #4 below)

# 4. A private instance method to
# o check if the file (ordersdata.dat) exists
# o if the file exists, load the data into the orders dictionary
# o if the file does not exist, assign an empty dictionary to orders dictionary

# 5. A public instance method (with appropriate parameters) to
# o instantiate an order object and add it to the orders dictionary (use customer name as the key)
# o return a confirmation message

# 6. A public instance method to return all the orders in the orders dictionary. If there are no orders, return a suitable
# message.

# 7. A public instance method to find and return the highest order total among all the orders in the orders dictionary. If
# there are no orders, return a suitable message.

# 8. A public instance method (with an appropriate parameter) to calculate and return the average order total for a
# particular combo menu item (e.g., box). If there are no orders for the combo menu item, return a suitable message.

# 9. A public instance method to calculate and return the sum of all order totals for each combo menu item. If there are
# no orders, return a suitable message.

# 10. A public instance method to
# o check if there are orders in the orders dictionary
# o if there are orders, save the orders data to ordersdata.dat and return a confirmation message
# o if there are no orders, return a suitable message

