'''
TODO:
        Write a program that will take as input a list of tuples of the form (<name>, <date of birth in the format DD.MM.YYYY>), determine how many days are left until the birthday and display a message for each entry:
             <name>, there are days left until your birthday: <days_until_birth_day>
'''
import datetime as dt

FORMAT = '%d.%m.%Y'

def get_days_to_bday(bday):
    today = dt.date.today()
    
    if bday > today:
        return None

    bday = bday.replace(year=today.year)

    if bday >= today:
        days_to_bday = bday - today
    else:
        bday = bday.replace(year=(bday.year + 1))
        days_to_bday = bday - today    
    
    return days_to_bday.days

def parse_birthday(bday_str):
    try:
        return dt.datetime.strptime(bday_str, FORMAT).date()
    except ValueError:
        print(f"Invalid date format: {bday_str}")
        return None
    
def display_msg(name, days):
    if days is None:
        print(f'{name}, has not yet been born')
    elif days == 0:
        print(f'{name}, happy birthday!')    
    else:
        print(f'{name}, there are days left until your birthday: {days}')

def display_days_to_birthday(data):
    for name, bday_str in data:
        try:
            bday = parse_birthday(bday_str)
            days_to_bday = get_days_to_bday(bday)
            display_msg(name, days_to_bday)
        
        except ValueError:
            print(f"Invalid date format for {name}'s birthday: {bday_str}")

test_data = [('Sam', '21.01.1998'), 
             ('Vova', '22.09.1993'), 
             ('Masha', '06.12.1993'),
             ('Maya', '03.07.2018'), 
             ('Lera', '25.06.1997'),
             ('Ariel', '23.03.2025'),
             ('Slava', '22.03.1997')]

display_days_to_birthday(test_data)
