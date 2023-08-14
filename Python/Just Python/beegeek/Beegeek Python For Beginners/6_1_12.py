""" 
Task: Walking around Manhattan, you can't get from point A to point B on the shortest path.
Unless you know how to walk through walls, you will definitely have to walk along its parallel-perpendicular streets.

On a plane, the Manhattan distance between two points (p1;p2) (q1;q2) is defined as 
|p1 - q1| + |p2 - q2|

Write a program that determines the Manhattan distance between two points whose coordinates are given.
"""
p1, p2, q1, q2 = float(input()), float(input()), float(input()), float(input())

f = abs(p1-q1) + abs(p2-q2)

print(int(f))