'''
TODO:   
        Write a program that takes time as input and outputs the integer number of seconds that have passed since the beginning of the day.

NOTE:   
        The beginning of the day is considered to be the moment in time corresponding to 00:00:00    
'''

from datetime import datetime

TIME_FORMAT = '%H:%M:%S'

def get_user_time():
    """Prompt the user to input time and return as a datetime object."""
    user_input = input('Please input the time in the format HH:MM:SS: ')

    return datetime.strptime(user_input, TIME_FORMAT)

def get_time_since_midnight(current_time):
    """Calculate the time difference between the given time and midnight."""
    time_since_midnight = current_time - current_time.replace(hour=0, minute=0, second=0)

    return time_since_midnight

def print_seconds_since_midnight(giving_time):
    """Print the integer number of seconds that have passed since the beginning of the day."""
    time_since_midnight = get_time_since_midnight(giving_time)
    seconds_since_midnight = int(time_since_midnight.total_seconds())
    print(seconds_since_midnight)

giving_time = get_user_time()
print_seconds_since_midnight(giving_time)