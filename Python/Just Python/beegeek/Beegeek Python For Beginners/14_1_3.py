'''
TODO: Write a function compute_binom(n, k) that takes two natural numbers n and k as arguments and returns the value of the binomial coefficient equal to ( n! / (k! (n - k)!))
NOTE: The factorial of a natural number n is the product of all natural numbers from 1 to n, that is n! = 1 * 2 * 3 * ... * n.
Implement a helper function factorial(n) that calculates the factorial of a number, or use a ready-made function from the math module.
Note that compute_binom(n, k) must return an integer.
'''


from math import factorial


def compute_binom(n, k):
    return factorial(n) // (factorial(k) * factorial(n - k))


n = int(input())
k = int(input())

print(compute_binom(n, k))