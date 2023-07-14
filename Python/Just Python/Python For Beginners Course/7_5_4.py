""" 
Task: Given a natural number. 
Write a program that calculates:

the sum of its digits;
the number of digits in it;
multiplying its numbers;
the arithmetic mean of its digits;
its first digit;
the sum of its first and last digits.
"""

n = int(input())

digit_sum = 0
digit_cnt = 0
digit_product = 1
last_digit = n % 10

while n > 0:
    cur_digit = n % 10

    first_digit = cur_digit
    digit_sum += cur_digit
    digit_cnt += 1
    digit_product *= cur_digit
    
    n //= 10

digit_average = digit_sum / digit_cnt
first_last_sum = first_digit + last_digit

print(digit_sum)
print(digit_cnt)
print(digit_product)
print(digit_average)
print(first_digit)
print(first_last_sum)