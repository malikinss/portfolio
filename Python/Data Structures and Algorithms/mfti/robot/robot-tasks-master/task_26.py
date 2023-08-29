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


def fill_a_cross():
    steps = 2

    for i in range(2):

        move_down_check_fill(steps, i)
        move_right_check_fill(steps, i)
        move_up_check_fill(steps, i)
        move_left_check_fill(steps, i)

        steps -= 1


def fill_n_crosses(number, side):
    for j in range(number):
        fill_a_cross()

        if j < number - 1:
            if side == "right":
                move_right(4)
            elif side == "left":
                move_left(4)


def move_left_to_wall():
    while wall_is_on_the_left() == False:
                move_left()  

@task(delay=0.02)
def task_2_4():

    for i in range(3):
        fill_n_crosses(10, "right")

        if i != 2:
            move_down(4)

            fill_n_crosses(10, "left")
            move_down(4)
        elif i == 2:
            move_left_to_wall()



if __name__ == '__main__':
    run_tasks()
