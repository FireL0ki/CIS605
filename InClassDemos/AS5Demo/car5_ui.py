from car5 import Car5

# declare module level variable
a_car = None

def main():
    print("Car 5 Example\n")
    get_user_inputs()

def get_user_inputs():
    try:
        while True:
            horsepower = int(input("Enter horse power between 100-300: "))
            # if user input a value within the correct range, break out of the try loop
            if 100 <= horsepower <= 300: break
    except:
        print("Input error")
        get_user_inputs()
    else:
        create_object(horsepower)

def create_object(horsepower):
    global a_car
    a_car = Car5(horsepower)
    display_menu()


def display_menu():
    print("\n--------- Menu ---------")
    print("1 - Display car's status")
    print("2 - Increase speed")
    print("3 - Decrease speed")
    print("4 - Speed up")
    print("5 - Slow down")
    print("6 - Create another car5")
    print("7 - Exit")

    try:
        while True:
            selection = int(input("Enter our choice (1-7): "))
            if 1 <= selection <= 7: break
    except:
        print("Input error")
        call_function(selection)

def call_function(choice):
    match choice:
        case 1: print_object()
        case 2: increase_speed()
        case 3: decrease_speed()
        case 4: speed_up()
        case 5: slow_down()
        case 6: create_another()
        case 7: exit_app()

def print_object():
    print(a_car)
    display_menu()

def increase_speed():
    try:
        while True:
            mph = int(input("Enter by how much you would like to increase the car speed (1 - 500): "))
            # if user input a value within the correct range, break out of the try loop
            if 1 <= mph <= 500: break
    except:
        print("Input error")
        increase_speed()
    else:
        print(a_car.increase_speed(mph))
        display_menu()

def decrease_speed():
    try:
        while True:
            mph = int(input("Enter by how much you would like to increase the car speed (1 - 500): "))
            # if user input a value within the correct range, break out of the try loop
            if 1 <= mph <= 500: break
    except:
        print("Input error")
        decrease_speed()
    else:
        print(a_car.decrease_speed(mph))
        display_menu()

# fill water tank
def speed_up():
    try:
        while True:
            mph = int(input("Enter mph to increase by between 1-500: "))
            if 1 <= mph <= 500: break
    except:
        print("Input error")
        speed_up()
    
    while True:
        if a_car.speed_up(mph):
            print(f"{a_car.current_speed} mph")
        else:
            print(f"Car has reached max speed or speec cannot be increased any further.")
        display_menu()

def speed_up():
    try:
        while True:
            mph = int(input("Enter mph to increase by between 1-500: "))
            if 1 <= mph <= 500: break
    except:
        print("Input error")
        speed_up()

    while True:
        if a_car.speed_up(mph):
            print(f"{a_car.current_speed} mph")
        else:
            print(f"Car has reached max speed or speec cannot be increased any further.")

def create_another():
    # input("Would you like to create another car? ")
    #  user already selected create_another() from menu
    get_user_inputs()