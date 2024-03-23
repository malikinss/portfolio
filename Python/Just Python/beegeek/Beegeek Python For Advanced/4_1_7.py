'''
TODO: A sublist is part of another list.
A sublist can contain one element, several, or even none.
For example, [1], [2], [3] and [4] are sublists of the list [1, 2, 3, 4].
The list [2, 3] is a sublist of the list [1, 2, 3, 4], but the list [2, 4] is not a sublist of the list [1, 2, 3, 4], since elements 2 and 4 in the second list are not adjacent (since they are broken by element 3).
An empty list is a sublist of any list. The list itself is a sublist of itself, that is, the list [1, 2, 3, 4] is a sublist of the list [1, 2, 3, 4].

The input to the program is a text string containing symbols. A list is formed from this string. Write a program that prints a list containing all possible sublists of the list, including the empty list.

NOTE: The order of lists of the same length must correspond to the order in which they appear in the main list.
'''

input_data = input().split()
# save the length of the input list here
n = len(input_data)

result = [[]]
for size in range(1, n + 1):
    # sublist when iterating over size elements
    cur_seq = []
    for i in range(n - size + 1):
        cur_seq.append(input_data[i:i + size])
    
    result.extend(cur_seq)
    
print(result)