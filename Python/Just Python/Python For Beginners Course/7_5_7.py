""" 
Task: Given a natural number.
Write a program that determines whether the sequence of its digits, 
when viewed from right to left, is sorted in non-decreasing order.
The program should print "YES" if the sequence of its digits when 
viewed from right to left is in non-decreasing order and "NO" otherwise.
"""

n = int(input())
flag ='YES'

while n // 10 != 0 :
    last_digit = n % 10  
    n //= 10

    if last_digit > n % 10:
        flag = 'NO'

print(flag)