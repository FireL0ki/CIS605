# Description:      Display greetings
# Purpose:          Demonstrate how to "import" a module and "call" functions
#                   "print" and "input" functions
#                   assigning a value to a "variable"
# Depends on:       greeter.py
# Developed By:     LV

import greeter as g # import the greeter module

print(g.say_hello()) #call the say_hello function

your_name = input('Enter your name: ') #get name as user input and assign it to a "variable"

print(g.say_goodbye(your_name)) #call the say_goodbye function and output the returned value    