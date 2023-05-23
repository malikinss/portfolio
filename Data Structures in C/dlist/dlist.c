/*
*****************************************	
* Title : dlist implementation	*
* Author: Sam Malikin					*
* Reviewer: ...						    *
* Date : 22.04.2023						*
*****************************************	
*/
#include <stdlib.h> /* malloc(), free() */
#include <assert.h> /* assert() */

#include "dlist.h"

#define SUCCESS (0)
#define FOUND (1)
#define BAD_VALUE (9999999)

#define FREE_MEMORY(ptr) \
{free(ptr); (ptr) = NULL;}



typedef struct dlist_node dlist_node_t;

struct dlist_node
{
    void *data;
    struct dlist_node *next;
    struct dlist_node *prev;
};

struct dlist
{
    struct dlist_node head;
    struct dlist_node tail;
};

static dlist_iterator_t GetLastNode(dlist_iterator_t iterator);
static int CountNodes(void *dummy, void *counter);

static void SetNextPrevNode(dlist_node_t *node, dlist_node_t *node_to_set);

static void SetPrevNextLinks(dlist_node_t *node, dlist_node_t *node_to_set);
static void SetPrevNextNode(dlist_node_t *node, dlist_node_t *node_to_set);
static void SetPrevNode(dlist_node_t *node, dlist_node_t *node_to_set);

static dlist_iterator_t CreateNode(void *data, dlist_iterator_t next,
 												dlist_iterator_t prev);							 
static void NodeInit(void *data, dlist_node_t *node,  
								 dlist_node_t *next,
								 dlist_node_t *prev);
								 
								 
dlist_t *DListCreate(void)
{
    size_t dlist_size = sizeof(struct dlist);
    
    dlist_t *new_dlist = (dlist_t *)malloc(dlist_size);
    if (NULL == new_dlist)
    {
        return (NULL);
    }
    
    NodeInit(NULL, &(new_dlist->head), &(new_dlist->tail), NULL);
	NodeInit(NULL, &(new_dlist->tail), NULL, &(new_dlist->head));      
    
    return (new_dlist);
}


void DListDestroy(dlist_t *dlist)
{
	dlist_iterator_t end = NULL;
	dlist_iterator_t current_iterator = NULL;
	dlist_iterator_t next_iterator = NULL;
	
	assert(NULL != dlist);

	end = DListEnd(dlist);
	current_iterator = DListBegin(dlist);
	
	while(!DListIsSameIterator(end, current_iterator))
	{
		next_iterator = DListNext(current_iterator);

		free(current_iterator);
		current_iterator = next_iterator;
	}

	free(dlist);
	dlist = NULL;
}


int DListIsEmpty(const dlist_t *dlist)
{
    assert(NULL != dlist);
        
    return (dlist->head.next == &(dlist->tail));
}


dlist_iterator_t DListBegin(const dlist_t *dlist)
{
	assert(NULL != dlist);
        
    return ((dlist_iterator_t)(dlist->head.next));
}


dlist_iterator_t DListEnd(const dlist_t *dlist)
{
	assert(NULL != dlist);
	
	return((dlist_iterator_t)&(dlist->tail));
}


dlist_iterator_t DListNext(dlist_iterator_t iterator)
{
	assert(NULL != iterator);
	
	return((dlist_iterator_t)(iterator->next));
}


dlist_iterator_t DListPrev(dlist_iterator_t iterator)
{
	assert(NULL != iterator);
	
	return((dlist_iterator_t)(iterator->prev));
}


int DListIsSameIterator(dlist_iterator_t iterator1, 
						dlist_iterator_t iterator2)
{
	assert(NULL != iterator1);
	assert(NULL != iterator2);
	
	return(iterator1 == iterator2);
}


void *DListGetData(dlist_iterator_t iterator)
{
	assert(NULL != iterator);
	
	return(iterator->data);
}


void DListSetData(dlist_iterator_t iterator, void *data)
{
	assert(NULL != iterator);
	
	iterator->data = data;
}


dlist_iterator_t DListInsert(dlist_iterator_t iterator, void *data)
{
	struct dlist_node *new_node = NULL;
    struct dlist_node *prev_node = NULL;
	
	assert(NULL != iterator);
	assert(NULL != DListPrev(iterator));
	
	prev_node = DListPrev(iterator);
	
	new_node = CreateNode(data, iterator, prev_node);
	if (NULL == new_node)
    {
        return (GetLastNode(iterator));
    }

	SetPrevNextLinks(iterator, new_node);
	
    return (new_node);
}


dlist_iterator_t DListRemove(dlist_iterator_t iterator)
{
	struct dlist_node *prev_node = NULL;
	struct dlist_node *next_node = NULL;
	
	assert(NULL != iterator);
	
	prev_node = DListPrev(iterator);
	next_node = DListNext(iterator);
	
	SetNextPrevNode(iterator, prev_node);
	SetPrevNextNode(iterator, next_node);
	
	prev_node->next = next_node;
	next_node->prev = prev_node;

    FREE_MEMORY(iterator)
    
    return (next_node);
}


int DListForEach(dlist_iterator_t from, dlist_iterator_t to, 
                               dlist_action_func_t action, void *param)
{
    dlist_iterator_t runner = from;
    int status = SUCCESS;

    assert(NULL != from);
    assert(NULL != to);
    assert(NULL != action);
    
    while (!DListIsSameIterator(runner, to) && !status)
    {
        status = action(DListGetData(runner), param);
        if(SUCCESS != status)
		{
			return (status);
		}
        runner = DListNext(runner);
    }
    
    return (status);    
}


size_t DListSize(const dlist_t *dlist)
{
    dlist_iterator_t from = NULL;
	dlist_iterator_t to = NULL;
    size_t counter = 0;
    
    from = DListBegin(dlist);
    to = DListEnd(dlist);
    
    assert(NULL != dlist);
    
    DListForEach(from, to, CountNodes, &counter);
	
    return (counter);
}


dlist_iterator_t DListPushBack(dlist_t *dlist, void *data)
{
	assert(NULL != dlist);
	
	return (DListInsert(DListEnd(dlist), data));
}


dlist_iterator_t DListPushFront(dlist_t *dlist, void *data)
{
	assert(NULL != dlist);
	
	return (DListInsert(DListBegin(dlist), data));
}


void *DListPopBack(dlist_t *dlist)
{
	dlist_iterator_t last_element = NULL;
	void *data = NULL;

	assert(NULL != dlist);
	assert(!DListIsEmpty(dlist));

	last_element = DListEnd(dlist);
	last_element = DListPrev(last_element);
	data = DListGetData(last_element);
	DListRemove(last_element);

	return (data);
}


void *DListPopFront(dlist_t *dlist)
{
	dlist_iterator_t first_element = NULL;
	void *data = NULL;

	assert(NULL != dlist);
	assert(!DListIsEmpty(dlist));

	first_element = DListBegin(dlist);
	data = DListGetData(first_element);
	DListRemove(first_element);

	return (data);
}



dlist_iterator_t DListFind(dlist_iterator_t from, dlist_iterator_t to,
    				dlist_is_match_func_t is_match, void *param)
{
	dlist_iterator_t runner = NULL;
	
	assert(NULL != from);
    assert(NULL != to);
    assert(NULL != is_match);

	runner = from;
    
    while (!DListIsSameIterator(runner, to))
    {
        if (FOUND == is_match(DListGetData(runner), param))
        {
            return (runner);
        }
        runner = DListNext(runner);
    }
    
    return (runner);
}

int DListMultiFind(dlist_iterator_t from, dlist_iterator_t to,
            dlist_t *output_list, dlist_is_match_func_t is_match, void *param)
{
	dlist_iterator_t runner = NULL;
    int find_count = 0;
    void *find_data = NULL;
	
	assert(NULL != from);
    assert(NULL != to);
    assert(NULL != is_match);
	
	runner = DListFind(from, to, is_match, param);
    
    while (!DListIsSameIterator(runner, to))
    {
        ++find_count;
        find_data = DListGetData(runner);
        DListPushBack(output_list, find_data);
        from = DListNext(runner);
        runner = DListFind(from, to, is_match, param);
    }
    
    return (find_count);
}

dlist_iterator_t DListSplice(dlist_iterator_t where,
							 dlist_iterator_t from,
							 dlist_iterator_t end)
{
	dlist_iterator_t tmp_for_prev_of_end = NULL;

	assert(NULL != where);
	assert(NULL != from);
	assert(NULL != end);

	SetPrevNextNode(from, end);
	SetPrevNextNode(where, from);
	SetPrevNextNode(end, where);

	tmp_for_prev_of_end = DListPrev(end);

	SetPrevNode(end, DListPrev(from));
	SetPrevNode(from, DListPrev(where));
	SetPrevNode(where, tmp_for_prev_of_end);

	return (from);
}

static dlist_iterator_t CreateNode(void *data, dlist_iterator_t next, 
												dlist_iterator_t prev)
{
    dlist_iterator_t new_node = NULL;
    
    assert(NULL != next);
    assert(NULL != prev);

    new_node = (dlist_iterator_t)malloc(sizeof(struct dlist_node));
    
    if(NULL == new_node)
    {
        return (NULL);
    }

    new_node->data = data;
    new_node->next = next;
    new_node->prev = prev;

    return (new_node);
}

static dlist_iterator_t GetLastNode(dlist_iterator_t iterator)
{
	assert(NULL != iterator);

	while(NULL != iterator->next)
	{
		iterator = iterator->next;
	}

	return (iterator);
}

static int CountNodes(void *dummy, void *counter)
{
	assert(NULL != counter);

	*(size_t *)counter += 1;

	return (0);
	(void)dummy;
}

static void NodeInit(void *data, dlist_node_t *node,  
								 dlist_node_t *next,
								 dlist_node_t *prev)
{
	assert(NULL != node);

	node -> data = data;
    node -> next = next;
    node -> prev = prev;
}

static void SetPrevNextNode(dlist_node_t *node, dlist_node_t *node_to_set)
{
	node -> prev -> next = node_to_set;
}

static void SetPrevNode(dlist_node_t *node, dlist_node_t *node_to_set)
{
	node -> prev = node_to_set;
}

static void SetPrevNextLinks(dlist_node_t *node, dlist_node_t *node_to_set)
{
	SetPrevNextNode(node, node_to_set);
	SetPrevNode(node, node_to_set);
}

static void SetNextPrevNode(dlist_node_t *node, dlist_node_t *node_to_set)
{
	node -> next -> prev = node_to_set;
}

