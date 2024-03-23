'''
TODO:   
        Implement the get_biggest() function, which takes one argument:
            numbers — a list of non-negative integers

        The function should return the largest number that can be made up of numbers from the numbers list. 
        If the numbers list is empty, the function should return the number -1.

NOTE:   
        Let's consider the first test with a list of numbers [1, 2, 3], from which the following numbers can be made: 
            123, 132, 213, 231, 312, 321
        The largest of the presented is 321.
'''

def get_numbers_as_str_list(numbers):
    """Converts a list of numbers to a list of strings."""
    return [str(number) for number in numbers]


def compare_elements(element1, element2):
    """Compares two elements based on their concatenation."""
    return element1 + element2 > element2 + element1


def find_max_index(numbers_as_str, start_index, end_index):
    """Finds the index of the maximum element within the given range."""
    max_index = start_index
    
    for j in range(start_index + 1, end_index):
        if compare_elements(numbers_as_str[j], numbers_as_str[max_index]):
            max_index = j
    
    return max_index


def swap_elements(numbers_as_str, index1, index2):
    """Swaps elements at the specified indices in the list."""
    numbers_as_str[index1], numbers_as_str[index2] = numbers_as_str[index2], numbers_as_str[index1]


def sort_numbers_for_maximum_combination(numbers_as_str):
    """Sorts the list of numbers in a way that ensures the maximum concatenation."""
    length = len(numbers_as_str)
    
    for i in range(length):
        max_index = find_max_index(numbers_as_str, i, length)
        swap_elements(numbers_as_str, i, max_index)

def get_biggest(numbers):
    if not numbers:
        return -1

    numbers_as_str = get_numbers_as_str_list(numbers)

    sort_numbers_for_maximum_combination(numbers_as_str)

    # Concatenate the sorted strings and convert the result to an integer
    return int(''.join(numbers_as_str))