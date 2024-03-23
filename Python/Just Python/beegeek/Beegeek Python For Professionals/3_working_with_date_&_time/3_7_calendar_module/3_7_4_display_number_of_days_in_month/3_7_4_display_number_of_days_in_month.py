'''
TODO:   
        Write a program that determines the number of days in a given month.

        The input to the program is the year and the serial number of the month (starting from 1), separated by a space.

        The program should output a single number - the number of days in the entered month.

NOTE:   
        January has a serial number of 1, February - 2, March - 3, and so on.        
'''
import calendar

def display_number_of_days_in_month(user_input):
    given_year, given_month = map(int, user_input.split())

    _, number_of_days = calendar.monthrange(given_year, given_month)

    print(number_of_days)
    
display_number_of_days_in_month(input())