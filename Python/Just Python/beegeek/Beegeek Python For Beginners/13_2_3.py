'''
TODO: Write a print_digit_sum() function that takes a single integer num and prints the sum of its digits.
'''


def print_digit_sum(num):
    digit_sum = 0
    
    while num > 0:
        digit_sum += num % 10
        num //= 10

    print(digit_sum)

n = int(input())

print_digit_sum(n)