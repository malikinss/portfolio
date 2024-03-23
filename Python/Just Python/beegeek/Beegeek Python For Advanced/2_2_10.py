'''
TODO: Artificial intelligence Anton, created by Guilfoyle, hacked a network of smart refrigerators. 
Now he uses them as servers for the Piebald Piper. 
Help the owner of the company find all the infected refrigerators.

For each refrigerator there is a data line consisting of lowercase letters and numbers, and if the word “anton” is present in it (not necessarily adjacent letters, the main thing is the presence of a sequence of letters), then the refrigerator is infected and you need to display the refrigerator number, numbering starts from one.
NOTE: If there are no Tails, then you need to output the number 0.
'''

n = int(input())

for i in range(n):
    seq = ["a", "n", "t", "o", "n"]
    s = list(input())

    # for now we have a non-empty list of letters from the string and a list of the word "anton"
    while seq and s:  
        
        # if the letters are equal, then we tear out both
        if seq[0] == s[0]:
            seq.pop(0)
            s.pop(0)
        else:
            # otherwise we only take strings from the list of letters  
            s.pop(0)

    # if the list of letters of the word "anton" is empty, then all the letters have been taken out,
    # means all these letters are found in the line in the order we need
    if not seq:
        print(i + 1, end=" ")