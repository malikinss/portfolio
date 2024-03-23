'''
TODO:   Implement the same_parity() function, which takes a single argument:

        numbers — a list of integers

        The function should return a new list, the elements of which are numbers from the numbers list having the same parity as the first element of this list.

NOTE:   The numbers in the list returned by the function must be in their original order.
'''

def same_parity(numbers):
    return list(filter(lambda x: numbers[0] % 2 == x % 2, numbers))