""" 
Task: The input to the program is a sequence of integers from 1 to 5, 
characterizing the student's grade, each number on a separate line.
The end of the sequence is any negative number, or a number greater than 5.
Write a program that prints the number of fives.
"""

num = 1
p = 0
while num > 0 and num < 6:
    num = int(input())
    if num == 5:
        p += 1
print(p)