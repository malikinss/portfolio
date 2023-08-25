'''
The input to the program is a text string containing natural numbers. Write a program that inserts a + sign between each number and then calculates the sum of the resulting numbers.
'''


n = [int(i) for i in input().split()]

print(*n, sep='+', end='=')
print(sum(n))