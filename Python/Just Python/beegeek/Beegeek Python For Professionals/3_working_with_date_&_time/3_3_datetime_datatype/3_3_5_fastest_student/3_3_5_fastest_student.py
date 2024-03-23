'''
TODO:   
        Students at the BEEGEEK online school decided to find out which of them could solve their math homework the fastest.

        To do this, each student recorded the start and end time of solving their homework.

        You have access to a data dictionary containing student results.

        The key in the dictionary is the name of the student, and the value is a tuple, the first element of which is the start time of the solution, the second element is the end time of the solution.

        Complete the code below to display the name of the student who spent the least amount of time solving the homework problem.

NOTE:   
        It is guaranteed that the required student is unique.
        Date-times in tuples are presented as strings in the format DD.MM.YYYY HH:MM:SS

'''
from datetime import datetime

def convert_to_datetime(given_date):
    try:
        new_datetime = datetime.strptime(given_date, '%d.%m.%Y %H:%M:%S')
        return new_datetime
    except ValueError:
        print(f"Error: Invalid date-time format - {given_date}")
        return None

def get_seconds_per_user(data):
    seconds_per_user = {}

    for key, (start_time, end_time) in data.items():
        start_time_dt = convert_to_datetime(start_time).timestamp()
        end_time_dt = convert_to_datetime(end_time).timestamp()

        if start_time_dt is not None and end_time_dt is not None:
            seconds_to_solve = end_time_dt - start_time_dt
            seconds_per_user[key] = seconds_to_solve

    return seconds_per_user

def get_name_with_specific_value(given_dict, specific_value):
    for key, value in given_dict.items():
        if value == specific_value:
            return key

def fastest_student(data):
    student_solving_time = get_seconds_per_user(data)

    if not student_solving_time:
        return None
    
    min_time = min(student_solving_time.values())
    name = get_name_with_specific_value(student_solving_time, min_time)

    return name
    

data = {'Дима': ('03.11.2021 09:31:18', '03.11.2021 11:41:28'), 
        'Геор': ('01.11.2021 09:03:04', '01.11.2021 12:40:35'), 
        'Анна': ('02.11.2021 04:41:54', '02.11.2021 05:39:40'), 
        'Илина': ('02.11.2021 01:36:40', '02.11.2021 04:48:27'), 
        'Герман': ('04.11.2021 07:51:19', '04.11.2021 09:53:53'), 
        'Руслан': ('01.11.2021 11:26:06', '01.11.2021 12:56:24'), 
        'Лера': ('03.11.2021 11:09:41', '03.11.2021 14:37:41'), 
        'Егор': ('03.11.2021 05:29:38', '03.11.2021 06:01:59'), 
        'Максим': ('05.11.2021 13:05:03', '05.11.2021 14:27:41'), 
        'Саша': ('03.11.2021 04:14:26', '03.11.2021 05:10:58'), 
        'Марина': ('05.11.2021 15:21:06', '05.11.2021 18:33:46')}

result = fastest_student(data)

if result is not None:
    print(result)