#!/usr/bin/python3

from pyrob.api import *

def is_three_cells_filled():
    counter = 1
    move_right()
    
    for _ in range(2):
        if cell_is_filled():
            counter += 1
        else:
            break

        if wall_is_on_the_right() == False and counter != 3:    
            move_right()
        else:
            break        
    
    if counter == 3:
        return(True)
    else:
        return(False)
                     

@task
def task_7_7():
    flag = False
    
    while wall_is_on_the_right() == False:
        
        if cell_is_filled():
            flag = is_three_cells_filled()
            if flag:
                break    
        
        move_right()

if __name__ == '__main__':
    run_tasks()
