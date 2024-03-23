'''
TODO:
        Create a list of integers 1, 4, 9, 16, 25, 36, 49, 64, 81, 100 using list encoding. 
        Use range() as the value source
'''

numbers = [number * number for number in range(1,11)]
print(numbers)