'''
TODO: The input to the program is a text string containing symbols. Write a program that packs sequences of identical characters from a given string into sublists.
'''

res = []

for el in input().split():
    if res and el in res[-1]:
        res[-1].append(el)
    else:
        res.append([el])

print(res)
    