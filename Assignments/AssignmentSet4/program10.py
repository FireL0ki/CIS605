# Description: Program that takes user inputs with property details and uses them to calculate property taxes
# Developer: Sif Oberon
# Date Created: 10.16.2025
# Date Last Modified: 10.19.2025

from property_tax import Property_Tax

# declare module level variable
my_property_tax = None

def main():
    print('Property Tax Calculator')

    get_user_tax_inputs()

# function to get user inputs & set as variables
def get_user_tax_inputs():
    property_owner_name = input("Enter the property owner name: ")
    building_square_footage = int(input("Enter the building's square footage: "))
    land_square_footage = int(input("Enter the land square footage: "))
    year_built = int(input("Enter the year built: "))
    property_location = input("Please enter the property location (Rural, Suburban, or Urban): ")
    validate_property_type(property_location)

    # instantiate property tax object
    create_property_tax_object(property_owner_name=property_owner_name, building_square_footage=building_square_footage, land_square_footage=land_square_footage, year_built=year_built, property_location=property_location)

# method to validate data for user input of property location type
def validate_property_type(property_type):
    type = property_type.upper()
    if type != "RURAL" and type != "SUBURBAN" and type != "URBAN":
        raise ValueError("Property location type must be either: Rural, Suburban, or Urban.")
    
# method to create new property tax object
def create_property_tax_object(property_owner_name, building_square_footage, land_square_footage, year_built, property_location):
    # use the module level declared variable
    global my_property_tax

    # create the object
    my_property_tax = Property_Tax(property_owner_name=property_owner_name, building_square_footage=building_square_footage, land_square_footage=land_square_footage, year_built=year_built, location=property_location)

    # call method to print object state
    print_tax_object()

def print_tax_object():
    print(my_property_tax)

    # check if user wishes to enter another property tax object
    check_if_additional_property_tax_object()

def check_if_additional_property_tax_object():
    check_for_additional = input("Would you like to enter details for another property tax object (Y or N)? ")

    if check_for_additional.upper() == "Y":
        get_user_tax_inputs()
    else:
        print("Thank you!")

main()