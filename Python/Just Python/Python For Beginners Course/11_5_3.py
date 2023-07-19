""" 
Task: In the Windows operating system, the full file name consists of a drive letter followed by a colon and the \ character, then the subdirectories (folders) in which the file is located are listed through the same character, and the file name is written at the end (C:\Windows\System32 \calc.exe).

The input to the program is one line with the correct file name in the Windows operating system. 
Write a program that parses a string into pieces separated by the \ character. 
Print each part on a separate line.
"""

s = input()
a = '\\'
lst = s.split(a)
print(*lst, sep = '\n')  