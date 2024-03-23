'''
TODO:   
        You have access to a dates list containing dates and a times list containing times.

        The number of elements in these lists is the same.

        Complete the code below to output datetime objects obtained by concatenating the elements of the dates and times lists at the same positions.

        The resulting objects should be arranged in ascending seconds order, each on a separate line.

NOTE:   
        If objects have an equal number of seconds, then their original order should be preserved.

'''
from datetime import date, time, datetime

def combine_and_sort_dates_times(dates, times):
    datetime_objs = []

    for i in range(len(dates)):
        new_datetime = datetime.combine(dates[i], times[i])
        datetime_objs.append(new_datetime)

    sorted_datetimes = sorted(datetime_objs, key=lambda dt: dt.second)

    return sorted_datetimes

dates = [date(1793, 8, 23), date(1410, 3, 11), date(804, 11, 12), date(632, 6, 4),
         date(295, 1, 23), date(327, 8, 24), date(167, 4, 16), date(229, 1, 24), 
         date(1239, 2, 5), date(1957, 7, 14), date(197, 8, 24), date(479, 9, 6)]

times = [time(7, 33, 27), time(21, 2, 10), time(17, 20, 47), time(20, 8, 59), 
         time(12, 42, 56), time(15, 9, 57), time(17, 47, 9), time(9, 40, 2), 
         time(11, 47, 1), time(17, 27, 10), time(17, 55, 40), time(9, 14, 9)]

print(*combine_and_sort_dates_times(dates, times), sep='\n')