# Project:          Module 6 - Example 4
# Description:      Demos creating plots of list data using pyplot module of matplotlib package             
# Depends on:       matplotlib package
# Developed By:     LV
# Date:             October 2025

# install matplotlib - pip install matplotlib

# import the pyplot module

import matplotlib.pyplot as plt

# declare module-level list variables

years = []
prices = []

# entry point for program

print('Plots of Coffee Prices by LV')

def main():

   # call function to read year and price data from a file into lists
    
    read_data()
    
# read year and price data from a file into lists

def read_data():

    # to modify the module-level variables, thay must be declared as global within the function

    global years
    global prices
    
    try:

        with open('coffee_prices.csv', 'r') as infile: # open the prices.csv in read mode
            lines = infile.readlines()

        # for each line of data, strip any leading or trailing characters, split the year and price
        # convert and append the data to the two lists 
        
        for line in lines:
            values = line.strip().split(',')
            years.append(int(values[0]))
            prices.append(float(values[1]))
        
    except FileNotFoundError as e:
        print(e)

    except ValueError as e:
        print(e)

    except Exception as e:
        print(e)
    
    print(years)
    print(prices)

    # call methods on object and print returned values

    call_plot_methods()

# function to call methods on object and print returned values

def call_plot_methods():
    
    create_line_graph()
    create_bar_chart()
    create_pie_chart()
   
def create_line_graph():

    plt.figure(figsize=(16, 10))

    plt.plot(years, prices, marker='D')

    plt.title("Average Price of Ground Roast Coffee Per Pound 2010-2025")

    plt.xlabel("Years")
    plt.ylabel("Price in US$")

    plt.xlim(xmin=2010, xmax=2025)
    plt.ylim(ymin=3.0, ymax=8.0)
    
    plt.grid(True)

    plt.show()

def create_bar_chart():

    plt.figure(figsize=(16, 10))
    
    plt.bar(years, prices, color=("pink", "beige", "black", "blue", "brown", "coral", "crimson", "cyan", "fuchsia", "green", "indigo", "yellow", "maroon", "orange","orchid", "red"))

    plt.title("Average Price of Ground Roast Coffee Per Pound 2010-2025")

    plt.xlabel("Years")
    plt.ylabel("Price in US$")

    plt.xlim(xmin=2010, xmax=2025)
    plt.ylim(ymin=3.0, ymax=8.0)
    
    plt.grid(True)

    plt.show()

def create_pie_chart():

    production = [66.4, 30.1, 12.9, 10.9, 8.6]

    countries = ["Brazil", "Vietnam", "Colombia", "Indonesia", "Ethiopia"]

    colors = ("green", "gold", "yellow", "red", "blue") # example of a tuple

    plt.figure(figsize=(16, 10))
    
    plt.pie(production, labels = countries, colors = colors)

    plt.title("Coffee Production (millions of bags) by Country - 2025")

    plt.show()

# call main function

main()

