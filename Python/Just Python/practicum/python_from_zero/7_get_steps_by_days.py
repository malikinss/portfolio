'''
TODO:
        From a tuple and a list, create a list of tuples.

        The program receives a days tuple with a list of days of the week, a list of steps, which lists the number of steps taken by the user on the corresponding day; for example, steps[0] is the number of steps for Monday.

        The program should return a list of tuples, each containing two elements: the name of the day of the week and the number of steps for that day.
'''

def get_steps_by_days(days, steps):
    week_len = len(days)

    result = []

    for i in range(week_len):
        new_tuple = days[i], steps[i]
        result.append(new_tuple)

    return result


days = ('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday')
steps = [1500, 3445, 13222, 10000, 12555, 1300, 6000]

print(get_steps_by_days(days, steps))