'''
TODO: The input to the program is a text string of natural numbers. 
A list of numbers is formed from the elements of the string. 
Write a program that swaps the places of adjacent elements of a list (a[0] with a[1], a[2] with a[3], etc.). 
If there is an odd number of elements in the list, then the last one remains in its place.

'''

numbers = input().split()

for i in range(0, len(numbers) - 1, 2):
    numbers[i], numbers[i + 1] = numbers[i + 1], numbers[i]
    
print(*numbers)