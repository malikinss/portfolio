'''
TODO:   
        The number 13 has long been considered diabolical. 
        
        This has its own explanation, and more than one: there are interpretations related to the Last Supper - where Christ and the 12 apostles were, one of whom became a traitor. 
        
        There is a belief that a Sabbath requires 12 witches and Satan. 
        
        In history, the number 13 in conjunction with Friday became “unlucky” in 1307, when King Philip the Fair of France gave the order to capture all the Templars - members of the knightly order of the crusaders. 
        All of them were burned at the stake of the Inquisition, and this happened on Friday, April 13.

        Prove that the 13th of the month most often falls on a Friday. 
        
        Write a program that calculates how many thirteenth numbers there are for each day of the week in the period from 01/01/0001 to 31/12/9999.

'''

from datetime import datetime, timedelta

def is_last_month(giving_date):
    is_last_year = giving_date.year == 9999
    is_december = giving_date.month == 12

    return is_last_year and is_december

def count_thirteenth_days(start_date, end_date):
    thirteen_dict = {'Monday': 0, 
                 'Tuesday': 0, 
                 'Wednesday':0, 
                 'Thursday': 0, 
                 'Friday': 0, 
                 'Saturday': 0, 
                 'Sunday': 0}
    
    # Set the current date to the 13th of the first month
    current_date = start_date

    if current_date.day <= 13:
        current_date = start_date.replace(day = 13)
    
    while current_date < end_date:
        if current_date.day == 13:
            current_date_weekday = current_date.strftime('%A')
            thirteen_dict[current_date_weekday] += 1

            if not is_last_month(current_date):
                # If not, move on to next month
                current_date += timedelta(days=27)
                continue
        
        current_date += timedelta(days=1)

    return thirteen_dict        

def display_dict_items(any_dict):
    for any_value in any_dict.values():
        print(any_value)

start_date = datetime(1,1,1)
end_date = datetime(9999,12,31)

display_dict_items(count_thirteenth_days(start_date, end_date))