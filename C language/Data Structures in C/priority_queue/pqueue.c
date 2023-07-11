/*
*****************************************
* Title : PQ function implementation	*
* Author: Sam Malikin					*
* Reviewer: Sergey						*
* Date : 07.05.2023						*
*****************************************
*/

#include <stdlib.h> /* malloc, free */
#include <assert.h> /* assert */

#include "pqueue.h"

#define PQ_T_SIZE (sizeof(pq_t))
#define FREE_MEMORY(ptr) {free(ptr); (ptr) = NULL;}

typedef enum status {SUCCESS, FAIL} status_t;

struct pq
{
	sorted_list_t *sorted_list;
};


pq_t *PQCreate(pqueue_compare_func_t compare)
{
	pq_t *pqueue = NULL;
	sorted_list_t *new_sorted_list = NULL;
	
	assert(NULL != compare);
	
	pqueue = (pq_t *)malloc(PQ_T_SIZE);
	
	if (NULL == pqueue)
	{
		return (NULL);
	}
	
	new_sorted_list = SortedListCreate(compare);
	
	if (NULL == new_sorted_list)
	{
		FREE_MEMORY(pqueue);
		return (NULL);
	}
	
	pqueue->sorted_list = new_sorted_list;

	return (pqueue); 
}


void PQDestroy(pq_t *pqueue)
{
	sorted_list_t *sorted_list_to_destroy = NULL;
	
	assert(NULL != pqueue);
	assert(NULL != pqueue->sorted_list);

	sorted_list_to_destroy = pqueue->sorted_list;

	SortedListDestroy(sorted_list_to_destroy);
	pqueue->sorted_list = NULL;

	FREE_MEMORY(pqueue);
}


int PQEnqueue(pq_t *pqueue, void *data)
{
	sorted_list_iterator_t enqueued_elem;
	sorted_list_iterator_t list_end;
	sorted_list_t *sorted_list_to_insert = NULL;

	assert(NULL != pqueue);
	assert(NULL != pqueue->sorted_list);

	sorted_list_to_insert = pqueue->sorted_list;
	enqueued_elem = SortedListInsert(sorted_list_to_insert, data);
	list_end = SortedListEnd(sorted_list_to_insert);

	if(SortedListIsSameIterator(enqueued_elem, list_end))
	{
		return(FAIL);
	}

	return(SUCCESS);
}



void *PQDequeue(pq_t *pqueue)
{
	sorted_list_t *sorted_list = NULL;
	
	assert(NULL != pqueue);
	assert(NULL != pqueue->sorted_list);

	sorted_list = pqueue->sorted_list;
	
	return (SortedListPopBack(sorted_list));
}

void *PQPeek(const pq_t *pqueue)
{
	sorted_list_iterator_t last_element; 

	assert(NULL != pqueue);
	assert(NULL != pqueue->sorted_list);

	last_element = SortedListPrev(SortedListEnd(pqueue->sorted_list));

	return (SortedListGetData(last_element));
}


int PQIsEmpty(const pq_t *pqueue)
{
	sorted_list_t *list_to_check = NULL;
	
	assert(NULL != pqueue);
	assert(NULL != pqueue->sorted_list);

	list_to_check = pqueue->sorted_list;
	
	return (SortedListIsEmpty(list_to_check));
}


size_t PQSize(const pq_t *pqueue)
{
	sorted_list_t *list_to_check = NULL;
	
	assert(NULL != pqueue);
	assert(NULL != pqueue->sorted_list);
	
	list_to_check = pqueue->sorted_list;

	return (SortedListSize(list_to_check));
}


void PQClear(pq_t *pqueue)
{	
	sorted_list_t *list_to_check = NULL;
	
	assert(NULL != pqueue);

	list_to_check = pqueue->sorted_list;
	
	while(!SortedListIsEmpty(list_to_check))
	{	
		SortedListRemove(SortedListBegin(list_to_check));
		list_to_check = pqueue->sorted_list;
	}
}


void *PQErase(pq_t *pqueue, pqueue_is_match_func_t is_match, void *param)
{
	sorted_list_t *list_to_operations = NULL;
	sorted_list_iterator_t element_to_erase;
	sorted_list_iterator_t from;
	sorted_list_iterator_t to;
	sorted_list_iterator_t end;
	void *data = NULL; 

	assert(NULL != pqueue);
	assert(NULL != pqueue->sorted_list);
	assert(NULL != is_match);

	list_to_operations = pqueue->sorted_list;
	from = SortedListBegin(list_to_operations);
	to = SortedListEnd(list_to_operations);
	end = to;

	element_to_erase = SortedListFindIf(from, to, is_match, param);

	if (SortedListIsSameIterator(element_to_erase, end))
    {
        return (NULL);
    }

    data = SortedListGetData(element_to_erase);

    SortedListRemove(element_to_erase);

    return (data);
}
