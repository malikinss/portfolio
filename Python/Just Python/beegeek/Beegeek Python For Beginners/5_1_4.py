""" 
Task: Write a program that reads an integer and outputs its corresponding Roman numeral. If the number is outside the range 1-10, then the program should display the text "error".
"""
digit = int(input())
if digit == 1:
    print('I')
elif digit == 2:
    print('II')
elif digit == 3:
    print('III')
elif digit == 4:
    print('IV')
elif digit == 5:
    print('V')
elif digit == 6:
    print('VI')
elif digit == 7:
    print('VII')
elif digit == 8:
    print('VIII')
elif digit == 9:
    print('IX')
elif digit == 10:
    print('X')
else:
    print('error')