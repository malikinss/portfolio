import numpy as np


# Create your own ufunc for addition:
def myadd(x, y):
  return x+y

myadd = np.frompyfunc(myadd, 2, 1)

print(myadd([1, 2, 3, 4], [5, 6, 7, 8]))


# Check if a function is a ufunc:
print(type(np.add))


# Check the type of another function: concatenate():
print(type(np.concatenate))


# Use an if statement to check if the function is a ufunc or not:
if type(np.add) == np.ufunc:
  print('add is ufunc')
else:
  print('add is not ufunc')