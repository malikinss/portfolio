""" 
Task: A natural number is being processed.

You need to write a program that displays its first (highest) digit on the screen.

The programmer was in a hurry and wrote the program incorrectly.

Find all the errors in this program (there are exactly 2 of them).

It is known that each error affects only one line and can be fixed without changing other lines.
"""

#original code:
n = int(input())
while n > 0:
    n %= 10
print(n)

#fixed code:
n = int(input())

while n > 9:
    n //= 10

print(n)