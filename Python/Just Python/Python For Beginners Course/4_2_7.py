""" 
Task: Two different cells of a chessboard are given. 
Write a program that determines whether a rook can move from the first square to the second in one move. 
The program receives as input four numbers from 1 to 8 each, specifying the column number and row number, first for the first cell, then for the second cell. 
The program should print "YES" if it is possible to get to the second one from the first cell with the move of the rook, or "NO" otherwise.
"""
x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())
if x1 - x2 == 0 or y1 - y2 == 0:
    print('YES')
else:
    print('NO')