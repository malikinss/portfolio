'''
TODO:   
       A list of employees of the organization is given, which indicates their last names, given names and dates of birth. 
       
       Write a program that determines the most senior employee from a given list.

       The input to the program in the first line is a natural number n - the number of employees working in the organization. 
       
       In the next n lines, data about each employee is entered: first name, last name and date of birth, separated by a space. 
       
       Date of birth is indicated in the format DD.MM.YYYY.

       The program should determine the oldest employee and display his date of birth, first and last name, separated by a space. 
       
       If there are several such employees, the program should display their date of birth, as well as their number, separated by a space.
NOTE:
        It is guaranteed that all employees have different first and last names.
'''

from datetime import datetime, timedelta

DATE_FORMAT = '%d.%m.%Y'
    
def parse_date(date_string):
    try:
        return datetime.strptime(date_string, DATE_FORMAT).date()
    except ValueError:
        raise ValueError('Invalid datetime format. Please use the format DD.MM.YYYY HH:MM')       

def get_employee_info():
    employee_name, employee_lastname, birthday_str = input().split(' ')

    employee = f"{employee_name} {employee_lastname}"
    birthday_date = parse_date(birthday_str)

    return employee, birthday_date

def get_all_employees_info(employees_num):
    employees_info = {}

    for _ in range(employees_num):
        employee, birthday = get_employee_info()
        employees_info[employee] = birthday

    return employees_info

def find_oldest_employees(employees_data):
    earliest_birthday = min(employees_data.values())

    oldest_employees = [employee for employee, birthday in employees_data.items() if birthday == earliest_birthday]

    return oldest_employees, earliest_birthday

def display_oldest_employee():
    employees_data = get_all_employees_info(int(input()))
    oldest_employees, oldest_birthday = find_oldest_employees(employees_data)

    oldest_employees_num = len(oldest_employees)
    oldest_birthday_str = oldest_birthday.strftime(DATE_FORMAT)

    if oldest_employees_num > 1:
        print(oldest_birthday_str, oldest_employees_num)
    elif oldest_employees_num == 1:
        print(oldest_birthday_str, *oldest_employees)

def main():
    display_oldest_employee()

    return 0

main()