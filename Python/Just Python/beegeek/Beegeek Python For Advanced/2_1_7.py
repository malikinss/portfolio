'''
TODO: A natural number is given as input to the program. 
Write a program that inserts commas into a given number according to the standard American convention for commas in large numbers.
'''

seq = list(input())
new_s = ""

while len(seq) >= 3:
    # tear off the last 3 digits and put a comma after them
    new_s += seq.pop(-1) + seq.pop(-1) + seq.pop(-1) + ","  

# process the numbers that could remain (there are 1 or 2 of them)
new_s += "".join(seq[::-1])

# turn the result back to its original form
new_s = new_s[::-1]  
new_s = new_s.lstrip(",")  # remove the extra comma

print(new_s)