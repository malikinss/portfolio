#!/usr/bin/python3

from pyrob.api import *


def check_and_fill():
    if cell_is_filled() == False:
        fill_cell()  


@task
def task_7_5():
    
    cur_pos = 1
    prev_pos = cur_pos

    step = 1

    move_right()
    check_and_fill()
    cur_pos += 1

    while wall_is_on_the_right() == False:
        move_right()
        
        if cur_pos == prev_pos + step and wall_is_on_the_right() == False:
            check_and_fill()
            step += 1
            prev_pos = cur_pos

        cur_pos += 1        



if __name__ == '__main__':
    run_tasks()
