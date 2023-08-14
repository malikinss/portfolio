import numpy as np
# Slice elements from index 1 to index 5 from the following array:
arr = np.array([1, 2, 3, 4, 5, 6, 7])
print(arr[1:5])

# Slice elements from index 4 to the end of the array:
print(arr[4:])

# Slice elements from the beginning to index 4 (not included):
print(arr[:4])

# Use the minus operator to refer to an index from the end:
print(arr[-3:-1])

# Return every other element from index 1 to index 5:
print(arr[1:5:2])

# Return every other element from the entire array:
print(arr[::2])

# From the second element, slice elements from index 1 to index 4 (not included):
arr = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
print(arr[1, 1:4])

# From both elements, return index 2:
print(arr[0:2, 2])

# From both elements, slice index 1 to index 4 (not included), this will return a 2-D array:
print(arr[0:2, 1:4])

# Insert the correct slicing syntax to print the following selection of the array:
# Everything from (including) the second item to (not including) the fifth item.
arr = np.array([10, 15, 20, 25, 30, 35, 40])
print(arr[1:4])

# Everything from (including) the third item to (not including) the fifth item.
print(arr[2:4])

# Every other item from (including) the second item to (not including) the fifth item.
print(arr[1:4:2])

# Every other item from the entire array.
print(arr[::2])