'''
TODO:   
        It is necessary to write a program that will read the city name and time from standard input and display information in the format “Current location is [Location] and time is [Time]”.

INPUT:
        location from user input
        time from user input

OUTPUT:
        Location and time indicated
'''
def display_location_and_time_message():
    location = input()
    time = input()

    print(f'Current location is {location} and time is {time}')

display_location_and_time_message()
