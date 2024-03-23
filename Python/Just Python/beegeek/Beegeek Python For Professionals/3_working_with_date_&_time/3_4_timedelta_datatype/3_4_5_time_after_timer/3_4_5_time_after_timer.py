'''
TODO:   
        Write a program that takes time as input and outputs the integer number of seconds that have passed since the beginning of the day.

NOTE:   
        The beginning of the day is considered to be the moment in time corresponding to 00:00:00    
'''

from datetime import datetime, timedelta

TIME_FORMAT = '%H:%M:%S'

def get_user_time():
    """Prompt the user to input time and return as a datetime object."""
    while True:
        user_input = input('Please input the time in the format HH:MM:SS (e.g., 10:15:30): ')
        try:
            return datetime.strptime(user_input, TIME_FORMAT)
        except ValueError:
            print('Invalid time format. Please use the format HH:MM:SS.')

def get_user_timer_duration():
    """Prompt the user to input timer duration in seconds and return as a timedelta object."""
    while True:
        user_input = input('Please input the timer duration in seconds: ')
        try:
            return timedelta(seconds=int(user_input))
        except ValueError:
            print('Invalid input. Please enter a valid integer number of seconds.')


def time_after_timer(current_time, timer_duration):
    """Calculate the time after the timer and print it."""
    time_after = current_time + timer_duration
    print('Time after the timer:', time_after.strftime(TIME_FORMAT))

current_time = get_user_time()
timer_duration = get_user_timer_duration()

time_after_timer(current_time, timer_duration)