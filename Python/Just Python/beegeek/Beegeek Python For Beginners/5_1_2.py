""" 
Task: Two cells of a chessboard are given. 
Write a program that determines whether the specified cells have the same color or not. If they are painted in the same color, then print the word "YES", and if they are in different colors, then print "NO".
"""
x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())
a = x1 + y1
b = x2 + y2
if (a+b) % 2==0:
    print('YES')
else:
    print('NO')