# Write a program to print "Hello World" if a is greater than b.
a = 50
b = 10

if a > b:
    print("Hello World")

# Write a program to print "Hello World" if a is not equal to b.
a = 50
b = 10

if a != b:
    print("Hello World")

# Write a program to print "Yes" if a is equal to b, otherwise print "No".
a = 50
b = 10

if a == b:
    print("Yes")
else:
    print("No")

# Write a program to print "1" if a is equal to b, print "2" if a is greater than b, otherwise print "3".
a = 50
b = 10

if a == b:
    print("1")
elif a > b:
    print("2")
else:
    print("3")


# Write a program to print "Hello" if a is equal to b, and c is equal to d.
if a == b and c == d:
    print("Hello")

# Write a program to print "Hello" if a is equal to b, or c is equal to d.
if a == b or c == d:
    print("Hello")

''' 
This example misses indentations to be correct.
Insert the missing indentation to make the code correct:
if 5 > 2:
print("Five is greater than two!")  
'''
if 5 > 2:
    print("Five is greater than two!")

# Use the correct short hand syntax to put the following statement on one line: 
if 5 > 2: print("Five is greater than two!")
 
''' 
Use the correct short hand syntax to write the following conditional expression in one line:
if 5 > 2:
  print("Yes")
else
  print("No")
'''
print("Yes") if 5 > 2 else print("No")