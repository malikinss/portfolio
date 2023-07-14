""" 
Task: Given a natural number n, (n≥10).
Write a program that determines its maximum and minimum digits
"""

n = int(input())
max_digit, min_digit = 0, 9

while n != 0:
    last_digit = n % 10
    n //= 10
    
    if last_digit < min_digit:
        min_digit = last_digit
    
    if last_digit > max_digit:
        max_digit = last_digit

print('Maximum digit is equals to', max_digit)
print('Minimum digit is equals to', min_digit)