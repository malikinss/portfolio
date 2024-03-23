'''
TODO:

        Let's search in the list and in the set; Let's create a million elements in each collection.

        To record the execution time of an operation, we import the built-in time module into the code.
'''

import time

def display_spent_time(start_time):
    print(time.time() - start_time)

def is_exist_and_display_time_to_find(collection, elem):
    start_time = time.time()

    print(elem in collection)
    display_spent_time(start_time)

    

elem = 1_954_365
num_set = set()
size = 10**6

for num in range(size):
    num_set.add(num)

is_exist_and_display_time_to_find(num_set, elem)

num_list = []

for num in range(size):
    num_list.append(num)

is_exist_and_display_time_to_find(num_list, elem)

num_list_set = set(num_list)

is_exist_and_display_time_to_find(num_list_set, elem)