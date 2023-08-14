import numpy as np

# Iterate on the elements of the following 1-D array:
arr = np.array([1, 2, 3])
for x in arr:
    print(x)

# In a 2-D array it will go through all the rows.
arr = np.array([[1, 2, 3], [4, 5, 6]])
for x in arr:
    print(x)

# Iterate on each scalar element of the 2-D array:
arr = np.array([[1, 2, 3], [4, 5, 6]])
for x in arr:
    for y in x:
        print(y)

# Iterate on the elements of the following 3-D array:
arr = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
for x in arr:
    print(x)

# Iterate down to the scalars:
arr = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
for x in arr:
    for y in x:
        for z in y:
            print(z)

# Iterate through the following 3-D array:
arr = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
for x in np.nditer(arr):
    print(x)

# Iterate through the array as a string:
arr = np.array([1, 2, 3])
for x in np.nditer(arr, flags=['buffered'], op_dtypes=['S']):
    print(x)

# Iterate through every scalar element of the 2D array skipping 1 element:
arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
for x in np.nditer(arr[:, ::2]):
    print(x)

# Enumerate on following 1D arrays elements:
arr = np.array([1, 2, 3])
for idx, x in np.ndenumerate(arr):
    print(idx, x)

# Enumerate on following 2D array's elements:
arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
for idx, x in np.ndenumerate(arr):
    print(idx, x)