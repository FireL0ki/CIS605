# Description:      Functions for displaying greetings
# Purpose:          Demonstrate examples of simple functions
# Developed By:     LV

# a function with no parameters

def say_hello():
    return 'Hello!'

# a function with one parameter
# concatenates or joins "Goodbye" to the argument passed to the function and returns the concatenated string

def say_goodbye(name):
    return f'Goodbye, {name}!' # example of a F-string or formatted string literal; used to format output