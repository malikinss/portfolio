#!/usr/bin/python3

from pyrob.api import *

def go_to_up_left_corner():
    if wall_is_on_the_right():
        while wall_is_above() == False:
            move_up()

        while wall_is_on_the_left() == False:
            move_left()
    elif wall_is_on_the_left:
        while wall_is_above() == False:
            move_up()
        

def move_right_till_wall():
    while wall_is_on_the_right() == False:
        move_right()


def move_left_till_wall():
    while wall_is_on_the_left() == False:
        move_left()


def check_is_right_closed():
    if wall_is_on_the_right() and wall_is_above() and wall_is_beneath():
        return True
    return False


def check_is_left_closed():
    if wall_is_on_the_left() and wall_is_above() and wall_is_beneath():
        return True
    return False


@task
def task_8_29():
    is_right_closed = False
    is_left_closed = False

    move_right_till_wall()
    is_right_closed = check_is_right_closed()

    if is_right_closed:
        move_left_till_wall()
        is_left_closed = check_is_left_closed()

        if is_left_closed:
            move_right_till_wall()
        else:
            go_to_up_left_corner()
    else:
        go_to_up_left_corner()


if __name__ == '__main__':
    run_tasks()
