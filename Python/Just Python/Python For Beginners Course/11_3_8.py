""" 
Task: The input to the program is a natural number n and n lines, 
and then the number k.
Write a program that prints the kth letter from the input strings 
on one line without spaces.
"""

n = int(input())
given_list = []

for _ in range(n):
    given_list.append(input())

index = int(input())    
result = ''

for current_string in given_list:
    if len(current_string) >= index:
        result += current_string[index - 1]

print(result)