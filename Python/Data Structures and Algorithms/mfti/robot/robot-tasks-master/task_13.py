#!/usr/bin/python3

from pyrob.api import *

def go_up_fill():
    
    if wall_is_above() == False:
        move_up()
        
        if cell_is_filled() == False:
            fill_cell()

        move_down()        

def go_down_fill():
    if wall_is_beneath() == False:
        move_down()
        
        if cell_is_filled() == False:
            fill_cell()

        move_up()

    

@task
def task_8_10():
    while wall_is_on_the_right() == False:
        go_up_fill()
        go_down_fill()
        move_right()

    if wall_is_on_the_right():
        go_up_fill()
        go_down_fill()    
        


if __name__ == '__main__':
    run_tasks()
