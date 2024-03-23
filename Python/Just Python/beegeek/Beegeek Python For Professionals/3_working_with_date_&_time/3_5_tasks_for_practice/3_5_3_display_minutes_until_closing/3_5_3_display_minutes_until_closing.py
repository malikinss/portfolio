'''
TODO:   
       The store's operating hours are given.
       
       Write a program that takes the current date and time as input and determines the number of minutes remaining until the store closes.

       The program input is the current date and time in the format DD.MM.YYYY HH:MM.

       The program should display the number of minutes remaining until the store closes, or the text “The store is closed” if it is closed.
'''

from datetime import datetime

TIME_FORMAT = '%H:%M'
DATE_FORMAT = '%d.%m.%Y'

def parse_time(time_string):  
    try:
        return datetime.strptime(time_string, TIME_FORMAT).time()
    except ValueError:
        raise ValueError('Invalid time format. Please use the format HH:MM')

def parse_datetime(datetime_string):
    try:
        return datetime.strptime(datetime_string, f'{DATE_FORMAT} {TIME_FORMAT}')
    except ValueError:
        raise ValueError('Invalid datetime format. Please use the format DD.MM.YYYY HH:MM')    

def create_operating_hours():
    operating_hours = {}
    
    for day in ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']:
        operating_hours[day] = ('9:00', '21:00')
    
    for day in ['Saturday', 'Sunday']:
        operating_hours[day] = ('10:00', '18:00')
    
    return operating_hours      

def retrieve_operating_hours_for_date(current_date):
    operating_hours = create_operating_hours()

    current_weekday = current_date.strftime('%A')

    return operating_hours.get(current_weekday)

def is_store_open(current_time, start_time, end_time):
    after_opening = start_time.hour <= current_time.hour
    before_closing = end_time.hour > current_time.hour
    
    return after_opening and before_closing

def minutes_until_closing(current_dt, end_dt):
    return int((end_dt - current_dt).total_seconds() // 60)

def process_operating_hours(given_datetime):
    given_date = given_datetime.date()
    start_time_str, end_time_str = retrieve_operating_hours_for_date(given_date)

    start_time = parse_time(start_time_str)
    end_time = parse_time(end_time_str)

    start_dt = datetime.combine(given_date, start_time)
    end_dt = datetime.combine(given_date, end_time)

    return start_dt, end_dt

def display_minutes_until_closing(given_datetime_string):
    given_dt = parse_datetime(given_datetime_string)
    start_dt , end_dt = process_operating_hours(given_dt)

    if is_store_open(given_dt, start_dt, end_dt):
        remaining_minutes = minutes_until_closing(given_dt, end_dt)
        print(remaining_minutes)
    else:
        print('The store is closed')

datetime_string = input()
display_minutes_until_closing(datetime_string) 