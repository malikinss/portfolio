""" 
Task: The input to the program is a natural number n.
Write a program that finds the digital root of a given number.
The digital root of the number n is obtained as follows:
if you add all the digits of this number, then all the digits of the found 
sum and repeat this process until the result is a single-digit number 
(digit), which is called the digital root of the original number.

Note. Use nested while loops.
"""

n = int(input())

while n > 9:
    new_n = 0
    
    while n > 0:
        new_n += n % 10 
        n //= 10
    
    n = new_n

print(n)