'''
TODO:   
        The BEEGEEK team plans to release their new course on 08.11.2022 at exactly 12:00. 
        
        Write a program that takes the current date and time as input and determines how much time is left until the course is released.

        The program input is the current date and time in the format 
            'DD.MM.YYYY HH:MM'

        The program should output text indicating the number of days and hours remaining until the course is released, in the following format:
            'There are: <number of days> days and <number of hours> hours left until the course is released'

        If in this case the number of hours is zero, then only days need to be displayed.

        If the number of days is zero, then you only need to display the hours and minutes in the following format:
            'There are: <number of hours> hours and <number of minutes> minutes left until the course is released'
        
        If in this case the number of minutes is zero, then only the hours need to be displayed. Similarly, if the number of hours is zero, then only minutes need to be output.

        If the entered date and time is greater than or equal to 08.11.2021 12:00, the program should output the text:
            'The course is out now!'
'''
from datetime import date, time, datetime, timedelta

TIME_FORMAT = '%H:%M'
DATE_FORMAT = '%d.%m.%Y'
FULL_DAY_MINUTES = 60 * 24

CORRECT_WORDS = {'d':('день', 'дня', 'дней'),
                 'h':('час', 'часа', 'часов'),
                 'm':('минута', 'минуты', 'минут')}

    
def parse_datetime(datetime_string):
    try:
        return datetime.strptime(datetime_string, f'{DATE_FORMAT} {TIME_FORMAT}')
    except ValueError:
        raise ValueError('Invalid datetime format. Please use the format DD.MM.YYYY HH:MM') 

def choose_plural(amount, variants):
    if amount % 10 == 1 and amount % 100 != 11:
        variant = 0
    elif amount % 10 >= 2 and amount % 10 <= 4 and \
            (amount % 100 < 10 or amount % 100 >= 20):
        variant = 1
    else:
        variant = 2
    return '{} {}'.format(amount, variants[variant])

def is_not_released(date1, date2):
    return date1 > date2

def get_answer_for_remain_measure(remain_minutes, measure):
    return choose_plural(remain_minutes, CORRECT_WORDS[measure])

def get_answer_for_remain_hours(remain_hours):
    return choose_plural(remain_hours, CORRECT_WORDS['h'])

def get_expanded_answer(answer, part_to_expand):
    return answer + ' и ' + part_to_expand

def get_answer_if_remain_more_than_day(remain_days, remain_hours):
    result = get_answer_for_remain_measure(remain_days, 'd')
        
    if remain_hours > 0:
        part_to_expand = get_answer_for_remain_measure(remain_hours, 'h')
        result = get_expanded_answer(result, part_to_expand)

    return result

def get_answer_if_remain_less_than_day(remain_hours, remain_minutes):
    result = get_answer_for_remain_measure(remain_hours, 'h')
    
    if remain_minutes > 0:
        part_to_expand = get_answer_for_remain_measure(remain_minutes, 'm')
        result = get_expanded_answer(result, part_to_expand)

    return result    

def get_minutes_from_time(given_time):
    return given_time.seconds // 60 % 60

def get_hours_from_time(given_time):
    return given_time.seconds // 3600

def get_remain_time_dict(current_date, required_date):
    remain_time = {'days': 0,
                   'hours': 0,
                   'minutes': 0}
    
    remain_time_td = required_date - current_date
    remain_time['days'] = remain_time_td.days
    remain_time['hours'] = get_hours_from_time(remain_time_td)
    remain_time['minutes'] = get_minutes_from_time(remain_time_td)

    return remain_time

def display_time_to_release():
    now_date = parse_datetime(input())
    required_date = datetime(2022, 11, 8, 12)

    if is_not_released(required_date, now_date):
        remain_time = get_remain_time_dict(now_date, required_date)
        
        result = ''
        
        if remain_time['days'] > 0:
            result = get_answer_if_remain_more_than_day(remain_time['days'], remain_time['hours'])
        
        elif remain_time['hours'] > 0:
            result = get_answer_if_remain_less_than_day(remain_time['hours'], remain_time['minutes'])

        else:
            result = get_answer_for_remain_measure(remain_time['minutes'], 'm')
        
        print('До выхода курса осталось: ' + result)

    else:
        print('Курс уже вышел!')

display_time_to_release()