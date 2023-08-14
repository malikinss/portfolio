""" 
Task: The input to the program is a natural number n(n≥2) 
- the leg of a right-angled isosceles triangle.
Write a program that prints a star triangle according to the example.
"""

given_number = int(input())
star_to_print = '*'

for i in range(given_number):
    print(star_to_print * (given_number - i))