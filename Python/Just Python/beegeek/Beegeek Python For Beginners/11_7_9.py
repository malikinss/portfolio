'''
The input to the program is a text string containing integers. Write a list expression program that prints the squares of even numbers that do not end in 4.
'''


print(*[int(i) ** 2 for i in input().split() if i[-1] in "046"])