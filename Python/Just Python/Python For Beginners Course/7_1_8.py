""" 
Task: The input to the program is three natural numbers m, p, n:

m: starting number of organisms;
p: average daily increase in %;
n: number of days to breed.

Write a program that predicts the size of a population of organisms. The program should output the population size on each day, starting on day 1 and ending on the nth day.
"""

m, p, n = int(input()), int(input()), int(input())

p = p/100
p = p+1

for i in range(n):
    print(i+1, m)
    m = m * p