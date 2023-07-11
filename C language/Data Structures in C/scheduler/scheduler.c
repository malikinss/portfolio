#include "task.h"
#include "pq.h"

struct scheduler
{
	pq_t *pq;                    
	task_t *curr_running_task;  // pointer to the task that we get from PQDequeue in teh beginning of SchedulerRun.
	int is_running;             // being checked in a while loop of SchedulerRun. Changed by SchedulerStop
	int remove_current_task;    // means: destroy the current task. Will be checked by SchedulerRun after the task is executed. 
	                            // Set to 1 by SchedulerRemoveTask when The current task calls it 
	                            // (by comparing using TaskISame om curr_running_task). 
}


#define SCHEDULER_T_SIZE (sizeof(scheduler_t))
#define FREE_MEMORY(ptr) {free(ptr); (ptr) = NULL;}

static void SchedulerInit(scheduler_t *scheduler, 
							pq_t *pq_to_set, 
							task_t *task_to_set, 
							int any_status, 
							int rm_cur_task);
							
static void SetSchedulerPQ(scheduler_t *scheduler, pq_t *pq_to_set);
static void SetSchedulerCurRunTask(scheduler_t *scheduler, task_t *task_to_set);
static void SetSchedulerIsRunning(scheduler_t *scheduler, int any_status);
static void SetSchedulerRemoveCurTask(scheduler_t *scheduler, int rm_cur_task);


static pq_t *GetSchedulerPQ(const scheduler_t *scheduler);
static task_t *GetSchedulerCurRunTask(const scheduler_t *scheduler);
static int GetSchedulerIsRunning(const scheduler_t *scheduler);
static int GetSchedulerRemoveCurTask(const scheduler_t *scheduler);


static pq_t *GetSchedulerPQ(const scheduler_t *scheduler)
{
	pq_t *pq_get = {0};
	
	assert(NULL != scheduler);
	
	pq_get = scheduler -> pq;
	
	return (pq_get);
}

static task_t *GetSchedulerCurRunTask(const scheduler_t *scheduler);
{
	pq_t *pq_get = 0;
	
	assert(NULL != scheduler);
	
	pq_get = scheduler -> pq;
	
	return (pq_get);
}

static int GetSchedulerIsRunning(const scheduler_t *scheduler);
static int GetSchedulerRemoveCurTask(const scheduler_t *scheduler);

scheduler_t *SchedulerCreate(void)
{
    scheduler_t *new_scheduler = {0};
    pq_t *new_pq = {0};
    
    new_scheduler = (scheduler_t *)malloc(SCHEDULER_T_SIZE);
    if (NULL != new_scheduler)
    {
    	return (NULL);
    }
    
	new_pq = PQCreate(TaskCompare);
	if (NULL != new_pq)
	{
		FREE_MEMORY(new_scheduler);
		return (NULL);
	}
	
	SchedulerInit(new_scheduler, new_pq, NULL, 0, 0);
	 	
 	return (new_scheduler);
}

void SchedulerDestroy(scheduler_t *scheduler)
{
    assert(NULL != scheduler);
    
    SchedulerClear(scheduler)
    pqdestroy
    
    
    FREE_MEMORY(scheduler);
}

/* BadUID if fails */
ilrd_uid_t SсhedulerAddTask(scheduler_t *scheduler, 
                            int (*action)(void *params), 
			                void (*cleanup)(void *params), 
				            void *action_params, void *cleanup_params,
				            size_t interval_seconds)
{
 
    
    Create new_task = TaskCreate()
        return baduid on fail    
    PqEnqueue(scheduler->pq, new_task)
        return baduid on fail    
    return(TaskGetUID(new_task));
    
}

/* 1 if uid not found and no removal */
int SchedulerRemoveTask(scheduler_t *scheduler, ilrd_uid_t uid); /* return fail if uid is not in the scheduler */
{
    if(TaskIsSame(sceduler.curr_running_task, uid))
    {
        schedul.remove_curr_task = 1;   (scheduler, after you finish running the task, please destroy the task)
    }
    else
    {
        task = PqErase(pq, TaskIsSame, &uid)
        check if task = NULL, return (1)
        
        TaskDestroy(task);
        
    }
    
    return (0)
}


int SchedulerRun(scheduler_t *scheduler)        User runs scheduler -> scheduler runs task -> task runs action() -> In action() user call Stop()
{
    scehuler.isrunning = 1;
    
    while(!isempty(scehuler) && is_running)
    {
        task = PqDequeue(pq);
        sched->current_running = task;
        
        WaitUntill(TaskGetExecutionTime(task))
        if(wait until fail)
        {
            SchedStop(scheduler);
            destroy(task);
            sched->current_running = NULL   
            return Failure;
        }
        
        status = TaskExecute(task);
        
        if(status == fail)
        {
            SchedStop(scheduler);
            destroy(task);
            sched->current_running = NULL
            return Failure;
        }
        else if(schedul.remove_curr_task == 1 || status == succ)
        {
            remove current task = 0
            TaskDestroy(task);
            sched->current_running = NULL
        }
        else if(status == reschedule)
        {
            TaskUpdateExecTime(task)
            sched->current_running = NULL
            Enqueue(task)
            check for fail
        }
    }
        
        if(isrunning == 0)
        {
            return stopped by user;
        }
   
        scehuler.isrunning = 0;    
        return Success;

}

void SchedulerStop(scheduler_t *scheduler)
{
    scheduler->is_running = 0;
}

size_t SchedulerSize(const scheduler_t *scheduler)
{
    return (PqSize(scheduler->pq))
}

int SchedulerIsEmpty(const scheduler_t *scheduler)
{
    return (PQIsEmpty(scheduler->pq))
}

void SchedulerClear(scheduler_t *scheduler)
{
    while(!PQisEmpty)
    {
        task_to_destroy = PqDequeue(shed->pq);
        TaskDestroy(task_to_destroy)
    }
}




static void SchedulerInit(scheduler_t *scheduler, pq_t *pq_to_set, task_t *task_to_set, int any_status, int rm_cur_task)
{
	assert(NULL != scheduler);
	
	SetSchedulerPQ(scheduler, pq_to_set);
	SetSchedulerCurRunTask(scheduler, task_to_set);
	SetSchedulerIsRunning(scheduler, any_status);
	etSchedulerRemoveCurTask(scheduler, rm_cur_task);
}


static void SetSchedulerPQ(scheduler_t *scheduler, pq_t *pq_to_set)
{
	assert(NULL != scheduler);
	scheduler -> pq = pq_to_set;
}


static void SetSchedulerCurRunTask(scheduler_t *scheduler, task_t *task_to_set)
{
	assert(NULL != scheduler);
	scheduler -> curr_running_task = task_to_set;
}


static void SetSchedulerIsRunning(scheduler_t *scheduler, int any_status)
{
	assert(NULL != scheduler);
	scheduler -> is_running = any_status;
}


static void SetSchedulerRemoveCurTask(scheduler_t *scheduler, int rm_cur_task)
{
	assert(NULL != scheduler);
	scheduler -> remove_current_task = rm_cur_task;
}
