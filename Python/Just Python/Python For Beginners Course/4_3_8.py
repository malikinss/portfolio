""" 
Task: On the roulette wheel, the pockets are numbered from 0 to 36. 
Below are the colors of the pockets:

pocket 0 green;
for pockets 1 to 10, odd-numbered pockets are red, even-numbered pockets are black;
for pockets 11 to 18, odd-numbered pockets are black, even-numbered pockets are red;
for pockets 19 to 28, odd-numbered pockets are red, even-numbered pockets are black;
for pockets 29 to 36, odd-numbered pockets are black, even-numbered pockets are red.

Write a program that reads the number of a pocket and shows if that pocket is green, red, or black. 
The program should display an error message if the user enters a number that is outside the range 0 to 36.
The program should display the color of the pocket or the message "input error" if the entered number lies outside the range from 0 to 36.
"""
number_of_pocket = int(input())
green = 'green'
black = 'black'
red = 'red'

if (1 <= number_of_pocket <= 10 or 19 <= number_of_pocket <= 28):
    if number_of_pocket % 2 == 0:
        print(black)
    else:
        print(red)
elif (11 <= number_of_pocket <= 18 or 29 <= number_of_pocket <= 36):
    if number_of_pocket % 2 == 0:
        print(red)
    else:
        print(black)
elif number_of_pocket == 0:
    print(green)
else:
    print('input error')