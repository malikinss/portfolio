""" 
Task: The input to the program is a natural number n, and then n integers.
Write a program that for each input number x prints the value of the 
function f(x)=x ^2 +2x+1, each on a separate line.
"""

n = int(input())
lst = []

for i in range(n):
    a = int(input())
    lst.append(a)

print(*lst, sep = '\n')
print()

for num in lst:
    f = num**2 + 2*num + 1
    print(f)