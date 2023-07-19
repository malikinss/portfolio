""" 
Task: The input to the program is a natural number n, then n lines, 
then one more line — the search query. 
Write a program that prints out all the input lines that match the search term.
"""

lst = []
for i in range(int(input())):
    a = input()
    lst.append(a)

srch = input().lower()    

for s in lst:
    if srch in s.lower():
        print(s)