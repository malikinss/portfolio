'''
TODO:   
        Anri and Dima, having a box with an endless number of socks on their hands, decided to play a game. 
        
        The guys take turns taking an arbitrary number of socks out of the box, and after an indefinite number of moves the game ends. 
        
        If the one who made the last move drew an even number of socks, he wins, otherwise he loses.
        
        Write a program that determines the winner of this game if Anri makes the first move.    

'''
import sys

PLAYERS = ['ANRI', 'DIMA']

def get_next_player(data):
    if get_last_player(data) == PLAYERS[1]:
        return PLAYERS[0]
    elif get_last_player(data) == PLAYERS[0]:
        return PLAYERS[1]

def get_last_player(data):
    if len(data) % 2 == 0:
        return PLAYERS[1]
    
    return PLAYERS[0]

def is_win(move):
    return move % 2 == 0

def get_moves_values():
    return [line.strip() for line in sys.stdin.readlines()]

def determine_winner():
    moves_values = get_moves_values()
    moves_values = list(map(int, moves_values))

    if is_win(moves_values[-1]):
        print(get_last_player(moves_values))
    else:
        print(get_next_player(moves_values))

determine_winner()