'''
TODO:   
        Write a program that determines whether a year is a leap year.
        
        The input to the program in the first line is an integer n, in the next n lines natural numbers representing years are entered.

        For each year entered, the program must print True if it is a leap year, or False otherwise.

'''
import calendar

try:
    num_years = int(input("Enter the number of years: "))

    for _ in range(num_years):
        given_year = int(input("Enter year: "))
        # Print True if the year is a leap year, otherwise False
        print(calendar.isleap(given_year))

except ValueError:
    print("Invalid input. Please enter a valid integer for the number of years.")

