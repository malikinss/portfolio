""" 
Task: Enhance the following code using the concatenation (+) and 
list multiplication (*) operators so that it outputs a list:

[1, 2, 3, 1, 2, 3, 6, 6, 6, 6, 6, 6, 6, 6, 6, 7, 8, 9, 10, 11, 12, 13].
"""

# original code
numbers1 = [1, 2, 3]
numbers2 = [6]
numbers3 = [7, 8, 9, 10, 11, 12, 13]

print()

# fixed code
numbers1 = [1, 2, 3]
numbers2 = [6]
numbers3 = [7, 8, 9, 10, 11, 12, 13]
numbers4 = (numbers1 * 2) + (numbers2*9) + numbers3
print(numbers4)