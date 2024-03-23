'''
TODO: The program receives two integers a and b as input.
Write a program that prints:
- the sum of numbers a and b;
- difference between numbers a and b;
- the product of numbers a and b;
- quotient of numbers a and b;
- the integer part of dividing the number a by b;
- the remainder when dividing the number a by b;
- square root of the sum of their 10th powers sqrt(a^10 + b^10)
'''

a = int(input())
b = int(input())

# Sum of numbers a and b
sm = a + b
print(sm)

# Difference of numbers a and b
diff = a - b
print(diff)

# Product of numbers a and b
product = a * b
print(product)

# Quotient of numbers a and b
quotient = a / b
print(quotient)

# Integer part of a divided by b
integer_division = a // b
print(integer_division)

# Remainder of number a divided by b
remainder = a % b
print(remainder)

# Square root of the sum of their 10th powers
sqrt_sum_pow_10 = (a**10 + b**10)**0.5
print(sqrt_sum_pow_10)