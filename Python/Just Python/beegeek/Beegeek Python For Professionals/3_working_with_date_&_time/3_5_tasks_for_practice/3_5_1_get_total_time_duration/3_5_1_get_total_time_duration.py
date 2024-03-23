'''
TODO:   
        While solving the next problem, the programmer records the start and end times of its solution and adds the results obtained to the data list. 
        
        Each result is a tuple, the first element of which is the start time of the solution as a string in the HH:MM format, the second element is the end time of the solution as a string in the same format. 
        
        Complete the code below to print the total integer number of minutes the programmer spent solving all problems.

'''

from datetime import datetime, timedelta

TIME_FORMAT = '%H:%M'

def get_time_from_string(string_time):
    try:
        return datetime.strptime(string_time, TIME_FORMAT)
    except ValueError:
        raise ValueError('Invalid time format. Please use the format HH:MM')

def get_time_duration_for_one_task(task):
    start_time = get_time_from_string(task[0])
    end_time = get_time_from_string(task[1])

    # Ensure end time is after start time
    if end_time < start_time:
        raise ValueError('End time cannot be before start time.')

    time_duration = end_time - start_time

    return time_duration

def get_total_time_duration(data):
    total_time_duration = timedelta()

    for task_record in data:
        task_duration = get_time_duration_for_one_task(task_record)
        total_time_duration += task_duration

    total_minutes_duration = int(total_time_duration.total_seconds() // 60)

    return total_minutes_duration   

data = [('07:14', '08:46'),
        ('09:01', '09:37'),
        ('10:00', '11:43'),
        ('12:13', '13:49'),
        ('15:00', '15:19'),
        ('15:58', '17:24'),
        ('17:57', '19:21'),
        ('19:30', '19:59')]

print(get_total_time_duration(data))
