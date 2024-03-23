'''
TODO: The input to the program is a string of text containing natural numbers arranged in non-decreasing order. 
A list of numbers is formed from the string. 
Write a program to count the number of different elements in a list.
'''

numbers = input().split()
counter = 1

for i in range(len(numbers) - 1):
    if numbers[i] != numbers[i + 1]:
        counter += 1

print(counter)