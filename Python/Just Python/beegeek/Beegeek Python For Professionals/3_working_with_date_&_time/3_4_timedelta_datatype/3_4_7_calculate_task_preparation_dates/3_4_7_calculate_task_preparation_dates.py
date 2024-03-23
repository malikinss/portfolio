'''
TODO:   
        Arthur needs to prepare 10 problems for the new course "OOP in Python".
        To prevent the task from being tedious, he came up with a rule:

            - if today he prepared the first task, then he should prepare the second in one day
            - if today he prepared the second task, then he should prepare the third in two days
            - if today he prepared the third task, then he must prepare the fourth in three days, and so on
        
        Write a program that determines the dates on which Arthur needs to prepare tasks.
 
'''
from datetime import datetime, timedelta

DATE_FORMAT = '%d.%m.%Y'

def get_user_date():
    """Prompt the user to input date and return as a datetime object."""
    while True:
        user_input = input('Please input the date in the format DD.MM.YYYY (e.g., 1.1.1995): ')
        try:
            return datetime.strptime(user_input, DATE_FORMAT)
        except ValueError:
            print('Invalid date format. Please use the format DD.MM.YYYY')

def calculate_task_preparation_dates(giving_date, number_of_tasks):
    cur_date = giving_date
    dates = [cur_date]

    for i in range(1, number_of_tasks):
        cur_date += timedelta(days=i+1)
        dates.append(cur_date)

    return dates    

def display_list(any_list):
    for record in any_list:
        print(record.strftime(DATE_FORMAT))


def main():
    user_date = get_user_date()
    dates_for_preparation = calculate_task_preparation_dates(user_date, 10)
    display_list(dates_for_preparation)

if __name__ == "__main__":
    main()