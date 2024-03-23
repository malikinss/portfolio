'''
TODO:   
        Implement a get_min_max() function that takes one argument:
            dates — list of dates (date type)

        The function must return a tuple whose first element is the minimum date from the dates list, and the second element is the maximum date from the dates list.

        If the dates list is empty, the function should return an empty tuple.
'''
def get_min_max(dates):
    if dates:
        return min(dates), max(dates)
    return ()