#!/usr/bin/python3

from pyrob.api import *

def zig_zag_down_right():
    while wall_is_beneath() == False and wall_is_on_the_right() == False:
        move_down()
        move_right()


def zig_zag_down_left():
    while wall_is_beneath() == False and wall_is_on_the_left() == False:
        move_down()
        move_left()


def zig_zag_up_right():
    while wall_is_above() == False and wall_is_on_the_right() == False:
        move_up()
        move_right()


def zig_zag_up_left():
    while wall_is_above() == False and wall_is_on_the_left() == False:
        move_up()
        move_left()


@task
def task_8_21():
    
    if wall_is_above() and wall_is_on_the_left():
        zig_zag_down_right()
    elif wall_is_above() and wall_is_on_the_right():
        zig_zag_down_left()
    elif wall_is_beneath() and wall_is_on_the_right():
        zig_zag_up_left()
    elif wall_is_beneath() and wall_is_on_the_left():
        zig_zag_up_right()           
    

if __name__ == '__main__':
    run_tasks()
