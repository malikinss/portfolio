'''
The input to the program is a string of text. 
Write a program that determines if an input string is a valid phone number. 
A string of text is a valid phone number if it has the format:

- abc-def-hijk or
- 7-abc-def-hijk,
where a, b, c, d, e, f, h, i, j, k are numbers from 0 to 9.
'''


seq = input().split("-")
lens = [len(el) for el in seq]

if lens == [1, 3, 3, 4] and "".join(seq).isdigit() and seq[0] == "7":
    print("YES")
elif lens == [3, 3, 4] and "".join(seq).isdigit():
    print("YES")
else:
    print("NO")