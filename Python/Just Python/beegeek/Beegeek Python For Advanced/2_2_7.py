'''
TODO: Timur and Ruslan are trying to share the front of work on the "Python for Professionals" course. 
To do this, they decided to play rock, paper and scissors. 
Help the kids cast fair lots and determine who will do the next module of the new course.
The program receives two lines of text containing the words "rock", "scissors" or "paper" as input. 
The first line records Timur's choice, the second line records Ruslan's choice.
'''

options = ["rock", "scissors", "paper"]
results = ["draw", "Ruslan", "Timur"]

timur_move = input()
ruslan_move = input()

case = options.index(timur_move) - options.index(ruslan_move)
res = results[case]

print(res)