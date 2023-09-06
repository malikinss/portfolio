'''
TODO: Recall that the string find('a') method returns the location of the first occurrence of the character 'a' in the string. 
The problem is that this method does not find the location of all "a"'s.

Write a function called find_all(target, symbol) that takes two arguments: the string target and the symbol symbol, and returns a list containing all locations of that symbol in the string.

NOTE: If the specified character does not occur in the string, then an empty list should be returned.
'''


def find_all(target, symbol):
    return [i for i in range(len(target)) if target[i] == symbol]


s = input()
char = input()


print(find_all(s, char))