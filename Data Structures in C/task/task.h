/* Header file for task.
Task refers to a specific unit of work that needs to be executed by the
computer system.
The task is a tool for scheduler to manage and prioritize the execution
of various operations or processes running on a computer system. The scheduler
decides which tasks to execute, when to execute them, and for how long they
should run.

*****************************************
* Title : task function declarations	*
* Author: Sam Malikin					*
* Reviewer: Dima						*
* Date : 08.05.2023						*
*****************************************
*/


#ifndef __TASK_H_ILRD__
#define __TASK_H_ILRD__

#include <time.h> /* time_t */

#include "uid.h" /* ilrd_uid_t */

typedef struct task task_t;

typedef enum op_status {SUCCESS, RESCHEDULE, FAILURE} op_status_t;

/*
DESCRIPTION
    A pointer to a user's function that executes a task using
    the operation_params.
    The actual action and types of the input are defined by the user.
RETURN
    SUCCESS - if success and no need to reschedule the task.
    RESCHEDULE - if success and need to reschedule the task.
    FAILURE - if fail.
INPUT
    operation_params: a pointer to a some parameter for action.
*/
typedef op_status_t (*task_action_t)(void *operation_params);

/*
DESCRIPTION
    A pointer to a user's function that clean up after a task execution
    using the cleanup_params.
    The actual clean up pattern and types of the input are defined by the user.
RETURN
    Doesn't return anything.
INPUT
    operation_params: a pointer to a some parameter for clean up.
*/                                            
typedef void(*task_cleanup_t)(void *cleanup_params);

/*
DESCRIPTION
    Creates new task.
    Creation may fail, due to memory allocation fail.
    User is responsible for destroying tasks.
RETURN
    Pointer to the created sorted linked list on success.
    NULL if allocation failed.
INPUT
    action_func: pointer to action function.
    clean_func: pointer to cleanup function.
    operation_params: pointer to users params for action.
    cleanup_params: pointer to users params for cleanup.
    interval_seconds: how many seconds before execute(s) after creating task.
*/
task_t *TaskCreate(task_action_t action_func,
                    task_cleanup_t clean_func,
                    void *operation_params,
                    void *cleanup_params,
                    size_t interval_seconds);

/* 
DESCRIPTION
	Destroys a task by deallocating memory and running the cleanup function
	with provided parameters. 
RETURN
	There is no return for this function.
INPUT
	task - a pointer to the task.
*/
void TaskDestroy(task_t *task);

/* 
DESCRIPTION
	Runs the execute function using its parameters. Returns status if 
	the function needs to be rescheduled nd if it was succesful.
RETURN
	0 - execution succesful and no rescheduling needed;
	1 - execution succesful and needs to be rescheduled;
	2 - execution failed.
INPUT
	task - a pointer to the task.
*/
/* return action status */ 
op_status_t TaskExecute(task_t *task); 

/* 
DESCRIPTION
	Compares execution time of two tasks.
RETURN
	-1 - if task1 is scheduled earlier than task2;
	0 - if tasks are scheduled on the same time;
	1 - if task1 is scheduled later than task2. 
INPUT
	task1 - a pointer to the task;
	task2 - a pointer to the task.
*/
int TaskCompare(const void *task1, const void *task2); 

/* 
DESCRIPTION
	Copares UIDs of two tasks. 
RETURN
	1 - UIDs are the same;
	0 - UIDs are not the same. 
INPUT
	task1 - a pointer to the task;
	task2 - a pointer to the task.
*/
int TaskIsSame(const task_t *task1, const task_t *task2); 

/* 
DESCRIPTION
	Returns the UID of a task.
RETURN
	UID of a task by value.
INPUT
	task1 - a pointer to the task;
	task2 - a pointer to the task.
*/
ilrd_uid_t TaskGetUID(const task_t *task);

/* 
DESCRIPTION
	Returns the scheduled execution time of a task.
RETURN
	Execution time in seconds since UNIX Epoch.
INPUT
	task - a pointer to the task.
*/
time_t TaskGetExecutionTime(const task_t *task);

/* 
DESCRIPTION
	Changes the execution time of a task by the interval in seconds,
	stored in the task.
RETURN
	Execution time in seconds since UNIX Epoch.
INPUT
	task - a pointer to the task.
*/
void TaskUpdateExecTime(task_t *task);

#endif /* __TASK_H_ILRD__ */


