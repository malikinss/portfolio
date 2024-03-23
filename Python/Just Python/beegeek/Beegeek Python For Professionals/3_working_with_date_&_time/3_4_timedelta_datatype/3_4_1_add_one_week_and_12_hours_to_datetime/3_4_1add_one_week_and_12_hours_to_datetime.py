'''
TODO:   
        Complete the code below to add one week and 12 hours to the datetime(2021, 11, 4, 13, 6) object and output the result in the format DD.MM.YYYY HH:MM:SS.       
'''
from datetime import datetime, timedelta

dt = datetime(2021, 11, 4, 13, 6) + timedelta(weeks=1, hours=12)

print(dt.strftime('%d.%m.%Y %H:%M:%S'))