""" 
Task: The input to the program is a text string containing various natural numbers. A list of numbers is formed from this string. Write a program that swaps the minimum and maximum elements of this list.
"""

seq = []
for el in input().split():
    seq.append(int(el))
    
mx_ind = seq.index(max(seq))
mn_ind = seq.index(min(seq))

seq[mx_ind], seq[mn_ind] = seq[mn_ind], seq[mx_ind]

print(*seq)