""" 
TODO: A geometric progression is a sequence of numbers 
      b1,b2, ..., bn, each of which, starting from b2, is obtained from the previous one by multiplying by the same constant number q (the denominator of the progression), that is:

    bn = b(n-1) * q

    If the first member of the progression and its denominator are known, then the n-th member of the geometric progression is found by the formula

    bn = b1 * q^(n-1)

    Input data: The input to the program is given three integers: b1, q and n, each on a separate line.

    Output: The program should display the n-th term of a geometric progression.
"""

b1 = int(input())
q = int(input())
n = int(input())

bn = b1 * q ** (n - 1)

print(bn)