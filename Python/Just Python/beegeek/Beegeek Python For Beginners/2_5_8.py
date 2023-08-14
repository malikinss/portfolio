""" 
Task: Given a three-digit number abc, in which all digits are different. Write a program that prints the six numbers formed by permuting the digits of a given number.
"""
num = int(input())
a = num // 100
b = num // 10 % 10
c = num % 10
print(num)
print(a*100+c*10+b)
print(b*100+a*10+c)
print(b*100+c*10+a)
print(c*100+a*10+b)
print(c*100+b*10+a)