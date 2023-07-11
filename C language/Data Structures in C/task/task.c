/*
*************************************
* Title : task function definitions	*
* Author: Sam Malikin				*
* Reviewer: Dima					*
* Date : 08.05.2023					*
*************************************
*/
#include <assert.h>
#include <stdlib.h>
#include <limits.h>

#include "task.h"

#define TIME_T_MAX ((time_t)LONG_MAX)
#define TASK_T_SIZE (sizeof(task_t))
#define FREE_MEMORY(ptr) {free(ptr); (ptr) = NULL;}

static void SetTaskId(task_t *task, ilrd_uid_t new_id);
static void SetTaskActionFunc(task_t *task, task_action_t action);
static void SetTaskCleanFunc(task_t *task, task_cleanup_t clean);
static void SetTaskActionParams(task_t *task, void *params);
static void SetTaskCleanUpParams(task_t *task, void *params);
static void SetTaskExecutionTime(task_t *task, time_t time);
static void SetTaskInterval(task_t *task, size_t interval);
static size_t TaskGetInterval(const task_t *task);
static int CompareExecTime(time_t exec_time1, time_t exec_time2);


struct task
{
    ilrd_uid_t task_id;
    task_action_t action_func;
    task_cleanup_t clean_func;
    void *operation_params;
    void *cleanup_params;
    
    time_t execution_time; 
    size_t interval_seconds;
    
};


task_t *TaskCreate(task_action_t action, 
					task_cleanup_t clean_up, 
					void *params, 
					void *cleanup_params,  
					size_t interval_seconds)
{
	task_t *new_task = NULL;
	ilrd_uid_t new_id = {0};
	time_t current_time	= 0;
	time_t time_to_set	= 0;
	
	assert(NULL != action);
    assert(NULL != clean_up);
    
    if ((time_t)-1 == time(&current_time))
    {
        return (NULL);
    }
	
	assert(TIME_T_MAX - current_time > (time_t)interval_seconds);
	
	new_id = UIDCreate();
    if(UIDIsSame(new_id, BadUID))
    {
    	return (NULL);
    }
    
    new_task = (task_t *)malloc(TASK_T_SIZE);
    if (NULL == new_task)
    {
    	return (NULL);
    }
    
    SetTaskId(new_task, new_id);
    SetTaskActionFunc(new_task, action);
    SetTaskCleanFunc(new_task, clean_up);
    SetTaskActionParams(new_task, params);
    SetTaskCleanUpParams(new_task, cleanup_params);
    
    time_to_set = current_time + (time_t)interval_seconds;
	SetTaskExecutionTime(new_task, time_to_set);

	SetTaskInterval(new_task, interval_seconds);
    
    return (new_task);
}



void TaskDestroy(task_t *task)
{
	task_cleanup_t CleanUp = NULL;
	void *params = NULL;
	    
	assert(NULL != task);
	assert(NULL != task->clean_func);
	
	CleanUp = task->clean_func;
	params = task->cleanup_params;
	
	CleanUp(params);
	
	FREE_MEMORY(task);
}


op_status_t TaskExecute(task_t *task)
{
    op_status_t operation_status = SUCCESS;
    task_action_t Action = NULL;
    void *params = NULL;

    assert(NULL != task);
    assert(NULL != task->action_func);

    Action = task->action_func;
    params = task->cleanup_params;

    operation_status = Action(params);

    return (operation_status);
}


int TaskCompare(const void *task1, const void *task2)
{
	time_t task1_exec_time = 0;
	time_t task2_exec_time = 0;
	
	int status = 0;
	
	assert(NULL != task1);
	assert(NULL != task2);
	
	task1_exec_time = TaskGetExecutionTime((const task_t *)task1);
	task2_exec_time = TaskGetExecutionTime((const task_t *)task2);
	
	status = CompareExecTime(task1_exec_time, task2_exec_time);
	
	return (status);
	
}


int TaskIsSame(const task_t *task1, const task_t *task2)
{
	int result = 0;
	ilrd_uid_t uid_1 = {0};
	ilrd_uid_t uid_2 = {0};
	
	assert(NULL != task1);
	assert(NULL != task2);
	
	uid_1 = TaskGetUID(task1);
	uid_2 = TaskGetUID(task2);
	
	result = UIDIsSame(uid_1, uid_2);
	
	return (result);	
}


ilrd_uid_t TaskGetUID(const task_t *task)
{
	ilrd_uid_t uid = {0};
	
	assert(NULL != task);
	
	uid = task -> task_id;
	
	return (uid);
}

time_t TaskGetExecutionTime(const task_t *task)
{
	time_t get_exec_time = 0;
	
	assert(NULL != task);
	
	get_exec_time = task -> execution_time;
	
	return (get_exec_time);
}

void TaskUpdateExecTime(task_t *task)
{
	time_t new_exec_time = 0;
	task_cleanup_t CleanUp = NULL;
	void *params = NULL;
	
	assert(NULL != task);
	assert(NULL != task->clean_func);
	assert(TIME_T_MAX - task->execution_time > (time_t)task->interval_seconds);
	
	CleanUp = task->clean_func;
	params = task->cleanup_params;
	
	CleanUp(params);
	
	new_exec_time = TaskGetExecutionTime(task);
	new_exec_time += TaskGetInterval(task);
	SetTaskExecutionTime(task, new_exec_time);
}

static void SetTaskExecutionTime(task_t *task, time_t time)
{
	assert(NULL != task);
	task -> execution_time = time;
}

static void SetTaskId(task_t *task, ilrd_uid_t new_id)
{
	assert(NULL != task);
	task -> task_id = new_id;
}

static void SetTaskActionFunc(task_t *task, task_action_t action)
{
	assert(NULL != task);
	task -> action_func = action;
}

static void SetTaskCleanFunc(task_t *task, task_cleanup_t clean)
{
	assert(NULL != task);
	task -> clean_func = clean;
}

static void SetTaskActionParams(task_t *task, void *params)
{
	assert(NULL != task);
	task -> operation_params = params;
}

static void SetTaskCleanUpParams(task_t *task, void *params)
{
	assert(NULL != task);
	task -> cleanup_params = params;
}

static void SetTaskInterval(task_t *task, size_t interval)
{
	assert(NULL != task);
	task -> interval_seconds = interval;
}

static size_t TaskGetInterval(const task_t *task)
{
	size_t interval = 0;
	
	assert(NULL != task);
	
	interval = task -> interval_seconds;
	
	return (interval);
}

static int CompareExecTime(time_t exec_time1, time_t exec_time2)
{
	if (exec_time1 < exec_time2)
	{
		return (-1);
	}
	
	if (exec_time1 > exec_time2)
	{
		return (1);
	}
	
	return (0);
}
