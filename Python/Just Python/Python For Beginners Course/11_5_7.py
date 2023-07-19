""" 
Task: The input to the program is a text string containing natural numbers. A list of numbers is formed from this string. Write a program that counts how many pairs of elements in the resulting list are equal to each other. It is believed that any two elements that are equal to each other form one pair, which must be calculated.
"""

num, count = input().split(), 0

for i in range(len(num)):
    for j in range(i + 1, len(num)):
        if num[i] == num[j]:
            count += 1
            
            
print(count)