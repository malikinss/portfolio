""" 
Task: A well-known Courier in the wastelands of Mojave has wandered into Hidden Valley, the secret bunker of the Brotherhood of Steel, and kindly agrees to help them solve their problems. One such problem was a strange computer virus that manifested itself in the form of program comments appearing on the Brotherhood of Steel's terminals. The Brotherhood programmers are known to never leave comments on the code and write programs in Python, so removing all these comments will not harm them in any way. Help the scribe Ibsen remove all comments from the program.
"""

n = input()

for _ in range(int(n[1:])):
    s = input()
    
    if '#' in s:
        s = s[:s.find('#')]
    
    print(s.rstrip())