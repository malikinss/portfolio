""" 
Task: Edit the code below to:
Replaced the second element of the list with 17;
Added the numbers 4, 5 and 6 to the end of the list;
Removed the first element of the list;
Doubled the list;
Inserted the number 25 at index 3;
Printed out a list using the print() function
"""

# original code
numbers = [8, 9, 10, 11]

# fixed code
numbers = [8, 9, 10, 11]
numbers[1] = 17
numbers.extend([4,5,6])
del numbers[0]
numbers *= 2
numbers.insert(3,25)
print(numbers)