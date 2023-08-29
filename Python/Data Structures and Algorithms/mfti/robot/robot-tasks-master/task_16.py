#!/usr/bin/python3

from pyrob.api import *

def move_up_till_wall():
    while wall_is_above() == False:
        move_up()


def move_left_till_wall():
    while wall_is_on_the_left() == False:
        move_left()


def move_right_till_wall():
    while wall_is_on_the_right() == False:
        move_right()

@task
def task_8_22():
    
    move_up_till_wall()
    
    if wall_is_on_the_left():
        move_right_till_wall()
        
    elif wall_is_on_the_right():
        move_left_till_wall()       


if __name__ == '__main__':
    run_tasks()
