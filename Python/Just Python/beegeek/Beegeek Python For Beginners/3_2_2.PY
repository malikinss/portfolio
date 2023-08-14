""" 
Task: Write a program that reads two integers a and b and displays the square of the sum (a+b)^2 and the sum of the squares a^2 + b^2 of these numbers.
"""
a = int(input())
b = int(input())
square_of_the_sum = (a + b) ** 2
sum_of_the_squares = (a ** 2) + (b ** 2)
print('square of the sum', a, 'and', b, 'equals to', square_of_the_sum)
print('sum of the squares', a, 'and', b, 'equals to', sum_of_the_squares)