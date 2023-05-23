/*
*****************************************
* Title : PQ function declarations		*
* Author: Sam Malikin					*
* Reviewer: Sergey						*
* Date : 07.05.2023						*
*****************************************
*/
#ifndef __PQUEUE_H_ILRD__
#define __PQUEUE_H_ILRD__

#include "sorted_list.h"

typedef struct pq pq_t;

/*
DESCRIPTION
    A pointer to a function that compares two data values.
    The method of comparison and types of the input are defined by the user.
RETURN
    1  - if value of data1 is grater than the value of data2
    -1 - if value of data2 is grater than the value of data1
    0  - if the values are equal
INPUT
    data1: a pointer to some value;
    data2: a pointer to some value. 
*/
typedef int (*pqueue_compare_func_t)(const void *data1, const void *data2);

/*
DESCRIPTION
    A pointer to a function that validates if the data matches a certain 
    criteria using the param.
    The actual matching and types of the input are defined by the user.
RETURN
    1 - if the criteria is matched.
    0 - if it's not
INPUT
    data1: a pointer to some value;
    data2: a pointer to data used as a matching parameter.  
*/
typedef int (*pqueue_is_match_func_t)(const void *data, const void *param);

/*
DESCRIPTION
    Creates a pqueue and allocates memory.
    Memory allocation may fail. 
    User is responsible for destroying created lists.
RETURN
    A pointer to the created pqueue - on success.
    NULL - on failure.
INPUT
    compare: a pointer to the compare function used for prioritizing the queue.
*/
pq_t *PQCreate(pqueue_compare_func_t compare); /* O(1) */

/*
DESCRIPTION
    Frees the memory allocated for the pqueue and each of its elements.
RETURN
    There is no return to this function.
INPUT
    pqueue: a pointer to a pqueue.
*/
void PQDestroy(pq_t *pqueue); /* O(n) */

/* adds an element according to the user's prioroty, can fail 
WHAT DOES IT RETURN? */
/*
DESCRIPTION
	Inserts an element with the provided data.
	The insertion place will depend on the priority, which in turn
	will depend on the value of data.
RETURN
    1 - in case of memory allocation failure.
    0 - on success.
INPUT
    pqueue: a pointer to a pqueue.
    data: a pointer to data.
*/
int PQEnqueue(pq_t *pqueue, void *data); /* O(n) */

/*
DESCRIPTION
    Removes the highest priority element and returns the data of the removed element. 
    Trying to dequeue from an empty list may cause undefined behaviour.
RETURN
    An pointer to data from the removed element. 
INPUT
    pqueue: a pointer to a pqueue.
*/
void *PQDequeue(pq_t *pqueue); /* O(1) */

/* returns pointer to data in the highest priority element */
/*
DESCRIPTION
    Returns the pointer to the data of the highest priority element of the pqueue. 
    Peeking at an empty pqueue may cause undefined behavior.
RETURN
    pointer to the data.
INPUT
    pqueue: a pointer to the pqueue
*/
void *PQPeek(const pq_t *pqueue); /* O(1) */

/*
DESCRIPTION
    Checks whether a pqueue is empty.
RETURN
    1 - if the pqueue is empty.
    0 - if it's not empty.
INPUT
    pqueue: a pointer to the pqueue
*/
int PQIsEmpty(const pq_t *pqueue); /* O(1) */

/*
DESCRIPTION
    Traverses the pqueue and returns the number of its elements.
RETURN
    The number of elements currently in the pqueue. 
INPUT
    pqueue: a pointer to a pqueue.
*/
size_t PQSize(const pq_t *pqueue); /* O(n) */

/*
DESCRIPTION
	Removes all elements of the pqueue.
RETURN
	There is no return to this function.
INPUT
    pqueue: a pointer to a pqueue.
*/
void PQClear(pq_t *pqueue); /* O(n) */

/*
DESCRIPTION
	Removes an element that matches a certain cretaria, using the is_match function
	and the param. 
RETURN
	Returns the data of the removed element on success.
	Returns NULL and doesn't remove anything if an element matching the creteria
	has not been find. (Note: if NULL is returned, please check if the size has changed).
INPUT
    pqueue: a pointer to a pqueue.
*/
void *PQErase(pq_t *pqueue, pqueue_is_match_func_t is_match, void *param);

#endif  /* __PQUEUE_H_ILRD__ */ 

