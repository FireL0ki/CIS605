
# ➢ Try and except blocks for functions that get input from a user or data files
# Program 11



# Create another module (program11.py) that

# 7. Imports the Water_Tank class from the water_tank module
# 8. Has a module level variable (for referencing a water tank object) initialized to “None”
# 9. Has a “main” function” to
# a. print a suitable header
# b. call function (#4) that gets input for a water tank object
# 10. Has a function to
# a. get user input (using appropriate prompts and validation) for a water tank object (radius –
# int, minimum: 5, maximum: 50; depth – int, minimum: 10, maximum: 100)
# b. convert and assign the input values to variables
# c. call the function (#5) that creates/instantiates a water tank object
# 11. Has a function (with appropriate parameters) to
# a. create/instantiate a water tank object and assign it to the module level variable
# b. call the function (#6) to display a menu
# 12. Has a function to
# a. display the following menu of options:
# 1) Display water tank’s state
# 2) Add water to tank
# 3) Withdraw water from tank
# 4) Fill water tank
# 5) Drain water tank
# 6) Enter inputs for another water tank
# 7) Exit the application
# b. get the user’s choice (i.e., 1-7) with an appropriate prompt and validation
# c. call the function (#7) that calls the function associated with the user’s menu choice
# 13. Has a function (with appropriate parameter) to
# a. call the function associated with the user’s menu choice:
# 1 – function #8
# 2 – function #9
# 3 – function #10
# 4 – function #11
# 5 - function #12
# 6 - function #13
# 7 - function #14
# 14. Has a function to
# a. print the water_tank object’s state
# b. call the function (#6) to display the menu
# 15. Has a function to
# a. get user input (using an appropriate prompt and validation) for the gallons of water to add
# to the tank (int, minimum: 1, maximum: 6,000,000)
# b. call the method to add water and display the returned message
# c. call the function (#6) to display the menu
# 16. Has a function to
# a. get user input (using an appropriate prompt and validation) for the gallons of water to
# withdraw from the tank (int, minimum: 1, maximum: 6,000,000)
# b. call the method to withdraw water and display the returned message
# c. call the function (#6) to display the menu
# 17. Has a function to
# a. get user input (using an appropriate prompt and validation) for the rate (i.e.,
# gallons/second) at which to fill the tank (int, minimum: 1, maximum: 5000)
# b. call the method to fill water within the body of a loop; to keep things simple, assume each
# loop iteration takes a second; the loop should execute as long as the method returns a
# value of true; after each iteration display the current water level of the tank
# c. call the function (#6) to display the menu
# 18. Has a function to
# a. get user input (using an appropriate prompt and validation) for the rate (i.e.,
# gallons/second) at which to drain the tank (int, minimum: 1, maximum: 5000)
# b. call the method to drain water within the body of a loop; to keep things simple, assume
# each loop iteration takes a second; the loop should execute as long as the method returns
# a value of true; after each iteration display the current water level of the tank
# c. call the function (#6) to display the menu
# 19. Has a function to
# a. ask the user if they wish to create another water tank object
# b. if yes, call the function (#4) that gets input for a water tank object
# c. else, call the function (#6) to display the menu
# 20. Has a function to
# a. ask the user if they wish to exit the application
# b. if yes, exit the application (hint: import the sys module and use the exit function)
# c. else, call the function (#6) to display the menu
# 21. Calls the “main” function (#3)
# Water Tank By LV
# Enter a radius between 5 and 50 feet: 10
# Enter a depth between 10 and 100 feet: 20
# ---- Menu ----
# 1 - Display water tank's state
# 2 - Add water to tank
# 3 - Withdraw water from tank
# 4 - Fill water tank
# 5 - Drain water tank
# 6 - Enter inputs for another water tank
# 7 - Exit the application
# Enter your choice (1-7): 1
# Tank radius: 10 feet
# Tank depth: 20 feet
# Max capacity: 46,998 gallons
# Current water level: 0 gallons
# ---- Menu ----
# 1 - Display water tank's state
# 2 - Add water to tank
# 3 - Withdraw water from tank
# 4 - Fill water tank
# 5 - Drain water tank
# 6 - Enter inputs for another water tank
# 7 - Exit the application
# Enter your choice (1-7): 2
# Enter the gallons of water to add to the tank (1-6,000,000): 20000
# 20,000 gallons of water added
# Current water level of tank: 20,000 gallons
# ---- Menu ----
# 1 - Display water tank's state
# 2 - Add water to tank
# 3 - Withdraw water from tank
# 4 - Fill water tank
# 5 - Drain water tank
# 6 - Enter inputs for another water tank
# 7 - Exit the application
# Enter your choice (1-7): 3
# Enter the gallons of water to withdraw from the tank (1-6,000,000): 10000
# 10,000 gallons of water withdrawn
# Current water level of tank: 10,000 gallons
# ---- Menu ----
# 1 - Display water tank's state
# 2 - Add water to tank
# 3 - Withdraw water from tank
# 4 - Fill water tank
# 5 - Drain water tank
# 6 - Enter inputs for another water tank
# 7 - Exit the application
# Enter your choice (1-7): 4
# Enter the rate (gallons of water/second) to fill the tank (1-5,000): 1000
# 11,000 gallons
# 12,000 gallons
# 13,000 gallons
# 14,000 gallons
# 15,000 gallons
# 16,000 gallons
# 17,000 gallons
# 18,000 gallons
# 19,000 gallons
# 20,000 gallons
# 21,000 gallons
# 22,000 gallons
# 23,000 gallons
# 24,000 gallons
# 25,000 gallons
# 26,000 gallons
# 27,000 gallons
# 28,000 gallons
# 29,000 gallons
# 30,000 gallons
# 31,000 gallons
# 32,000 gallons
# 33,000 gallons
# 34,000 gallons
# 35,000 gallons
# 36,000 gallons
# 37,000 gallons
# 38,000 gallons
# 39,000 gallons
# 40,000 gallons
# 41,000 gallons
# 42,000 gallons
# 43,000 gallons
# 44,000 gallons
# 45,000 gallons
# 46,000 gallons
# Tank is either full or cannot add another 1,000 gallons
# ---- Menu ----
# 1 - Display water tank's state
# 2 - Add water to tank
# 3 - Withdraw water from tank
# 4 - Fill water tank
# 5 - Drain water tank
# 6 - Enter inputs for another water tank
# 7 - Exit the application
# Enter your choice (1-7): 1
# Tank radius: 10 feet
# Tank depth: 20 feet
# Max capacity: 46,998 gallons
# Current water level: 46,000 gallons
# ---- Menu ----
# 1 - Display water tank's state
# 2 - Add water to tank
# 3 - Withdraw water from tank
# 4 - Fill water tank
# 5 - Drain water tank
# 6 - Enter inputs for another water tank
# 7 - Exit the application
# Enter your choice (1-7): 5
# Enter the rate (gallons of water/second) at which to drain the tank (1-5,000): 1000
# 45,000 gallons
# 44,000 gallons
# 43,000 gallons
# 42,000 gallons
# 41,000 gallons
# 40,000 gallons
# 39,000 gallons
# 38,000 gallons
# 37,000 gallons
# 36,000 gallons
# 35,000 gallons
# 34,000 gallons
# 33,000 gallons
# 32,000 gallons
# 31,000 gallons
# 30,000 gallons
# 29,000 gallons
# 28,000 gallons
# 27,000 gallons
# 26,000 gallons
# 25,000 gallons
# 24,000 gallons
# 23,000 gallons
# 22,000 gallons
# 21,000 gallons
# 20,000 gallons
# 19,000 gallons
# 18,000 gallons
# 17,000 gallons
# 16,000 gallons
# 15,000 gallons
# 14,000 gallons
# 13,000 gallons
# 12,000 gallons
# 11,000 gallons
# 10,000 gallons
# 9,000 gallons
# 8,000 gallons
# 7,000 gallons
# 6,000 gallons
# 5,000 gallons
# 4,000 gallons
# 3,000 gallons
# 2,000 gallons
# 1,000 gallons
# 0 gallons
# Tank is either empty or cannot drain another 1,000 gallons
# ---- Menu ----
# 1 - Display water tank's state
# 2 - Add water to tank
# 3 - Withdraw water from tank
# 4 - Fill water tank
# 5 - Drain water tank
# 6 - Enter inputs for another water tank
# 7 - Exit the application
# Enter your choice (1-7): 1
# Tank radius: 10 feet
# Tank depth: 20 feet
# Max capacity: 46,998 gallons
# Current water level: 0 gallons
# ---- Menu ----
# 1 - Display water tank's state
# 2 - Add water to tank
# 3 - Withdraw water from tank
# 4 - Fill water tank
# 5 - Drain water tank
# 6 - Enter inputs for another water tank
# 7 - Exit the application
# Enter your choice (1-7): 6
# Do you wish to create another water tank (Y or N)?: n
# ---- Menu ----
# 1 - Display water tank's state
# 2 - Add water to tank
# 3 - Withdraw water from tank
# 4 - Fill water tank
# 5 - Drain water tank
# 6 - Enter inputs for another water tank
# 7 - Exit the application
# Enter your choice (1-7): 7
# Do you wish to exit the application (Y or N)?: y
# Program 12
# Create a module (projectile) for a Projectile class that has
# 1. 4 instance attributes
# a. initial height (private)
# b. initial velocity (private)
# c. maximum height (private)
# d. land time (private)
# Note: Assume the units of measurement for initial height will be feet and initial velocity will be
# feet per second
# 2. An initializer to
# a. initialize the initial height and initial velocity attributes with parameter values
# b. set the maximum height attribute by calling the appropriate method (#4)
# c. set the land time attribute by calling the appropriate method (#5)
# 3. A private instance method to calculate and returns the height (in feet) of the projectile at a certain
# time (in seconds) after it has been thrown straight up into the air.
# a. the formula for calculating the height of a projectile at a certain time (t seconds) after it
# has been thrown up is as follows:
# initial height + (initial velocity * t) – (16 * t^2)
# for example, if the initial height of the projectile is 6 feet and its initial velocity is 100
# feet per second, the height of the projectile at 3 seconds after it is thrown up, would be
# 6 + (100 *3) – (16 * 3^2) = 162 feet
# b. the method should receive the time (in seconds) as a parameter
# 4. A private instance method to calculate and return the maximum height of the projectile
# a. this method should use the method described in #3
# b. a projectile will reach its maximum height at initial velocity/32 seconds (for example, if
# the initial velocity of the projectile is 100 feet per second, it will reach its maximum
# height at 100/32 = 3.125 seconds
# 5. A private instance method to determine and return the approximate time (in seconds) when the
# projectile will hit the ground
# a. this method should use the method described in #3
# b. hint: set up a loop to determine the height of the projectile after every 0.01 second; when
# the height is no longer a positive number you can assume the projectile has hit the
# ground.
# 6. A __str__ method that returns relevant information about a projectile object’s state (i.e.,
# its attributes and their current values) as a string with appropriate labels and formatting.
# Create another module (program12.py) that
# 1. Imports the Projectile class from the projectile module
# 2. Has a module level variable (for referencing a projectile object) initialized to “None”
# 3. Has a “main” function” to
# a. print a suitable header
# b. call function (#4) that gets input for a projectile object
# 4. Has a function to
# a. get user input (using appropriate prompts and validation) for a projectile object (initial
# height – int, minimum: 1, maximum: 15; initial velocity – int, minimum: 10, maximum:
# 500)
# b. convert and assign the input values to variables
# c. call the function (#5) that creates/instantiates a projectile object
# 5. Has a function (with appropriate parameters) to
# a. create/instantiate a projectile object and assign it to the module level variable
# b. call the function to display the projectile object’s state (#6)
# 6. Has a function to
# a. print the projectile object’s state
# b. call the function (#7) to check if the user wishes to enter input for another projectile
# 7. Has a function to
# a. ask the user if they wish to create another projectile object
# b. if yes, call the function (#4) that gets input for a projectile object
# c. if no, exit the application
# 8. Calls the “main” function (#3)
# Projectile By LV
# Enter an initial height between 1 and 15 feet: 10
# Enter an initial velocity between 10 and 500 feet per second: 250
# Initial Height: 10 feet
# Initial Velocity: 250 feet per second
# Maximum Height: 986.56 feet
# Land Time: 15.67 seconds
# Do you wish to create another projectile (Y or N)?: y
# Enter an initial height between 1 and 15 feet: 15
# Enter an initial velocity between 10 and 500 feet per second: 500
# Initial Height: 15 feet
# Initial Velocity: 500 feet per second
# Maximum Height: 3,921.25 feet
# Land Time: 31.28 seconds
# Do you wish to create another projectile (Y or N)?: n
# Program 13
# Create a module (wimbledon_champions) for a class (Wimbledon_Champions) that has
# 1. 1 instance attributes
# a. champions (private)
# 2. An initializer to
# a. initialize the champions attribute with a parameter value
# 3. A public method (with one parameter for the name of a tennis player) to check and return the
# number of times the player has won the championship
# 4. A public method to find and return the number of times there have been back-to-back champions
# Create another module (program13.py) that
# 1. Imports the Wimbledon_Champions class from the wimbledon_champions module
# 2. Has a module level variable (for referencing a wimbledon champions object) initialized to
# “None”
# 3. Has a “main” function” to
# a. print a suitable header
# b. call function (#4) that gets data for a champions object
# 4. Has a function to
# a. get data from champions.txt and create a list of champions
# b. call the function (#5) that creates/instantiates a wimbledon champions object
# 5. Has a function (with an appropriate parameter) to
# a. create/instantiate a wimbledon champions object and assign it to the module level
# variable
# b. call the function (6) to display a menu
# 6. Has a function to
# a. display the following menu of options:
# 1) Display the number of times there have been back-to-back champions
# 2) Display the number of times a player has won the championship
# 3) Exit the application
# b. get the user’s choice (i.e., 1-3) with an appropriate prompt and validation
# c. call the function (#7) that calls the function associated with the user’s menu choice
# 7. Has a function (with appropriate parameter) to
# a. call the function associated with the user’s menu choice:
# 1 – function #8
# 2 – function #9
# 3 – function #10
# 8. Has a function to
# a. call the method that that returns the number of times there have been back-to-back
# champions and display the result with appropriate wording
# b. call the function (#6) to display the menu
# 9. Has a function to
# a. get user input (using an appropriate prompt) for a player’s name
# b. call the method that returns the number of times a player has won the championship and
# display the result with appropriate wording
# c. call the function (#6) to display the menu
# 10. Has a function to
# a. ask the user if they wish to exit the application
# b. if yes, exit the application
# c. else, call the function (#6) to display the menu
# Wimbledon Champions By LV
# ---- Menu ----
# 1 - Display the number of times there have been back-to-back champions
# 2 - Display the number of times a player has won the championship
# 3 - Exit the application
# Enter your choice (1-3): 1
# Players have won back-to-back championships 16 times
# ---- Menu ----
# 1 - Display the number of times there have been back-to-back champions
# 2 - Display the number of times a player has won the championship
# 3 - Exit the application
# Enter your choice (1-3): 2
# Enter a player's name: Steffi Graf
# Steffi Graf has won the championship 7 times
# ---- Menu ----
# 1 - Display the number of times there have been back-to-back champions
# 2 - Display the number of times a player has won the championship
# 3 - Exit the application
# Enter your choice (1-3): 2
# Enter a player's name: Venus Williams
# Venus Williams has won the championship 5 times
# ---- Menu ----
# 1 - Display the number of times there have been back-to-back champions
# 2 - Display the number of times a player has won the championship
# 3 - Exit the application
# Enter your choice (1-3): 2
# Enter a player's name: Coco Gauff
# Coco Gauff has won the championship 0 times
# ---- Menu ----
# 1 - Display the number of times there have been back-to-back champions
# 2 - Display the number of times a player has won the championship
# 3 - Exit the application
# Enter your choice (1-3): 3
# Do you wish to exit the application (Y or N)?: y
