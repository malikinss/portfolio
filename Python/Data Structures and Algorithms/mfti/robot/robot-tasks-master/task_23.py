#!/usr/bin/python3

from pyrob.api import *


def is_upper_dead_end():
    return (wall_is_on_the_left() and wall_is_on_the_right() and wall_is_above())


def check_and_fill():
    if cell_is_filled() == False:
        fill_cell()    


def go_up_and_fill():
    while is_upper_dead_end() == False:
            move_up()
            check_and_fill()

def go_down_to_wall():
    while wall_is_beneath() == False:
            move_down()

@task(delay=0.01)
def task_6_6():
    steps_right = 0
    
    while wall_is_on_the_right() == False:
        move_right()
        steps_right += 1
        
        if wall_is_above() == False:
            go_up_and_fill()
            go_down_to_wall()    

    move_left(n = steps_right)                


if __name__ == '__main__':
    run_tasks()
