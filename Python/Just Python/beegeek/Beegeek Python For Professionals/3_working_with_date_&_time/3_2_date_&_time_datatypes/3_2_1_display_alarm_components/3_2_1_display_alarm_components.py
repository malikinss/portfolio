'''
TODO:   
        Alarm time is available to you.
        Complete the code below to output the following components:
            number of hours in HH format
            number of minutes in MM format
            number of seconds in SS format
'''
from datetime import time

alarm = time(7, 30, 25)

print('Hours:', alarm.strftime('%H'))
print('Minutes:', alarm.strftime('%M'))
print('Seconds:', alarm.strftime('%S'))
