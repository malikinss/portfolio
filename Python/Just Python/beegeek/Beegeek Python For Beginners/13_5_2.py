'''
TODO: Write a function is_prime(num) that takes a natural number as an argument and returns True if the number is prime and False otherwise.
'''


def is_prime(num):
    lst = [i for i in range(1, num + 1) if num % i == 0]
    
    if len(lst) == 2:
        return True
    else:
        return False


n = int(input())


print(is_prime(n))