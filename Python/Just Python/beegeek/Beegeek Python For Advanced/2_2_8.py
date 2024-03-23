'''
TODO: Having lost to Timur 10 times, Ruslan realized that things couldn't go on like this and decided to complicate the game. 
Now Timur and Ruslan are playing the game Rock, Paper, Scissors, Lizard, Spock. 
Help the kids cast fair lots again and determine who will do the next module in the new course.
NOTE: The rules of the game are standard: 
- The scissors cut paper. 
- The paper wraps the stone. 
- The rock crushes the lizard.
- The lizard poisons Spock
- Spock breaks the scissors
- The scissors cut off the head of the lizard
- The lizard eats the paper
- The paper contains evidence against Spock. 
- Spock vaporizes the stone
- The stone, of course, dulls the scissors.
'''

options = ["Stone", "Lizard", "Spock", "Scissors", "Paper"]
results = ["Draw", "Ruslan", "Timur", "Ruslan", "Timur"]

timur_move = input()
ruslan_move = input()

case = options.index(timur_move) - options.index(ruslan_move)
res = results[case]

print(res)