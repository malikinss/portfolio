""" 
Task: Write a program that reads 10 numbers and prints the result 
of multiplication of non-zero numbers.
"""

total = 1

for i in range(10):
    number = int(input())
    
    if number != 0:
        total *= number

print(total)