import numpy as np


# Find the HCF of the following two numbers:
num1 = 6
num2 = 9

x = np.gcd(num1, num2)

print(x)


# Find the GCD for all of the numbers in the following array:
arr = np.array([20, 8, 32, 36, 16])

x = np.gcd.reduce(arr)

print(x)