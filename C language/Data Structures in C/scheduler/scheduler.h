#ifndef __SCHEDULER_H_ILRD__
#define __SCHEDULER_H_ILRD__

#include <stddef.h> /* size_t */

#include "uid.h" /* ilrd_uid_t */


typedef struct scheduler scheduler_t;

typedef enum scheduler_run_status
{
SUCCESS,
FAILURE,
STOPPED
} scheduler_run_status_t;


scheduler_t *SchedulerCreate(void);

void SchedulerDestroy(scheduler_t *scheduler);

/* BadUID if fails */
ilrd_uid_t SchedulerAddTask(scheduler_t *scheduler, 
                            int (*action)(void *params), 
			                void (*cleanup)(void *params), 
				            void *action_params, void *cleanup_params,
				            size_t interval_seconds);

/* 1 if uid not found and no removal */
int SchedulerRemoveTask(scheduler_t *scheduler, ilrd_uid_t uid); /* return fail if uid is not in the scheduler */

/* SUCCESS if all operations ran, FAIL if one operation failed */
int SchedulerRun(scheduler_t *scheduler);

void SchedulerStop(scheduler_t *scheduler);

size_t SchedulerSize(const scheduler_t *scheduler);

int SchedulerIsEmpty(const scheduler_t *scheduler);

void SchedulerClear(scheduler_t *scheduler);


#endif /* __SCHEDULER_H_ILRD__ */

