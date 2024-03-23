'''
TODO:
        The working time tracking system stores on the server the time that employees spent on social networks during the month.
        HR decided to find out how long tester Anton spent scrolling through the feed with memes, but the server returned an incomprehensible number 424_562.
        HR read the system manuals and found out that the server stores time in seconds.
        HR has asked you to write an application that, using arithmetic operations, would convert the resulting number of seconds into the format days hours minutes seconds.
        Why not help a good person.
'''



SECONDS_IN_MINUTE = 60
MINUTES_IN_HOUR = 60
HOURS_IN_DAY = 24

SECONDS_IN_HOUR = SECONDS_IN_MINUTE * MINUTES_IN_HOUR
SECONDS_IN_DAY = SECONDS_IN_HOUR * HOURS_IN_DAY

def get_days(seconds):
    return seconds // SECONDS_IN_DAY

def get_hours(seconds):
    return seconds // SECONDS_IN_HOUR % HOURS_IN_DAY

def get_minutes(seconds):
    return seconds // MINUTES_IN_HOUR % SECONDS_IN_HOUR

def get_seconds(seconds):
    return seconds % SECONDS_IN_HOUR

response = 424_562

days = get_days(response)
hours = get_hours(response)
minutes = get_minutes(response)
seconds = get_seconds(response)

print(f'days: {days}, hours: {hours}, minutes: {minutes}, seconds: {seconds}')