# Write a program to print the length of the string.
x = "Hello world!"
print(len(x))

# Write a program to get the first character of the string txt.
txt = "Hello world!"
x = txt[0]

# Write a program to get the characters from index 2 to index 4 (llo).
txt = "Hello world!"
x = txt[2:5]

# Return the string without any whitespace at the beginning or the end.
txt = " Hello World "
x = txt.strip()

# Convert the value of txt to upper case.
txt = "Hello World"
txt = txt.upper()

# Convert the value of txt to lower case.
txt = "Hello World"
txt = txt.lower()

# Replace the character H with a J.
txt = "Hello World"
txt = txt.replace("H", "J")

# Write a program to add a placeholder for the age parameter.
age = 36
txt = "My name is John, and I am {}"
print(txt.format(age))