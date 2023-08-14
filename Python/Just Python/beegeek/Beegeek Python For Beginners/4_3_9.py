""" 
Task: Two segments are given on the number line: [a1; b1] and [a2; b2]
Write a program that finds their intersection.
The intersection of two segments can be:
line segment;
dot;
empty set.
It is guaranteed that a1 < b1 and a2 < b2
"""
a1 = int(input())
b1 = int(input())
a2 = int(input())
b2 = int(input())

if a1 < a2 > b1 or a2 < a1 > b2:
    print('empty set')
elif b1 == a2:
    print(b1)
elif b2 == a1:
    print(b2)
elif a1<a2<b1 and b1<b2:
    print(a2, b1)
elif a2<a1<b2 and b2<b1:
    print(a1, b2)
elif a1==a2 and b1<b2:
    print(a1, b1)
elif a2==a1 and b2<b1:
    print(a2, b2)
elif b1==b2 and a1<a2:
    print(a2, b2)
elif b2==b1 and a2<a1:
    print(a1, b1)
elif a1>a2 and b1<b2:
    print(a1, b1)
elif a2>a1 and b2<b1:
    print(a2, b2)    
elif a2==a1 and b2==b1:
    print(a1, b2)