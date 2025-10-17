# Description: Gets user inputs on entree choices & drinks to calculate total cost
# Developer: Sif Oberon
# Date Created: 10.16.2025
# Date Last Modified: 10.17.2025

from catering_event import Catering_Event

def main():
    # module level variable for catering_event object
    my_catering_event = None

    print('Oberon Catering')

    get_user_catering_choices()


    def get_user_catering_choices():
        event_name = input('Enter the event name: ')
        number_guests = int(input('Enter the number of guests: '))
        entree_choice = input('Enter an entree choice of either steak, chicken, or pasta: ')
        open_bar = bool(input('Would you like an open bar?'))
        wine_with_dinner = bool(input('Would you like wine with dinner?'))

        create_catering_object(event_name, number_guests, entree_choice, open_bar, wine_with_dinner)


    # function to create catering event object
    def create_catering_object(event_name, number_guests, entree_choice, open_bar, wine_with_dinner):
        # ensure the program knows to update the module level variable
        global my_catering_event

        my_catering_event = Catering_Event(event_name=event_name, number_guests=number_guests, entree_choice=entree_choice, open_bar=open_bar, wine_with_dinner=wine_with_dinner)

        # call method ot print object
        print_catering_object()


    def print_catering_object():
        # print catering event object's state
        print(my_catering_event)

        # call method to check if user wants to update the catering object after seeing the object state
        check_if_update_catering_event()


    # check if the user would like to update the catering event
    def check_if_update_catering_event():
        update_catering_info = bool(input('Would you like to update any of the catering event details?'))
        if update_catering_info is True:
            update_catering_event()
        else:
            print('Thank you for choosing Oberon Catering!')


    def update_catering_event():
        new_event_name = input("Enter the event name: ")
        if new_event_name != "": my_catering_event.event_name = (new_event_name)

        # shortened using walrus operator :=
        if (new_event_name := (input("Enter the event name: "))) != "": my_catering_event.event_name = new_event_name

        if (new_number_guests := (input("Enter the number of guests: "))) != "": my_catering_event.number_guests = int(new_number_guests)

        if (new_entree_choice := (input('Enter an entree choice of either steak, chicken, or pasta: '))) != "": my_catering_event.entree_choice = new_entree_choice

        if (new_open_bar_choice := (bool(input('Would you like an open bar?')))) != "": my_catering_event.open_bar = new_open_bar_choice

        if (new_wine_choice := (input('Would you like wine with dinner??'))) != "": my_catering_event.open_bar = bool(new_wine_choice)
            
        # print the updated object's state
        print_catering_object()

    main()