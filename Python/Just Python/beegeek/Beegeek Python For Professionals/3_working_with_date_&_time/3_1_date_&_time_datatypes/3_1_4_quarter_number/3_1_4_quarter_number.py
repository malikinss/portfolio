'''
TODO:   
        You have access to a dates list containing dates.
        
        Complete the code below to print the year and quarter number of each date in the given list.
        
        The date components must be in their original order, each on a separate line, in the following format:
            <year>-Q<quarter number>        

'''
from datetime import date

dates = [date(2010, 9, 28), date(2017, 1, 13), date(2009, 12, 25), date(2010, 2, 27), date(2021, 10, 11), date(2020, 3, 13), date(2000, 7, 7), date(1999, 4, 14), date(1789, 11, 19), date(2013, 8, 21), date(1666, 6, 6), date(1968, 5, 26)]

quarters = {'Q1': [1, 2, 3], 'Q2': [4, 5, 6], 'Q3': [7, 8, 9], 'Q4': [10, 11, 12]}

for cur_date in dates:
    for cur_quarter_key, cur_quarter_value in quarters.items():
        if cur_date.month in cur_quarter_value:
            print(str(cur_date.year) + '-' + cur_quarter_key)