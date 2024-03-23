'''
TODO:   
        Write a program that determines the number of days in a given month.

        The input to the program is the year and the full name of the month in English, separated by a space.

        The program should output a single number - the number of days in the entered month.       
'''
import calendar

def display_number_of_days_in_month(user_input):
    given_data = user_input.split()

    given_year = int(given_data[0]) 
    given_month_name = given_data[1]

    english_month_names = list(calendar.month_name)
    given_month_num = english_month_names.index(given_month_name)

    _, number_of_days = calendar.monthrange(given_year, given_month_num)

    print(number_of_days)
    
display_number_of_days_in_month(input())