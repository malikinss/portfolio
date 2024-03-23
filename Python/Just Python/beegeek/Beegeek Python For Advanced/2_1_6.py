'''
TODO: Given a five-digit or six-digit natural number. 
Write a program that will reverse the order of its last five digits.
'''

n = input()
new_n = int(n[:-5] + n[-5:][::-1])

print(new_n)