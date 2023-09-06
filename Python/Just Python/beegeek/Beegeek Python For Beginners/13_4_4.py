'''
TODO: Write a function number_of_factors(num) that takes a number as an argument and returns the number of factors of that number.

NOTE: Use the already implemented get_factors(num) function from the previous task.
'''


def get_factors(num):
    return [n for n in range(1, num + 1) if num % n == 0]


def number_of_factors(num):
    factors = get_factors(num)

    return len(factors) 


n = int(input())

print(number_of_factors(n))