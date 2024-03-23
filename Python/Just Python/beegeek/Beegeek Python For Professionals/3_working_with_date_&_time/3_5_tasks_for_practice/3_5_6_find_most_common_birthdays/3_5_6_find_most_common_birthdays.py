'''
TODO:   
       A list of employees of the organization is given, which indicates their last names, given names and dates of birth. 
       
       Write a program that determines which date has the most employees born.

       The input to the program in the first line is a natural number n - the number of employees working in the organization. 
       
       In the next n lines, data about each employee is entered: first name, last name and date of birth, separated by a space. 
       
       Date of birth is indicated in the format DD.MM.YYYY.

       The program should output the date on which the largest number of employees celebrate their birthdays, in the format DD.MM.YYYY. 
       
       If there are several such dates, the program should display them all in ascending order, each on a separate line, in the same format.
'''
from collections import Counter
from datetime import datetime, timedelta

DATE_FORMAT = '%d.%m.%Y'
    
def parse_date(date_string):
    try:
        return datetime.strptime(date_string, DATE_FORMAT).date()
    except ValueError:
        raise ValueError('Invalid datetime format. Please use the format DD.MM.YYYY HH:MM')   
        
def input_employee_data():
    employee_name, employee_lastname, birthday_str = input().split(' ')

    employee = f"{employee_name} {employee_lastname}"
    birthday_date = parse_date(birthday_str)

    return employee, birthday_date

def collect_employees_data(employees_num):
    employees = {}

    for _ in range(employees_num):
        employee, birthday = input_employee_data()
        employees[employee] = birthday

    return employees

def count_occurrences_per_date(dates_data):
    dates_counter = Counter(dates_data.values())

    return dates_counter

def get_most_common_dates(dates_count):
    max_occurance = max(dates_count.values())
    most_common_dates = [cur_date for cur_date, num_occurance in dates_count.items() if num_occurance == max_occurance]

    return most_common_dates        

def display_dates(popular_dates):
    for cur_date in sorted(popular_dates):
        cur_date_str = cur_date.strftime(DATE_FORMAT)
        print(cur_date_str)

def find_most_common_birthdays():
    employees = collect_employees_data(int(input()))
    dates_count = count_occurrences_per_date(employees)
    most_common_birtdays = get_most_common_dates(dates_count)

    return most_common_birtdays

display_dates(find_most_common_birthdays())