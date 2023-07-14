""" 
Task: The input to the program is a sequence of integers, 
each number on a separate line.
A sign of the end of the sequence is any negative number, 
while it is not included in the sequence itself.
Write a program that prints the sum of all terms in a given sequence.
"""

num = int(input())

sequence_sum = 0

while num >= 0:
    sequence_sum += num
    num = int(input())

print(sequence_sum)