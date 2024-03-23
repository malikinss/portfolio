'''
TODO: Write a function func(num1, num2) that takes two natural numbers num1 and num2 as arguments and returns True if num1 is evenly divisible by num2 and False otherwise.

The output of the program should be "divided" (if func() returned True) and "not divided" (if func() returned False).
'''

def func(num1, num2):
    return num1 % num2 == 0


num1, num2 = int(input()), int(input())


if func(num1, num2):
    print("divided")
else:
    print("not divided")