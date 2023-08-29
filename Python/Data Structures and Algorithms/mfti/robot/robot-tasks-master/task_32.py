#!/usr/bin/python3

from pyrob.api import *


def is_upper_dead_end():
    return (wall_is_on_the_left() and wall_is_on_the_right() and wall_is_above())


def check_and_fill():
    counter = 0
    
    if cell_is_filled():
        counter += 1
    else:
        fill_cell()
    
    return(counter)    
             

def fill_if_wall_up_down():
    counter = 0
    
    if wall_is_beneath() and wall_is_above():
        counter += check_and_fill()
    
    return(counter)    


def move_up_and_fill():
    counter = 0

    while is_upper_dead_end() == False:
            move_up()
            counter += check_and_fill()
    
    return(counter)

def move_down_to_wall():
    while wall_is_beneath() == False:
            move_down()


def look_for_column_and_fill():
    counter = 0

    if wall_is_above() == False and wall_is_beneath():
        counter += move_up_and_fill()
        move_down_to_wall()

    return(counter) 

@task(delay=0.01)
def task_8_18():
    counter = 0

    while wall_is_on_the_right() == False and wall_is_beneath():
        counter += fill_if_wall_up_down()
        counter += look_for_column_and_fill()
        move_right()

    mov('ax', counter)
        

        
        

        


if __name__ == '__main__':
    run_tasks()
