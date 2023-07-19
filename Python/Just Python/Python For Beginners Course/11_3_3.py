""" 
Task: Write a program that displays the following list:

['a', 'bb', 'ccc', 'dddd', 'eeeee', 'ffffff', ...]
"""

result = []

for i in range(26):
    cur = ""
    
    for j in range(i + 1):
        cur += chr(ord("a") + i)
    
    result.append(cur)

print(result)