'''
TODO: The input to the program is the number n, and then n lines containing integers in ascending order. 
Lists of numbers are formed from these lines. 
Write a program that merges the given lists into one sorted list using the quick_merge() function and then outputs it.
'''


def quick_merge(list1, list2):
    result = []

    p1 = 0  # pointer to the first element of list1
    p2 = 0  # pointer to the first element of list2

    # until at least one list is finished
    while p1 < len(list1) and p2 < len(list2):  
        if list1[p1] <= list2[p2]:
            result.append(list1[p1])
            p1 += 1
        else:
            result.append(list2[p2])
            p2 += 1

    if p1 < len(list1):   # attachment of remainder
        result += list1[p1:]
    
    if p2 < len(list2):
        result += list2[p2:]
    
    return result

total_list = []

for i in range(int(input())):
    num = [int(q) for q in input().split()]
    
    total_list = quick_merge(total_list, num)

print(*total_list)