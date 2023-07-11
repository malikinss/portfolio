#include <stdio.h> /* printf */

#include "task.h"

op_status_t PrintHelloWorld(void *operation_params);
void DoNotClean(void *cleanup_params);

static void PrintTestResult(int expression, char *name);
static void TestFunc(int value_to_compare, int value_to_check, char *name);

int main()
{
	int expression1 = 0;
	int expression2 = 0;
	int expression3 = 0;
	
	task_t *test_task = TaskCreate(PrintHelloWorld, DoNotClean, NULL, NULL, 35);
	task_t *test_task1 = TaskCreate(PrintHelloWorld, DoNotClean, NULL, NULL, 5);

	op_status_t action_status = TaskExecute(test_task);
	
	TestFunc(SUCCESS, action_status, "TaskExecute");
		
	TestFunc(0, difftime(time(NULL) + 5, TaskGetExecutionTime(test_task1)), "TaskGetExecutionTime");
	printf("Execution time: %ld\n\n", TaskGetExecutionTime(test_task1));

	TaskUpdateExecTime(test_task1);
	
	TestFunc(0, difftime(time(NULL) + 10, TaskGetExecutionTime(test_task1)), "TaskUpdateExecTime");
	printf("New execution time: %ld\n\n", TaskGetExecutionTime(test_task1));
	
	TestFunc(1, TaskCompare(test_task, test_task1), "TaskCompare");
	
	TestFunc(1, TaskCompare(test_task, test_task1), "TaskCompare");
	
	expression1 = 0 == TaskIsSame(test_task, test_task1);
	expression2 = 1 == TaskIsSame(test_task, test_task);
	
	PrintTestResult(expression1 && expression2, "TaskIsSame");
	
	expression1 = !UIDIsSame(BadUID, TaskGetUID(test_task));
	expression2 = !UIDIsSame(TaskGetUID(test_task), TaskGetUID(test_task1));
	expression3 = UIDIsSame(TaskGetUID(test_task), TaskGetUID(test_task));
	
	PrintTestResult((expression1 && expression2 && expression3), "TaskGetUID");

	TaskDestroy(test_task);
	TaskDestroy(test_task1);

	return (0);
}


op_status_t PrintHelloWorld(void *operation_params)
{
	printf("Hello, World!\n");

	return (SUCCESS);
	(void)operation_params;
} 

void DoNotClean(void *cleanup_params)
{
	return;
	(void)cleanup_params;
}

static void PrintTestResult(int expression, char *name)
{
	if (expression)
    {
        printf("%s test is passed\n", name);
    }
    else
    {
        printf("%s test is failed\n", name);
    }
}

static void TestFunc(int value_to_compare, int value_to_check, char *name)
{
	int expression = 0;
	
	expression = (value_to_compare == value_to_check);
    PrintTestResult(expression, name);
}
