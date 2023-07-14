""" 
Task: Jim Hopper tries to get a message from Eleven using the radio. 
The receiver receives n different Morse code sequences. 
Having decoded them, he receives sequences of numbers and a lowercase 
Latin alphabet, while all of Eleven's messages contain the number 11, 
and at least 3 times. 
Help Jim determine the number of messages from Eleven.
"""

n = int(input())
msg_cnt = 0

for i in range(n):
    message = input()

    if message.count('11') >= 3:
        msg_cnt += 1 

print(msg_cnt)