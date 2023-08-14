""" 
A natural number is being processed.

You need to write a program that displays the maximum digit of a number that is a multiple of 3.

If there are no digits divisible by 3 in the number, display “NO” on the screen.

The programmer was in a hurry and wrote the program incorrectly.

Find all the errors in this program (there are exactly 5 of them).

It is known that each error affects only one line and can be fixed without changing other lines.

Note 1. The number 0 is divisible by any natural number.
Note 2: If necessary, you can add the necessary lines of code.
"""

#original code:
n = int(input())
max_digit = n % 10
while n > 0:
    digit = n % 10
    if digit % 3 == 0:
        if digit < max_digit:
            digit = max_digit
    n = n % 10
if max_digit == 0:
    print('NO')
else:
    print(max_digit)

#fixed code:
n = int(input())

max_digit = -1

while n > 0:
    digit = n % 10
    
    if digit % 3 == 0:
        if digit > max_digit:
            max_digit = digit
    
    n = n // 10

if max_digit == -1:
    print('NO')
else:
    print(max_digit)