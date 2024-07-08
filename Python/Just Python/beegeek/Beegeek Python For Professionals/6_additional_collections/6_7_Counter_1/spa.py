from collections import Counter

letters = Counter('mississippi')
numbers = Counter([5, 6, 7, 1, 3, 9, 9, 1, 2, 5, 5, 7, 7, 9])

print(letters.most_common())    # [('i', 4), ('s', 4), ('p', 2), ('m', 1)]
print(numbers.most_common())    # [(5, 3), (7, 3), (9, 3), (1, 2), (6, 1), (3, 1), (2, 1)]


print(letters.most_common(3))   # [('i', 4), ('s', 4), ('p', 2)]
print(numbers.most_common(4))   # [(5, 3), (7, 3), (9, 3), (1, 2)]


print(letters.most_common()[-1])    # ('m', 1)
print(letters.most_common()[::-1])  # [('m', 1), ('p', 2), ('s', 4), ('i', 4)]
print(numbers.most_common()[-3:-1]) # [(6, 1), (3, 1)]



