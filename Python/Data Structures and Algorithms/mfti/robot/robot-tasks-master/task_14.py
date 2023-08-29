#!/usr/bin/python3

from pyrob.api import *

def check_and_fill():
    if cell_is_filled() == False:
        fill_cell()


def go_up_fill():
    
    if wall_is_above() == False:
        move_up()
        check_and_fill()
        move_down()        


def go_down_fill():
    if wall_is_beneath() == False:
        move_down()
        check_and_fill()
        move_up()


def fill_in_middle():
    if wall_is_beneath() and wall_is_above():
        check_and_fill()


@task
def task_8_11():
    while wall_is_on_the_right() == False:
        go_up_fill()
        go_down_fill()
        fill_in_middle()
        move_right()

    if wall_is_on_the_right():
        go_up_fill()
        go_down_fill()
        fill_in_middle()  


if __name__ == '__main__':
    run_tasks()
