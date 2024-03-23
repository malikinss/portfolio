'''
TODO:   
        Implement a function calculate_it() that takes one or more arguments in the following order:
            func - arbitrary function
            *args - a variable number of positional arguments, each of which is an arbitrary object

        The function must return a tuple whose first element is the return value of func when called with *args, and the second element is the estimated time (in seconds) it took to calculate that value.
'''
import timeit
import time

def calculate_it(func, *args):
    start_time = time.perf_counter()
    func_result = func(*args)
    end_time = time.perf_counter()
    execution_time = (end_time - start_time)
    
    return (func_result, execution_time)

def calculate_it_2(func, *args):
    execution_time = timeit.timeit(lambda: func(*args), number=1)
    return func(*args), execution_time