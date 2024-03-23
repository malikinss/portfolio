'''
TODO:   
        Implement a function get_the_fastest_func() that takes two arguments in the following order:
            funcs — list of arbitrary functions
            arg - arbitrary object
        
        The get_the_fastest_func() function should return the function from the list of funcs that took the least amount of time to calculate the value when called with the arg argument.
'''
import timeit

def get_execution_time(func, *args):
    return timeit.timeit(lambda: func(*args), number=1)

def get_the_fastest_func(funcs, *arg):
    funcs_time = {}

    for current_func in funcs:
        funcs_time[current_func] = get_execution_time(current_func, arg)

    fastest_execution_time = min(funcs_time.values())

    for current_func, execution_time in funcs_time.items():
        if execution_time == fastest_execution_time:
            result = current_func

    return result        

def get_the_fastest_func_2(funcs, *arg):
    fastest_func = None
    fastest_execution_time = float('inf')

    for current_func in funcs:
        current_execution_time = get_execution_time(current_func, *arg)
        
        if current_execution_time < fastest_execution_time:
            fastest_execution_time = current_execution_time
            fastest_func = current_func

    return fastest_func