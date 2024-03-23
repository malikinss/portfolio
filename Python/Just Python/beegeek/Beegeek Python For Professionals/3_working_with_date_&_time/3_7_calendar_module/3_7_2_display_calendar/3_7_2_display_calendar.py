'''
TODO:   
        Write a program that displays a calendar for a given year and month.
        
        The input to the program is the year and the abbreviated name of the month in English, separated by a space.

        The program should display a calendar for the entered year and month.
'''
import calendar

def display_calendar():

    user_input = input("Insert year and month name abbreviation (example, '2024 Jan'): ").split(' ')

    english_names = list(calendar.month_abbr)

    given_year = int(user_input[0])

    if user_input[1] not in english_names:
        print("Error: Wrong month name abbreviation")
    else:
        given_month = english_names.index(user_input[1])
        calendar.prmonth(given_year, given_month)

display_calendar()