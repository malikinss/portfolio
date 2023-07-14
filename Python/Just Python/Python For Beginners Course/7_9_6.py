""" 
Task: Given a natural number n.
Write a program that prints the value of the sum 1!+2!+3!+…+n!.
"""

n = int(input())
result = 0

for i in range(1, n + 1):
    cur_fact = 1

    for j in range(1, i + 1):
        cur_fact *= j
    
    result += cur_fact
    
print(result)