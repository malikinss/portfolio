#!/usr/bin/python3

from pyrob.api import *


def check_and_fill():
    if cell_is_filled() == False:
        fill_cell()        


def fill_if_no_walls_left_right():
    if wall_is_on_the_left() == False and wall_is_on_the_right() == False:
            check_and_fill()


def move_left_till_wall_and_step_down():
    while wall_is_on_the_left() == False:
        move_left()
        fill_if_no_walls_left_right()

    if wall_is_on_the_left():
        move_down()


def move_right_till_wall_and_step_down():
    while wall_is_on_the_right() == False:
        move_right()
        fill_if_no_walls_left_right()

    if wall_is_on_the_right():
        move_down()


@task(delay=0.05)
def task_4_3():

    for _ in range(6):
        move_right_till_wall_and_step_down()
        move_left_till_wall_and_step_down()
    move_right()

if __name__ == '__main__':
    run_tasks()
