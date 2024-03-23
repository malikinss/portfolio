'''
TODO:   
        A list of employees of the organization is given, which indicates their last names, given names and dates of birth. 
       
        Write a program that determines the youngest employee who celebrates his birthday within the next seven days from the current date.

        The input to the program in the first line is the current date in the format DD.MM.YYYY, in the next line the natural number n is entered - the number of employees working in the organization. 
       
        In the next n lines, data about each employee is entered: first name, last name and date of birth, separated by a space. Date of birth is indicated in the format DD.MM.YYYY.

        The program should determine the youngest employee celebrating his birthday within the next seven days, and display his first and last name, separated by a space. 
       
        If there are no such employees, the program should output the text:
            'No birthdays planned'

NOTE:       
        It is guaranteed that all employees have different dates of birth.

        For example, for the date 01.11.2021, the nearest seven days are:
            02.11.2021
            03.11.2021
            04.11.2021
            05.11.2021
            06.11.2021
            07.11.2021
            08.11.2021
'''
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

def generate_date_range(start_date, end_date):
    days_num = (end_date - start_date).days + 1
    dates_range = []

    for i in range(days_num):
        date = start_date + timedelta(days=i)
        dates_range.append(date)

    return dates_range        

def add_days_to_date(given_date, days_num):
    return given_date + timedelta(days=days_num)

def get_next_7_days(current_date):
    start = add_days_to_date(current_date, 1)
    end = add_days_to_date(current_date, 7)

    dates_range = generate_date_range(start, end)

    return dates_range

def format_dates_without_year(dates):
    new_list = []

    for current_date in dates:
        new_list.append(current_date.strftime('%d.%m'))

    return new_list    

def filter_employees_in_next_7_days(cur_date, employees_data):
    next_7_days = format_dates_without_year(get_next_7_days(cur_date))

    new_data = {}
    
    for employee, birthday in employees_data.items():
        bday_without_year_str = birthday.strftime('%d.%m')
        
        if bday_without_year_str in next_7_days:
            new_data[employee] = birthday

    return new_data

def get_key_by_value(given_dict, given_value):
    for key, value in given_dict.items():
        if value == given_value:
            return key

def find_youngest_employee(employees_data):
    lastest_birth_date = max(employees_data.values())
    youngest = get_key_by_value(employees_data, lastest_birth_date)

    return youngest

def data_is_empty(given_data):
    return len(given_data) == 0

def find_youngest_employee_with_birthday_in_next_7_days():
    current_date = parse_date(input())
    employees_birthdays = collect_employees_data(int(input()))
    this_week_birthdays = filter_employees_in_next_7_days(current_date, employees_birthdays)

    if data_is_empty(this_week_birthdays):
        print('No birthdays planned')
    else:
        print(find_youngest_employee(this_week_birthdays))

find_youngest_employee_with_birthday_in_next_7_days()