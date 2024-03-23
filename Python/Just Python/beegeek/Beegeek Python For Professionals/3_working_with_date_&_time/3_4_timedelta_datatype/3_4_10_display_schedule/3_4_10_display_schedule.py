'''
TODO:   
        A math tutor conducts lessons for 45 minutes with breaks of 10 minutes. 
        
        The tutor indicates the start time of the working day and the end time of the working day. 
        
        Write a program that generates and displays a class schedule.

NOTE:
        If a lesson is interrupted by the end time of work, then there is no need to add it to the schedule

        If the difference between the start and end times of the working day is less than 45 minutes, the program should not output anything.

'''
from datetime import datetime, timedelta

TIME_FORMAT = '%H:%M'

LESSON_DURATION = 45
BREAK_DURATION = 10

def get_time_from_string(string_time):
    try:
        return datetime.strptime(string_time, TIME_FORMAT)
    except ValueError:
        raise ValueError('Invalid time format. Please use the format HH:MM')
    
def get_string_from_time(datetime_time):
    return datetime.strftime(datetime_time, TIME_FORMAT)

def get_workday_duration_in_minutes(start_time, end_time):
    return int((end_time - start_time).total_seconds() / 60)

def is_short_workday(start_time, end_time):
    return get_workday_duration_in_minutes(start_time, end_time) < LESSON_DURATION

def calculate_number_of_lessons(start_time, end_time):
    total_workday_minutes =  get_workday_duration_in_minutes(start_time, end_time)

    classes_counter = 0
    time_counter = 0

    while time_counter + LESSON_DURATION <= total_workday_minutes:
        time_counter += LESSON_DURATION
        classes_counter += 1
        time_counter += BREAK_DURATION

    return classes_counter     

def get_lessons_schedule(start_time, number_of_lessons):
    current_time = start_time
    lessons_schedule = []

    for _ in range(number_of_lessons):
        lesson_end_time = current_time + timedelta(minutes=LESSON_DURATION)
        record = f"{get_string_from_time(current_time)} - {get_string_from_time(lesson_end_time)}"
        lessons_schedule.append(record)
        current_time = lesson_end_time + timedelta(minutes=BREAK_DURATION)

    return lessons_schedule    

def display_schedule():
    start_time = get_time_from_string(input())
    end_time = get_time_from_string(input())

    if start_time is None or end_time is None:
        return

    num_lessons = calculate_number_of_lessons(start_time, end_time)

    if is_short_workday(start_time, end_time) or 0 == num_lessons:
        return
    
    schedule = get_lessons_schedule(start_time, num_lessons)
    print(*schedule, sep='\n')

display_schedule()