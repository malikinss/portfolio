""" 
Task: n students divide k tangerines equally, the non-divisible remainder remains in the basket. How many whole tangerines will each student get? How many whole tangerines will be left in the basket?
"""
n = int(input())
k = int(input())
tangerines_per_student = k // n 
tangerines_left = k % n
print(tangerines_per_student)
print(tangerines_left)