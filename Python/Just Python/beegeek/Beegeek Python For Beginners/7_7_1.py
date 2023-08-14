""" 
Task: A sequence of 10 integers is received for processing.

It is known that the entered numbers do not exceed 10 ^6 
in absolute value.

You need to write a program that displays the number of 
non-negative numbers in a sequence and their product.

If there are no non-negative numbers, display "NO" on the screen.

The programmer was in a hurry and wrote the program incorrectly.

Find all the errors in this program (there are exactly 4 of them).

It is known that each error affects only one line and can be fixed 
without changing other lines.

Note 1. The number x does not exceed 10^6 in absolute value if -10^6≤x ≤10^6.

Note 2: If necessary, you can add the necessary lines of code.
"""

#original code:
count = 0
p = 0
for i in range(1, 10):
    x = int(input())
    if x > 0:
        p = p * x
        count = count + 1
if count > 0:
    print(x)
    print(p)
else:
    print('NO')

#fixed code:
count = 0
p = 1
for i in range(1, 11):
    x = int(input())
    if x >= 0:
        p *= x
        count += 1
if count > 0:
    print(count)
    print(p)
else:
    print('NO')