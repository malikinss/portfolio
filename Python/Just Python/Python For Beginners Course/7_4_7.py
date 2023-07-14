""" 
Task: Everyone knows that the witcher is able to defeat any monsters, 
but his services will cost a lot.
In addition, the witcher does not accept banknotes, 
he only accepts minted coins.
In the world of the witcher, there are coins with denominations of 1,5,10,25.
Write a program that determines the minimum number of minted coins 
to be paid to the witcher.
"""

n = int(input())
counter = 0

while n >= 25:
    counter += 1
    n = n - 25

while n >= 10:
    counter += 1
    n = n - 10

while n >= 5:
    counter += 1
    n = n - 5

while n >= 1:
    counter += 1
    n = n - 1

print(counter)   