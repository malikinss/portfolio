'''
TODO: n people, numbered from 1 to n, stand in a circle.
They begin to count, every kth person in a row leaves the circle, after which the count continues with the next person.
Write a program to determine the number of the person who will remain in the circle last.
'''

n = int(input())
k = int(input())
 
res = 0

for i in range(1, n+1):
    res = (res + k) % i

print(res + 1)