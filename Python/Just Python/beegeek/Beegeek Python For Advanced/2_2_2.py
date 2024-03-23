'''
TODO: The input to the program is a text string of natural numbers. A list of numbers is formed from it. Write a program to count the number of numbers that are greater than the number preceding them in this list.

'''

numbers = [int(n) for n in input().split()]
counter = 0

for i in range(1, len(numbers)):
    if numbers[i] > numbers[i - 1]:
        counter += 1
        
print(counter)