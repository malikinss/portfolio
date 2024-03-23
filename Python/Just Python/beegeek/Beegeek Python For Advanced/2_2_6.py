'''
TODO: Write a program to determine whether a number is the product of two numbers from a given set. 
The program should output the result as a “YES” or “NO” answer.
The first line contains the number n (0<n<1000) – the number of numbers in the set.
In the next n lines, the integers that make up the set (may be repeated) are entered.
Then follows an integer, which is or is not the product of two numbers from the set.
NOTE: A number from a set cannot be multiplied by itself. In other words, the two factors must have different indexes in the set.
'''

size = int(input())
seq = [int(input()) for _ in range(size)]
number = int(input())
flag = False

for i in range(size):
    for j in range(size):
        if i != j and seq[i] * seq[j] == number:
            flag = True

if flag:
    print("ДА")
else:
    print("НЕТ")