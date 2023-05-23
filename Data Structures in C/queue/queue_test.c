#include <stdio.h> /* printf */

#include "queue.h"

#define RED "\033[0;31m"
#define GREEN "\033[0;32m"
#define NC "\033[0m"

#define SUCCESS (0)
#define FAIL (1)

static const char *ok = GREEN"ok"NC;
static const char *not_ok = RED"not ok"NC;

static void PrintTestFailed(char *name, int line, long exp, long got);
static int IsFailed(int expression, char *name, long exp, long got);
static int TestQueue();
static void DestroyAll(queue_t *queue, queue_t *queue2);
static void TestQueueEnqueue(int *t1, int *t2, int *t3, queue_t *queue);
static void TestQueueDequeue(queue_t *queue);
static int TestQueueIsEmpty(queue_t *queue, long exp);
static int TestAction(int expression, char *name, long exp, long got);
static int TestQueuePeek(queue_t *queue, long exp);
static int TestQueueSize(queue_t *queue, long exp);
static int TestQueueAppend(queue_t *queue, queue_t *queue2, long exp);

int main()
{
	
	queue_t *queue = QueueCreate();
	printf("\n");
	printf("All functions is %s\n\n", TestQueue(queue) ? not_ok : ok);

	return (0);
}

static int TestQueue(queue_t *queue)
{
	int t1 = 1, t2 = 2, t3 = 3, t4 = 4, t5 = 5, t6= 6;
	int status = SUCCESS;

	queue_t *queue2 = QueueCreate();
	TestQueueEnqueue(&t1, &t2, &t3, queue);
	TestQueueEnqueue(&t4, &t5, &t6, queue2);
			
	status = TestQueuePeek(queue, 1);
	status = TestQueueIsEmpty(queue, 0);
	status = TestQueueSize(queue, 3);
	status = TestQueueSize(queue2, 3);
	status = TestQueueAppend(queue, queue2, 6);
	status = TestQueueIsEmpty(queue2, 1);

	TestQueueDequeue(queue);
			
	status = TestQueuePeek(queue, 5);

	DestroyAll(queue, queue2);
	
	return (status);
}

static void DestroyAll(queue_t *queue, queue_t *queue2)
{
	QueueDestroy(queue);
	QueueDestroy(queue2);
}

static void TestQueueEnqueue(int *t1, int *t2, int *t3, queue_t *queue)
{
	QueueEnqueue(queue, t1);
	QueueEnqueue(queue, t2);
	QueueEnqueue(queue, t3);
}

static void TestQueueDequeue(queue_t *queue)
{
	size_t i = 0;
	for (i = 0; i < 4; ++i)
	{
		QueueDequeue(queue);
	}
}

static int TestAction(int expression, char *name, long exp, long got)
{
	int status = IsFailed(expression, name, exp, got);
	printf("%s %s\n",name, ok);
	return (status);
}

static int TestQueuePeek(queue_t *queue, long exp)
{
	long action = *(int *)QueuePeek(queue);
	int expression = (exp != action);	
	return (TestAction(expression, "Test QueuePeek", exp, action));
}

static int TestQueueSize(queue_t *queue, long exp)
{
	long action = QueueSize(queue);
	int expression = (exp != action);
	return(TestAction(expression, "Test QueueSize", exp, action));
}

static int TestQueueAppend(queue_t *queue, queue_t *queue2, long exp)
{
	long action = 0;
	int expression = 0;
	QueueAppend(queue, queue2);
	action = QueueSize(queue);
	expression = (exp != action);
	return(TestAction(expression, "Test QueueAppend", exp, action));
}

static int TestQueueIsEmpty(queue_t *queue, long exp)
{
	long action = QueueIsEmpty(queue);
	int expression = (exp != action);
	return(TestAction(expression, "Test QueueIsEmpty", exp, action));
}

static int IsFailed(int expression, char *name, long exp, long got)
{
	if (expression)
	{
		PrintTestFailed(name, __LINE__, exp, got);
		return (1);
	}
	return (0);
}

static void PrintTestFailed(char *name, int line, long exp, long got)
{
	fprintf( stderr, RED"\n## %s failed on line %d ##\n"NC, name, line);
	fprintf( stderr, "EXPECTED: %ld\n", exp);
	fprintf( stderr, "GOT: %ld\n", got);
	printf("\n");
}

