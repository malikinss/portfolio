/* 
	Header file, contains declarations: type queue_t and QueueCreate(),
	QueueDestroy(), QueueEnqueue(), QueueDequeue(), QueuePeek(), QueueIsEmpty(),
	QueueSize(), QueueAppend() functions.
	Function definitions in the queue.c file. 
	Created by Sam 
	Reviewed by 	
*/
#ifndef __QUEUE_H_ILRD__
#define __QUEUE_H_ILRD__

#include <stddef.h> /* size_t */

typedef struct queue queue_t;

/*
DESCRIPTION
    A function that creates a new queue. Memory will be allocated.
    In case of allocation failure, function will return NULL.
    User is responsible for destroying queues.
RETURN
    queue_t * - pointer to a new queue
    NULL - if allocation failed
INPUT
    No input for this function.
*/
queue_t *QueueCreate(void); /* O(1) */

/*
DESCRIPTION
    Destroys the queue by freeing all the allocated memory.
    All remaining data will be lost. 
    The user is responsible for handling dangling pointers.
RETURN
    There is no return for this function.
INPUT
    queue: a pointer to the queue.
*/
void QueueDestroy(queue_t *queue); /* O(n) */

/*
DESCRIPTION
    A function create a new queue element, 
    Insert an element at the end of the queue. 
RETURN
    0 - on success
    1 - if allocation fails
INPUT
    queue: a pointer to the queue.
    data: a ponter to a data.
*/
int QueueEnqueue(queue_t *queue,  void *data); /* O(1) */  

/*
DESCRIPTION
    Remove the first element of the queue,
    if the queue is not empty.
    Dequeueing on the empty queue may cause undefined behavior.
RETURN
    There is no return for this function.
INPUT
    queue: a pointer to the queue.
*/
void QueueDequeue(queue_t *queue); /* O(1) */

/*
DESCRIPTION
    Returns the pointer to the First Out element of the queue. 
    Peeking at the empty queue may cause undefined behavior.
RETURN
    pointer to the element.
INPUT
    queue: a pointer to the queue
*/

void *QueuePeek(const queue_t *queue); /* O(1) */

/*
DESCRIPTION
    Checks whether the queue is empty.
RETURN
    1 - if the queue is empty.
	0 - if the queue is not empty.
INPUT
    queue: a pointer to the queue
*/
int QueueIsEmpty(const queue_t *queue); /* O(1) */

/*
DESCRIPTION
    Returns the number of elements currently in the queue.
RETURN
    Number of elements
INPUT
    queue: a pointer to the queue
*/
size_t QueueSize(const queue_t *queue); /* O(n) */ 

/*
DESCRIPTION
    Adds queue src to the end of the queue dest. The last element 
    of the src becomes the last element of the appended queue.
    The src becomes empty after the appendage.
RETURN
    A pointer to the appended queue
INPUT
    dest: a pointer to the destination queue
    src: a pointer to the source queue
*/
queue_t *QueueAppend(queue_t *dest, queue_t *src); /* O(1) */


#endif /* __QUEUE_H_ILRD__ */

