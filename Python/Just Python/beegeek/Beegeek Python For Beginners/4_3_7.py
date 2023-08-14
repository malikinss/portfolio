""" 
Task: Red, blue and yellow are called primary colors because 
they cannot be made by mixing other colors. 
When two primary colors are mixed, a secondary color is obtained:

if you mix red and blue, you get purple;
if you mix red and yellow, you get orange;
If you mix blue and yellow, you get green.
Write a program that reads the names of two primary colors to blend. 
If the user enters anything other than the names "red", "blue", 
or "yellow", then the program should display an error message. 
Otherwise, the program should display the name of the secondary 
color that will be the result.

The program should display the resulting blend color, or a "color error" 
message if a wrong color was entered.

Note. If you mix red and red, you get red, and so on.
"""
color_1 = input()
color_2 = input()

red = 'red'
blue = 'blue'
yellow = 'yellow'
orange = 'orange'
green = 'green'
purple = 'purple'

if (color_1 == red and color_2 == blue) or (color_1 == blue and color_2 == red):
    print(purple)
elif (color_1 == red and color_2 == yellow) or (color_1 == yellow and color_2 == red):
    print(orange)
elif (color_1 == blue and color_2 == yellow) or (color_1 == yellow and color_2 == blue):
    print(green)
elif (color_1 == color_2 == yellow):
    print(yellow)
elif (color_1 == color_2 == red):
    print(red)
elif (color_1 == color_2 == blue):
    print (blue)
else:
    print('color error')