""" 
Task: Write a program that reads a positive integer n, n∈[1;9] and outputs the value of n + nn + nnn.
"""
n = int(input())
nn = n*10+n
nnn = n*100+nn
f = n+nn+nnn
print(f)