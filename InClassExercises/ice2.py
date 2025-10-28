# Project:          In-class Exercise 2
# Purpose:          Practice for Looping Statements
# Developed By:     LV
# Date:             October 2025

# Write a function (with three parameters - for a product's current price, inflation rate (percentage), number of years) that prints, for each year (i.e., Year 1 to the number of years), the price of the product adjusted for inflation. Use a for loop. Assume inflation rate will be the same for all years.

def calc_product_price(price, rate, num_years):

    current_year = 1
    current_price = price

    # header
    print("Year\tPrice")
    print() # empty line for space

    for year in range(current_year, num_years+1):
        # 
        print(f"{year:<}\t${current_price:<,.2f}")

        current_price *= 1 + (rate/100)

        #long form of the above
        # inflation = current_price * (rate/100)
        # current_price = current_price + inflation


# Sample Output
# import ice2
# ice2.calc_product_price(10,5,10)

# Year    Price

# 1       $10.00
# 2       $10.50
# 3       $11.03
# 4       $11.58
# 5       $12.16
# 6       $12.76
# 7       $13.40
# 8       $14.07
# 9       $14.77
# 10      $15.51


        
    
# Write a function (with three parameters - for current tuition, tuition increase (percentage) per year, number of years in program) that prints, for each year in the program, the tuition amount. Use a while loop. Assume the tuition increase percentage will remain the same for all years.

# Sample Output

# import ice2
# ice2.calc_tuition(20000,3,4)

# Year    Tuition

# 1       $20,000.00
# 2       $20,600.00
# 3       $21,218.00
# 4       $21,854.54


        

# Write a function that uses a nested loop to print the following pattern:

# import ice2
# >>> ice2.print_pattern()

# * * * * * * *
# * * * * * *
# * * * * *
# * * * *
# * * *
# * *
# *



