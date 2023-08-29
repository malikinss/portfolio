#!/usr/bin/python3

from pyrob.api import *


def check_and_fill():
    if cell_is_filled() == False:
        fill_cell()    

def move_down_check_fill(steps, cur_round):
    for i in range(steps):
        move_down()
        if i == 0:
            check_and_fill()


def move_up_check_fill(steps, cur_round):
    for i in range(steps):
        move_up()
        if i == 0:
            check_and_fill()


def move_left_check_fill(steps, cur_round):
    for i in range(steps):
        move_left()
        if i == 0 and cur_round != 1:
            check_and_fill()


def move_right_check_fill(steps, cur_round):
    for i in range(steps):
        move_right()
        if i == 0:
            check_and_fill()

@task
def task_2_2():
    move_down()

    for j in range(5):
        steps = 2

        for i in range(2):

            move_down_check_fill(steps, i)
            move_right_check_fill(steps, i)
            move_up_check_fill(steps, i)
            move_left_check_fill(steps, i)

            steps -= 1
            
        if j < 4:
            move_right(4)


if __name__ == '__main__':
    run_tasks()
