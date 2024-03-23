'''
TODO:   
        Complete the code below so that the dt variable contains a datetime object with the date and time specified in the text string.

NOTE:
        The date specified in the text line is written in the DD.MM.YYYY format, and the time is in the HH:MM format.
'''
from datetime import datetime

text = 'Dear patient, the doctor is ready to see you on 15.07.2022 at 08:30'

dt = datetime.strptime(text, 'Dear patient, the doctor is ready to see you on %d.%m.%Y at %H:%M')

print(dt)