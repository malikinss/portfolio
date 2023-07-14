""" 
Task: A natural number is being processed.
You need to write a program that displays the sum of the even digits 
of this number or 0 if there are no even digits in the entry.
The programmer was in a hurry and wrote the program incorrectly.

Find all errors in this program (there may be one or more).
It is known that each error affects only one line and can be 
fixed without changing other lines.

Note. Please note that you need to find errors in the existing program, 
and not write your own, possibly using a different solution algorithm.
"""

# original code
n = input()
s = 0
while n > 10:
    if n % 2 == 1:
        s = n % 10
    n //= 10
print(s)


# fixed code
n = int(input())
s = 0

while n > 0:
    
    if n % 2 == 0:
        s += n % 10
    
    n //= 10

print(s)