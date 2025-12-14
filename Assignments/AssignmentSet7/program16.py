# Description: Module to run the food ordering program.
# Developer: Sif Oberon
# Date Created: 12.7.2025
# Date Last Modified: 12.14.2025

from order import Order
from combo_menu import Combo_Menu
from order_manager import Order_Manager

# module level variable
an_order_manager = None

def main():
    # print header
    print('Ordering Program')
    # call function to create an order manager object
    create_order_manager_object()
    # display menu for user choice
    display_menu()


# a function to create/instantiate an order manager object and assign it to the module level variable
def create_order_manager_object():
    global an_order_manager
    an_order_manager = Order_Manager()
    # call the function to display a menu
    display_menu()

# function to display the menu of options
def display_menu():
    print("\n--------- Menu ---------")
    print("1 - Add an order")
    print("2 - Display all orders")
    print("3 - Highest order total")
    print("4 - Average order total for a combo menu item")
    print("5 - Display sum of order totals per combo menu item")
    print("6 - Save orders")
    print("7 - Exit")
    
    while True:
        try:
            user_selection = int(input("Enter your choice (1-7): "))
            if 1 <= user_selection <= 7: 
                break
        except:
            print("Input error")

    # call method to get user selection
    call_menu_function(user_selection)

# method to call appropriate function based on user selection
def call_menu_function(user_selection):
    match user_selection:
        case 1: add_an_order()
        case 2: display_all_orders()
        case 3: highest_order_total()
        case 4: average_order_total_for_combo_item()
        case 5: display_sum_order_totals_per_combo_item()
        case 6: save_orders()
        case 7: exit_application()

# function to add an order
def add_an_order():
    customer_name = input("Enter customer's name (letters, spaces and hyphens only): ").strip()
    combo_choice = get_combo_choice()
    if combo_choice is None:
        return
    try:
        quantity = int(input("Enter the quantity for combo menu choice (1-25): "))
        if quantity <= 0 or quantity > 25:
            raise ValueError
    except ValueError:
        print("Quantity must be a choice between 1 - 25.")
        display_menu()

    order_object = an_order_manager.create_order_object(
        customer_name, combo_choice, quantity)
    print(order_object)

    # display menu for user again
    display_menu()

# function to get combo choice from user
def get_combo_choice():
    print("\nCombo Menu:")
    for combo in Combo_Menu:
        print(f"{combo.value}) {combo.name.title()}")
    try:
        choice = int(input("Enter 1-5 for the combo menu choice (1-Box, 2-Caniac, 3-Fingers, 4-Sandwich, 5-Kids): "))
        return Combo_Menu(choice)
    except (ValueError, KeyError):
        print("Invalid selection.")
        display_menu()
    # display menu for user again
    display_menu()

def display_all_orders():
    # retrieve all orders by calling the get_all_orders() function from order_manager module
    all_orders = an_order_manager.get_all_orders()
    print(all_orders)
    # display menu for user again
    display_menu()

def highest_order_total():
    highest_order_total = an_order_manager.get_highest_order_total()
    print(highest_order_total)

    # display menu for user again
    display_menu()

def average_order_total_for_combo_item():
    combo_choice = get_combo_choice()
    # if combo choice is None, end
    if combo_choice is None:
        return
    average_order_total = an_order_manager.calc_average_order_total_for_combo_item(combo_choice=combo_choice)
    print(average_order_total)

    # display menu for user again
    display_menu()
    

# display sum of order totals for each combo menu item
def display_sum_order_totals_per_combo_item():
    combo_sum = an_order_manager.sum_all_order_totals_per_combo_item()

    # check if combo_sum is a list, if so, prints it joined with other items
    if isinstance(combo_sum, list):
        print("\n".join(combo_sum))
    # else print the single item
    else:
        print(combo_sum)
    # display menu for user again
    display_menu()

# save orders
def save_orders():
    user_response = input("Do you wish to save orders to a file (Y or N)?: ")
    if user_response.upper() == "Y":
        # save orders using the Order_Manager method
        saved_check = an_order_manager.check_if_orders()
        print(saved_check)
        print("Orders saved.")
    else:
        print("Orders not saved.")
    # display menu for user again
    display_menu()

# function to exit the application
def exit_application():
    user_response = input("Would you like to exit the application? (Y / N): ")

    if user_response.upper() == "Y":
        # if yes, exit the application with a message to the user
        print("Program ended.")
        exit()
    else:
        # else, call the function to display the menu
        display_menu()

main()


