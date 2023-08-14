""" 
Task: The input to the program is a natural number n.
Write a program to calculate the alternating sum
1-2+3-4+5-6+...+(-1)^(n+1)n.
"""

n = int(input())
sum_result = 0

for i in range(1, n + 1):
    if i % 2 != 0:
        sum_result += i
    else:
        sum_result = sum_result + i * (-1)

print(sum_result)  