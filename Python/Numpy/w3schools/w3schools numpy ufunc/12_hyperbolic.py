import numpy as np


# Find sinh value of PI/2:
x = np.sinh(np.pi/2)

print(x)


# Find cosh values for all of the values in arr:
arr = np.array([np.pi/2, np.pi/3, np.pi/4, np.pi/5])

x = np.cosh(arr)

print(x)


# Find the angle of 1.0:
x = np.arcsinh(1.0)

print(x)


# Find the angle for all of the tanh values in array:
arr = np.array([0.1, 0.2, 0.5])

x = np.arctanh(arr)

print(x)