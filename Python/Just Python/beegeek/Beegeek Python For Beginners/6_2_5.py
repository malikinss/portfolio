""" 
Task: 3 lines are entered in random order. 
Write a program that finds out whether it is possible to construct 
an increasing arithmetic progression from the lengths of these strings.

The program should output the string "YES" if it is possible to construct 
an arithmetic progression from the lengths of the entered words, "NO" otherwise.
"""
strlen_1, strlen_2, strlen_3 = len(input()), len(input()), len(input())

shortest_str = min(strlen_1, strlen_2, strlen_3)
longest_str = max(strlen_1, strlen_2, strlen_3)
sum_of_strlens = strlen_1 + strlen_2 + strlen_3

middle_str = sum_of_strlens - shortest_str - longest_str

if longest_str - middle_str == middle_str - shortest_str:
    print('YES')
else:
    print('NO')