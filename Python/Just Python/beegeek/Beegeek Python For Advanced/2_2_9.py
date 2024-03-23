'''
TODO: Given a string of text consisting of the letters "H" and "T". 
The letter "H" corresponds to the appearance of Heads, and the letter "T" to the appearance of Tails. 
Write a program that counts the greatest number of consecutive Heads.
NOTE: If there are no Tails, then you need to output the number 0.
'''

s = input()
seq = s.split("H")  # remove all heads and group tails

mx = 0  # maximum number of consecutive heads

for el in seq:
    mx = max(mx, el.count("T"))
    
print(mx)