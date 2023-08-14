""" 
A sequence of 7 integers is received for processing.

It is known that the entered numbers do not exceed 10^6 in absolute value.

You need to write a program that calculates and prints the sum of all even 
numbers in a sequence, or 0 if there are no even numbers in the sequence.

The programmer was in a hurry and wrote the program incorrectly.

Find all the errors in this program (there are exactly 4 of them).
It is known that each error affects only one line and can be fixed without 
changing other lines.

Note 1. The number x does not exceed 10^6 in absolute value if -10^6 ≤ x ≤ 10^6.
Note 2: If necessary, you can add the necessary lines of code.
"""

#original code:
s = 1
for i in range(1, 7):
    n = input()
    if i % 2 == 0:
        s = s + n
print(s)

#fixed code:
s = 0

for i in range(7):
    n = int(input())
    
    if n % 2 == 0:
        s += n

print(s)