'''
The input to the program is two lines of text containing integers. Lists of numbers L and M are formed from these strings. Write a program that creates a third list whose elements are the sums of the corresponding elements of the lists L and M. Then the program should display each element of the resulting list on one line, separated by 1 space.
'''


l, m = input().split(), input().split()

g = (int(l[i]) + int(m[i]) for i in range(len(l)))

print(*g)