'''
TODO: Write a function merge(list1, list2) that takes two ascending-sorted integer lists as arguments and merges them into one sorted list.

NOTE: You can use the sort() list method, or you can do without it 😎.
'''


def merge(list1, list2):
    return sorted(list1 + list2)
    

numbers1 = [int(c) for c in input().split()]
numbers2 = [int(c) for c in input().split()]


print(merge(numbers1, numbers2))