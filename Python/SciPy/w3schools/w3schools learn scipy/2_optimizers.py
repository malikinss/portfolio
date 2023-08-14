from scipy.optimize import *
from math import cos


# Find root of the equation x + cos(x):
def eqn(x):
  return x + cos(x)

myroot = root(eqn, 0)

print(myroot.x)


# Print all information about the solution (not just x which is the root)
print(myroot)


# Minimize the function x^2 + x + 2 with BFGS:
def eqn(x):
  return x**2 + x + 2

mymin = minimize(eqn, 0, method='BFGS')

print(mymin)


# Insert the missing parts to minimize the equation, by using the TNC method:
from scipy.optimize import minimize

def eqn(x):
  return x**2 + x + 2

mymin = minimize(eqn, 0, method='TNC')