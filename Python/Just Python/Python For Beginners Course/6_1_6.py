""" 
Task: Given a positive real number. 
Print its first digit after the decimal point.
"""
a = float(input())
b = a*10
c = b%10
print(int(c))