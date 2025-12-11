# Description: 
# Developer: Sif Oberon
# Date Created: 12.7.2025
# Date Last Modified: 


# module level variable (for referencing an order manager object) initialized to “None”
an_order_manager = None

def main():
    # print header
    print('Ordering Program')
    # call function to create an order manager object
    create_order_manager_object()


    # a function to create/instantiate an order manager object and assign it to the module level variable
    def create_order_manager_object():
        global an_order_manager
        # call the function to display a menu
        display_menu()


    # function to display the menu of options
    def display_menu():
        print("\n--------- Menu ---------")
        print("1) Add an order")
        print("2) Display all orders")
        print("3) Highest order total")
        print("4) Average order total for a combo menu item")
        
        try:
            while True:
                user_selection = int(input("Enter our choice (1-4): "))
                if 1 <= user_selection <= 4: break
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


    # 5) display sum of order totals for each combo menu item
    def display_sum_order_totals_per_combo_item():
        # TODO
        pass

    # 6) Save orders

    # 7) Exit the application


