#!/usr/bin/python3

from pyrob.api import *


def move_down_to_wall():
    while wall_is_beneath() == False:
        move_down()


def move_left_to_wall():
    while wall_is_on_the_left() == False:
        move_left()


def move_right_to_wall():
    while wall_is_on_the_right() == False:
        move_right()


def look_down_hole():
    flag = 0
    while wall_is_beneath():
        if wall_is_beneath == False:
            break
        
        if flag == 0:
            move_left()
        
            if wall_is_on_the_left():
                flag += 1
        elif flag == 1:
            move_right()
            
            if wall_is_on_the_right():
                flag += 1
        else:
            break
    return(flag)                


def run_in_layer():
    move_down_to_wall()
    flag = look_down_hole()
    return(flag)


def left_down_corner():
    return (wall_is_beneath() and wall_is_on_the_left())    


@task(delay=0.01)
def task_8_30():
    flag = 0

    while flag != 2:
        flag = run_in_layer()

    move_left_to_wall()    

if __name__ == '__main__':
    run_tasks()
