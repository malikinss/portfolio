""" 
TODO: An arithmetic progression is a sequence of numbers 
      1, 2,..., a1, a2, ..., an, each of which, starting from a2, is obtained from the previous one by adding to it the same constant number d (the difference of the progression), then There is:

      an = a(n-1) + d

      If the first member of the progression and its difference are known, then the n-th member of the arithmetic progression is found by the formula:

      an = a1+d*(n-1)

      The program should output the nth term of the arithmetic progression.
"""

a1 = int(input())
d = int(input())
n = int(input())

an = a1 + d * (n - 1)

print(an)