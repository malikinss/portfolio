#!/usr/bin/python3

from pyrob.api import *


def left_down_corner():
    return (wall_is_beneath() and wall_is_on_the_left())


def right_down_corner():
    return (wall_is_beneath() and wall_is_on_the_right())


def left_up_corner():
    return (wall_is_above() and wall_is_on_the_left())


def right_up_corner():
    return (wall_is_above() and wall_is_on_the_right())


def only_one_cell():
    return (left_down_corner() and right_down_corner() and left_up_corner() and right_up_corner())




def right_wall_no_down_corner():
    return (wall_is_on_the_right() and wall_is_beneath() == False)


def right_wall_no_up_corner():
    return (wall_is_on_the_right() and wall_is_above() == False)


def right_wall_no_corners():
    return (right_wall_no_up_corner() and right_wall_no_down_corner())




def left_wall_no_down_corner():
    return (wall_is_on_the_left() and wall_is_beneath() == False)


def left_wall_no_up_corner():
    return (wall_is_on_the_left() and wall_is_above() == False)


def left_wall_no_corners():
    return (left_wall_no_up_corner() and left_wall_no_down_corner())




def check_and_fill():
    if cell_is_filled() == False:
        fill_cell()        


def fill_left_to_wall_stepdown():
    while wall_is_on_the_left() == False:
        check_and_fill()
        move_left()
        

    if left_wall_no_down_corner():
        check_and_fill()
        move_down()


def fill_right_to_wall_stepdown():
    while wall_is_on_the_right() == False:
        check_and_fill()
        move_right()

    if right_wall_no_down_corner():
        check_and_fill()
        move_down()


def move_right_to_wall():
    while wall_is_on_the_right() == False:
                move_right()


@task
def task_5_10(delay=0.01):


    while left_down_corner() == False:
        fill_right_to_wall_stepdown()
        fill_left_to_wall_stepdown()

    if left_down_corner() and wall_is_on_the_right() == False:
        move_right()
        
        if cell_is_filled():
            move_left()
            check_and_fill()
        
        else:
            move_right_to_wall()
            fill_left_to_wall_stepdown()
            check_and_fill()
    
    elif only_one_cell():
        check_and_fill()

if __name__ == '__main__':
    run_tasks()
