'''
TODO:   
        During the visit of the next guest, hotel staff have to check whether a particular date is available for booking a room.

        Implement a function is_available_date() that takes two arguments in the following order:

            - booked_dates -  is a list of string dates that are not available for booking. 
            The list element is either a single date or a period (two dates separated by a hyphen). 
            For example:
                ['04.11.2021', '05.11.2021-09.11.2021']

            - date_for_booking - a single string date or period (two dates separated by a hyphen) for which the guest wishes to book a room. 
            For example:
                '01.11.2021' or '01.11.2021-04.11.2021'

        The is_available_date() function must return True if the date or period date_for_booking is fully available for booking. 
        Otherwise the function must return False.        

NOTE:   
        It is guaranteed that in the period the left date is always less than the right one.

        In the period (two dates separated by a hyphen), boundary dates are included.
'''

from datetime import datetime, timedelta

def check_and_convert_to_list(data):
    if isinstance(data, str):
        return [data]
    elif isinstance(data, list):
        return data
    else:
        return None 

def convert_to_dt(given_date):
    return datetime.strptime(given_date, '%d.%m.%Y')

def split_date_range(date_range_str):
    start_date, end_date = map(lambda x: convert_to_dt(x), date_range_str.split('-'))
    dates = []

    cur_date = start_date
    
    while cur_date <= end_date:
        dates.append(cur_date)
        cur_date += timedelta(days=1)

    return dates

def get_range_dates_dt(dates):
    all_booked_dates = []

    for cur_date in dates:
        if '-' in cur_date:
            dates_range = split_date_range(cur_date)
            all_booked_dates.extend(dates_range)
        else:
            all_booked_dates.append(convert_to_dt(cur_date))

    return sorted(all_booked_dates)

def is_available_date(booked_dates, date_for_booking):
    booked_dates = check_and_convert_to_list(booked_dates)
    date_for_booking = check_and_convert_to_list(date_for_booking)

    all_booked_dates_dt = get_range_dates_dt(booked_dates)
    dates_for_booking_dt = get_range_dates_dt(date_for_booking)

    for cur_date_for_booking_dt in dates_for_booking_dt:
        if cur_date_for_booking_dt in all_booked_dates_dt:
            return False

    return True

dates = ['04.11.2021', '05.11.2021-09.11.2021']
some_date = '11.11.2021-15.11.2021'
print(is_available_date(dates, some_date))