#!/usr/bin/python3

from pyrob.api import *


def check_and_fill():
    if cell_is_filled() == False:
        fill_cell()  

def get_layer_length():
    length = 0
    
    while wall_is_on_the_right() == False:
        move_right()
        length += 1

    move_left(length)
    return(length)


@task(delay=0.01)
def task_9_3():
    n = get_layer_length()

    for i in range(n + 1):

        for j in range(n + 1):

            j_not_equal_i = (j != i)
            j_not_n_minus_one = (j != (n - i))
            expression = (j_not_equal_i and j_not_n_minus_one)

            if expression:
                check_and_fill()

            if i % 2 == 0 and j < n:
                move_right()
                
            elif i % 2 != 0 and j < n:
                move_left()                      

        if i != n:
            move_down()
        else:
            move_left(n)            
            





if __name__ == '__main__':
    run_tasks()
