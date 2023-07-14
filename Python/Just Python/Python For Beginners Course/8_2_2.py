""" 
Task: A sequence of 8 integers is received for processing.
It is known that the input numbers in absolute value do not exceed 10 ^ 12.

You need to write a program that displays the number of numbers divisible 
by 4 in the original sequence and the maximum number divisible by 4.

If there are no integers divisible by 4, you need to display "NO" on the screen.
The programmer was in a hurry and wrote the program incorrectly.

Find all errors in this program (there may be one or more).
It is known that each error affects only one line and can be 
fixed without changing other lines.

Note. Please note that you need to find errors in the existing program, 
and not write your own, possibly using a different solution algorithm.
"""

# original code
n = 7
count = 0
maximum = 1000
for i in range(1, n + 1):
    x = int(input())
    if x // 4 == 0:
        count += 1
        if x < maximum:
            maximum = x
if count > 0:
    print(count)
    print(maximum)
else:
    print('NO')


# fixed code
n = 8
count = 0
maximum = (-10 ** 6) - 1

for i in range(1, n + 1):
    x = int(input())
    
    if x % 4 == 0:
        count += 1
        
        if x > maximum:
            maximum = x

if count > 0:
    print(count)
    print(maximum)
else:
    print('NO')