""" 
Task: The legion of Caesar, created in the 23rd century on the 
basis of the Roman Empire, does not change the ancient traditions 
and uses the Caesar cipher. 
This let them down, because this cipher is very simple. 
However, in the post-apocalypse, people do not know well all the 
intricacies of the pre-war world, so scientists from the NKR cannot 
figure out exactly how to decode these messages. 
Write a program to decode this cipher.
"""

shift = int(input())
given_string = input()

for element in given_string:
    cur_n = ord("a") + (ord(element) - ord("a") + 26 - shift) % 26
    print(chr(cur_n), end="")