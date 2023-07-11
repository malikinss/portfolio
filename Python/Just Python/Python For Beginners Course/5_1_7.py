""" 
Task: Two different cells of a chessboard are given. 
Write a program that determines if the knight can get from the first cell to 
the second in one move. 
The program receives as input four numbers from 1 to 8 each, specifying the 
column number and row number, first for the first cell, then for the second cell. 
The program should print "YES" if it is possible to get to the second one 
from the first cell by the knight's move, or "NO" otherwise.
"""
x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())
dx = abs(x1 - x2)
dy = abs(y1 - y2)
if dx == 1 and dy == 2 or dx == 2 and dy == 1:
    print('YES')
else:
    print('NO')