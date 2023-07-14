""" 
Task: The input to the program is a natural number n. 
Write a program that for each of the numbers from 0 to n (inclusive) 
displays the phrase: 
"The square of the number [number] is equal to [number]" (without quotes).
"""

given_number = int(input())

for i in range(given_number+1):
    square_of_i = i ** 2
    print('The square of the number', i, 'is equal to', square_of_i)