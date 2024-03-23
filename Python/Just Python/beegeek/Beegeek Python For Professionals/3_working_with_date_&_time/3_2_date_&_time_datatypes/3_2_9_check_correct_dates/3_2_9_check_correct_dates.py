'''
TODO:   
        Write a program that takes a sequence of dates as input and checks each of them for correctness.

        The input to the program is a sequence of dates in the format DD.MM.YYYY, each on a separate line. The end of the sequence is the word end.

        For each date entered, the program should display the text Correct or Incorrect, depending on whether the date is correct, and then display the number of correct dates.

NOTE:
        To analyze the date for correctness, you can use the already implemented is_correct() function from the previous task.
'''
from datetime import date

def is_correct(day, month, year):
    try:
        new_date = date(year, month, day)
        return True
    except ValueError:
        return False

def check_correct_dates():
    correct_dates_counter = 0

    while True:
        current_date_components = input().split('.')

        if 'end' in current_date_components:
            break
        
        day, month, year = map(int, current_date_components)

        if is_correct(day, month, year):
            print('Correct')
            correct_dates_counter += 1
        else:
            print('Incorrect')

    print(correct_dates_counter)