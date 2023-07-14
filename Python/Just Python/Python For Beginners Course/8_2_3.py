""" 
Task: A sequence of 4 integers is received for processing.
It is known that the entered numbers do not exceed 10^8 in absolute value.

You need to write a program that displays the number of odd numbers 
in the original sequence and the maximum odd number.

If there are no odd numbers, display "NO" on the screen.
The programmer was in a hurry and wrote the program incorrectly.

Find all errors in this program (there may be one or more).
It is known that each error affects only one line and can be 
fixed without changing other lines.

Note. Please note that you need to find errors in the existing program, 
and not write your own, possibly using a different solution algorithm.
"""

# original code
n = 4
count = 0
maximum = 999
for i in range(1, n + 1):
    x = int(input())
    if x % 2 != 0:
        count += 1
        if x > maximum:
            maximum = i
            break
if count > 0:
    print(count)
    print(maximum)
else:
    print('NO')


# fixed code
count = 0
maximum = -1

for i in range(4):
    x = int(input())
    
    if x % 2 != 0:
        count += 1
        
        if x > maximum:
            maximum = x

if count > 0:
    print(count)
    print(maximum)
else:
    print('NO')