""" 
A sequence of 10 integers is received for processing.

It is known that the entered numbers do not exceed 10^6 
in absolute value.

You need to write a program that displays the sum of all 
negative numbers in a sequence and the maximum negative 
number in the sequence.

If there are no negative numbers, display "NO" on the screen.
The programmer was in a hurry and wrote the program incorrectly.

Find all the errors in this program (there are exactly 5 of them).
It is known that each error affects only one line and can be 
fixed without changing other lines.

Note 1. The number x does not exceed 10^6 in absolute value if -10^6 ≤ x ≤ 10^6.
Note 2: If necessary, you can add the necessary lines of code.
"""

#original code:
mx = 0
s = 0
for i in range(11):
    x = int(input())
    if x < 0:
        s = x
    if x > mx:
        mx = x
print(s)
print(mx)

#fixed code:
mx = (-10 ** 6) - 1
s = 0

for i in range(10):
    x = int(input())
    
    if x < 0:
        s += x
    
    if x < 0 and x > mx:
        mx = x

if s < 0:
    print(s)
    print(mx)
else:
    print('NO')