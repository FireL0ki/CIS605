# Description: 
# Developer: Sif Oberon
# Date Created: 9.26.2025
# Date Last Modified:

from pay_stub import Pay_Stub


def main():
    # call method to get user inputs
    get_user_inputs()

# method to get employee’s name, hours worked (float), and pay rate (float) as user inputs & assign to variables
def get_user_inputs():
    employee_name = input("Enter your name: ")
    hours_worked = float(input("Enter the number of hours worked: "))
    pay_rate = float(input("Enter your pay rate: "))

    # create/instantiate a pay_stub object
    my_pay_stub = Pay_Stub(employee_name=employee_name, hours_worked=hours_worked, pay_rate=pay_rate)

    # print the pay_stub object
    print(my_pay_stub)

# call the class method that returns summary information and prints the result
    print(f'Summary Info: {my_pay_stub.summary_info()}')

# call the main function three times to verify that the summary information is correct
main()
main()
main()

