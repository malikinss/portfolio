'''
TODO: Write a function get_factors(num) that takes a natural number as an argument and returns a list of all factors of that number.
'''

def get_factors(num):
    return [n for n in range(1, num + 1) if num % n == 0]

n = int(input())

print(get_factors(n))