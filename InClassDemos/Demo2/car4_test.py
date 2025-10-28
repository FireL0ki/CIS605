from car4 import Car4 as car

def main():
    get_user_input()

def get_user_input():

    car_make = input("Make: ")
    car_model = input("Model: ")
    car_volume = float(input("Volume: "))
    car_type = input("Type: ")

    create_object(car_make, car_model, car_volume, car_type)

def create_object(make, model, volume, type):
    global my_car

    # try / except blocks when getting outside info / interacting with DB, getting user input
    try:
        my_car = car(make, model, volume, type)

    except(TypeError, ValueError) as e:
        print(f"Error: {e}")
        get_user_input()
    
    else:
        print_object()


def print_object():
    print(my_car)