#!/usr/bin/python3

from pyrob.api import *


def check_and_fill():
    if cell_is_filled() == False:
        fill_cell()        


def fill_if_no_any_wall_arround():
    expression_1 = wall_is_on_the_left() == False
    expression_2 = wall_is_on_the_right() == False
    expression_3 = wall_is_beneath() == False
    expression_4 = wall_is_above() == False
    
    if expression_1 or expression_2 or expression_3 or expression_4:
            check_and_fill()


def fill_if_no_wall_beneath():
    no_wall_beneath = (wall_is_beneath() == False)
    
    if no_wall_beneath:
            check_and_fill()


def fill_if_no_wall_left():
    no_wall_left = (wall_is_on_the_left() == False)
    
    if no_wall_left:
            check_and_fill()


def move_down_right_fill_stepleft():
    while wall_is_beneath() == False:
        move_right()
        move_down()
        fill_if_no_wall_beneath()

    move_left()


def move_up_left_fill_stepdown():
    while wall_is_on_the_left() == False:
        move_left()
        move_up()
        fill_if_no_wall_left()

    move_down()


@task(delay=0.05)
def task_4_11():

    for _ in range(7):
        move_down_right_fill_stepleft()
        move_up_left_fill_stepdown()

    move_right()

    
if __name__ == '__main__':
    run_tasks()
