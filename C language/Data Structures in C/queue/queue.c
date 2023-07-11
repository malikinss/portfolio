/***********************************************************************
* FILENAME : queue.c
*
* DESCRIPTION :
*       Implementation of a queue data structure.
*
* PUBLIC FUNCTIONS :
*		queue_t *QueueCreate(void); 
*		void QueueDestroy(queue_t *queue); 
*		int QueueEnqueue(queue_t *queue, void *data); 
*		void QueueDequeue(queue_t *queue); 
*		void *QueuePeek(const queue_t *queue); 
*		int QueueIsEmpty(const queue_t *queue); 
*		size_t QueueSize(const queue_t *queue); 
*		queue_t *QueueAppend(queue_t *dest, queue_t *src); 
* 
* 
* AUTHOR : Sam Malikin       REVIEWED BY : Sergei
*
* LAB : OL142
*/

#include <assert.h> /* assert() */
#include <stdlib.h> /* malloc */

#include "queue.h"
#include "slinkedlist.h"

#define FREE_MEMORY(ptr) {free(ptr); (ptr) = NULL;}

typedef enum 
{ 
	SUCCESS, 
	FAIL
} status_t;

struct queue 
{ 
	list_t *list; 
};

static status_t CheckExpression(int expr, status_t true_t, status_t false_t);

queue_t *QueueCreate(void)
{
    queue_t *new_queue = (queue_t *) malloc(sizeof(queue_t));
	if (NULL == new_queue)
	{
		return (NULL);
	}

	new_queue -> list = SLinkedListCreate();
	if (NULL == new_queue -> list)
	{
		FREE_MEMORY(new_queue);
		return (NULL);
	}

	return (new_queue);
}

void QueueDestroy(queue_t *queue)
{
	assert(NULL != queue);

	SLinkedListDestroy(queue -> list);

	FREE_MEMORY(queue);

}

int QueueEnqueue(queue_t *queue, void *data)
{
	slist_iterator_t cur_end_iterator = NULL;
    slist_iterator_t check_iterator = NULL;
	
	int expression = 0;
	status_t result = SUCCESS;
	
	assert(NULL != queue);
	assert(NULL != data);
	
	cur_end_iterator = SlinkedListEnd(queue -> list);
	check_iterator = SlinkedListInsert(cur_end_iterator, data);
	cur_end_iterator = SlinkedListEnd(queue -> list);
	expression = SlinkedListIsSameIterator(cur_end_iterator, check_iterator);
	result = CheckExpression(expression, FAIL, SUCCESS);
	 
	return ((int)result);
}

void QueueDequeue(queue_t *queue)
{
	slist_iterator_t begin_iterator = NULL;	
	
	assert(NULL != queue);
	assert(!QueueIsEmpty(queue));
	
	begin_iterator = SlinkedListBegin(queue -> list);

	SlinkedListRemove(begin_iterator);
}

void *QueuePeek(const queue_t *queue)
{
	slist_iterator_t begin_iterator = NULL;
	
	assert(NULL != queue);
	
	begin_iterator = SlinkedListBegin(queue -> list);

	return (SlinkedListGetData(begin_iterator));
}

size_t QueueSize(const queue_t *queue)
{
	assert(NULL != queue);

	return (SlinkedListCount(queue -> list));
}

int QueueIsEmpty(const queue_t *queue)
{
	assert(NULL != queue);

	return (0 == QueueSize(queue));
}

queue_t *QueueAppend(queue_t *dest, queue_t *src)
{
	assert(NULL != dest);
	assert(NULL != src);

	SlinkedListAppend(dest -> list, src -> list);

	return (dest);
}

static status_t CheckExpression(int expr, status_t true_t, status_t false_t)
{
	if (expr)
	{
		return (true_t);
	}
	else
	{
		return (false_t);
	}
}
