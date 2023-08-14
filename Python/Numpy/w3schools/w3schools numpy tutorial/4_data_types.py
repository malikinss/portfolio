'''
Below is a list of all data types in NumPy and the characters used to represent them.

i - integer
b - boolean
u - unsigned integer
f - float
c - complex float
m - timedelta
M - datetime
O - object
S - string
U - unicode string
V - fixed chunk of memory for other type ( void )

'''

# Get the data type of an array object:
import numpy as np

arr = np.array([1, 2, 3, 4])
print(arr.dtype)

# Get the data type of an array containing strings:
arr = np.array(['apple', 'banana', 'cherry'])
print(arr.dtype)

# Create an array with data type string:
arr = np.array([1, 2, 3, 4], dtype='S')
print(arr)
print(arr.dtype)

# Create an array with data type 4 bytes integer:
arr = np.array([1, 2, 3, 4], dtype='i4')
print(arr)
print(arr.dtype)

# Change data type from float to integer by using 'i' as parameter value:
arr = np.array([1.1, 2.1, 3.1])
newarr = arr.astype('i')
print(newarr)
print(newarr.dtype)

# Change data type from float to integer by using int as parameter value:
arr = np.array([1.1, 2.1, 3.1])
newarr = arr.astype(int)
print(newarr)
print(newarr.dtype)

# Change data type from integer to boolean:
arr = np.array([1, 0, 3])
newarr = arr.astype(bool)
print(newarr)
print(newarr.dtype)

# Insert the correct NumPy syntax to print the data type of an array.
arr = np.array([1, 2, 3, 4])
print(arr.dtype)

# Insert the correct argument to specify that the array should be of type STRING.
arr = np.array([1, 2, 3, 4], dtype='S')

# Insert the correct method to change the data type to integer.
arr = np.array([1.1, 2.1, 3.1])
newarr = arr.astype('i')