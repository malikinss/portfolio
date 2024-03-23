'''
TODO:   
        A sequence of dates is given. 
        Write a program that creates and displays a list whose elements are nonnegative integers—the number of days between two adjacent dates in the sequence.

NOTE:
        The dates in the sequence can be in any order, that is, it is not guaranteed that the next date is greater than the previous one.

        If the sequence consists of a single date, then the program should output an empty list.

'''
from datetime import datetime

DATE_FORMAT = '%d.%m.%Y'

def get_user_dates():
    while True:
        user_input = input("Enter dates (DD.MM.YYYY format), separated by spaces: ").split()

        try:
            dates = []

            for record in user_input:
                new_date = datetime.strptime(record, DATE_FORMAT)
                dates.append(new_date)

            return dates    

        except ValueError:
            print('Invalid date format. Please use the format DD.MM.YYYY')

def calculate_days_difference(given_dates):
    days_difference = []

    for date1, date2 in zip(given_dates[:-1], given_dates[1:]):
        number_of_days = abs((date1 - date2).days)
        days_difference.append(number_of_days)

    return days_difference    

def main():
    user_dates = get_user_dates()

    if len(user_dates) > 1:
        days_diff = calculate_days_difference(user_dates)
        print(days_diff)
    else:
        print([])

if __name__ == "__main__":
    main()