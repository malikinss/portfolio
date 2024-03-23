'''
TODO:   
        Complete the code below to convert seconds (elapsed since the epoch) to a datetime object and, conversely, a datetime object to seconds (elapsed since the epoch).
'''
from datetime import datetime

seconds = 2483228800
dt = datetime(2011, 11, 4)

print(datetime.fromtimestamp(seconds))
print(dt.timestamp())