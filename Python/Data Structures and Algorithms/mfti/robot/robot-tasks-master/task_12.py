#!/usr/bin/python3

from pyrob.api import *


@task
def task_8_6():
    while wall_is_on_the_right() == False:
        
        if (cell_is_filled() == False) and (wall_is_above() == False and wall_is_beneath() == True):
            fill_cell()

        move_right()
        
        if (cell_is_filled() == False) and (wall_is_above() == False and wall_is_beneath() == True):
            fill_cell()


if __name__ == '__main__':
    run_tasks()
