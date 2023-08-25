""" 
TODO: Write a program to calculate the value of a function
      f(a,b) =3(a+b)^3+275b^2-127a-41 by the entered integer values a and b.
"""

a = int(input())
b = int(input())

f = (a + b)
f = f * f * f
f = 3*f
f = f + 275 * (b * b)
f = f - 127 * a - 41

print(f)