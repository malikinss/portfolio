import numpy as np


# Add the values in arr1 to the values in arr2:
arr1 = np.array([1, 2, 3])
arr2 = np.array([1, 2, 3])

newarr = np.add(arr1, arr2)

print(newarr)


# Sum the values in arr1 and the values in arr2:
arr1 = np.array([1, 2, 3])
arr2 = np.array([1, 2, 3])

newarr = np.sum([arr1, arr2])

print(newarr)

# Perform summation in the following array over 1st axis:
arr1 = np.array([1, 2, 3])
arr2 = np.array([1, 2, 3])

newarr = np.sum([arr1, arr2], axis=1)

print(newarr)


# Perform cummulative summation in the following array:
arr = np.array([1, 2, 3])

newarr = np.cumsum(arr)

print(newarr)