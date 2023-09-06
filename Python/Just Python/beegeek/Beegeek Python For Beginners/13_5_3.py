'''
TODO: Write a function get_next_prime(num) that takes a natural number num as an argument and returns the first prime number greater than num

NOTE: Use the is_prime() function from the previous task.
'''


def is_prime(num):
    lst = [i for i in range(1, num + 1) if num % i == 0]
    
    if len(lst) == 2:
        return True
    else:
        return False


def get_next_prime(num):
    while num > 0:
        num += 1
        
        if is_prime(num):
            return num


n = int(input())

print(get_next_prime(n))