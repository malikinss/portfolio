""" 
Task: Write a program that uses exactly three for loops to print the following sequence of characters:
AAA
AAA
AAA
AAA
AAA
AAA
BBBB
BBBB
BBBB
BBBB
BBBB
E
TTTTT
TTTTT
TTTTT
TTTTT
TTTTT
TTTTT
TTTTT
TTTTT
TTTTT
G
"""

row_A = 'AAA'
row_B = 'BBBB'
row_T = 'TTTTT'

for i in range(6):
    print(row_A)

for i in range(5):
    print(row_B)

print('E')

for i in range(9):
    print(row_T)

print('G')