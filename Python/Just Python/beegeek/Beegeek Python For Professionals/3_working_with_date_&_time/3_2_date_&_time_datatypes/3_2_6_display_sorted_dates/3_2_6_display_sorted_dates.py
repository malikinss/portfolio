'''
TODO:   
        Write a program that takes a sequence of dates as input and outputs them in non-decreasing order.

        The input to the program is a natural number n, and then n correct dates in ISO format (YYYY-MM-DD), each on a separate line.

        The program should output the entered dates in non-descending order, each on a separate line, in the format DD/MM/YYYY.

NOTE:
        A sequence is called non-decreasing if each next member is not less than the previous one, for example:
            1,1,2,3,4,4,4,5,6,...

        Please note that this sequence is not increasing.
'''
from datetime import date

def input_dates(dates_number):
    return [date.fromisoformat(input()) for _ in range(dates_number)]

def format_output_dates(dates):
    return [current_date.strftime('%d/%m/%Y') for current_date in dates]

def display_sorted_dates(dates_number):
    given_dates = input_dates(dates_number)
    sorted_dates = sorted(given_dates)
    formated_dates = format_output_dates(sorted_dates)
    
    print(*formated_dates, sep='\n')
