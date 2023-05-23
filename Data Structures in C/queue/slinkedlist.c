/**********************************************
*    THIS FILE CONTAINS A CUSTOM      		  *
*    IMPLEMENTATION OF SINGLY LINKED LIST     *
*    *************************	              *
*    Author: Sam                              *
*    Lab: OL - 142					          *
*    Reviewed by: Sergey Rabinovich           *
***********************************************/

#include <stdlib.h> /* malloc(), free() */
#include <assert.h> /* assert() */

#include "slinkedlist.h" /* header file */

#define FREE_MEMORY(ptr) {free(ptr); (ptr) = NULL;}
#define BAD_VALUE (9999999)


static struct node *CreateNode(void *data, void *next);
static slist_iterator_t FindDummyNode(slist_iterator_t iterator);
static int IsDummyNode(struct node *node);
static void MoveTailToNewNode(struct node *before, struct node *after);
static struct node *CopyNode(struct node *dest, const struct node *src);
static int ActionCount(void *iterator, void *counter);



list_t *SLinkedListCreate(void)
{
	list_t *new_list_ptr = NULL;
	struct node *dummy_node = NULL;
	
	size_t list_t_size = sizeof(list_t);
	
	new_list_ptr = (list_t *)malloc(list_t_size);
	if (NULL == new_list_ptr)
	{
		return (NULL);
	}
	
	dummy_node = CreateNode(new_list_ptr, NULL);
	if(NULL == dummy_node)
	{
		FREE_MEMORY(new_list_ptr);
		return (NULL);
	}

	new_list_ptr->head = dummy_node;
	new_list_ptr->tail = dummy_node;
	
	return (new_list_ptr);
}

void SLinkedListDestroy(list_t *list)
{
	struct node *cur_node = NULL;
	struct node *next_node = NULL;
	
	assert(NULL != list);
	
	cur_node = list->head;
	
	while(NULL != cur_node)
	{
		next_node = cur_node->next;
		free(cur_node);
		cur_node = next_node;
	}
	
	free(list);
	list = NULL;
}

slist_iterator_t SlinkedListInsert(slist_iterator_t iterator, void *data)
{
	struct node *new_node = NULL;

	assert(NULL != iterator);
	assert(NULL != data);

	new_node = CreateNode(iterator->data, iterator->next);
	if(NULL == new_node)
	{
		return (FindDummyNode(iterator));
	}

	if(IsDummyNode(new_node))
	{
		MoveTailToNewNode(iterator, new_node);
	}

	iterator->data = data;
	iterator->next = new_node;
	
	return (iterator);
}

slist_iterator_t SlinkedListRemove(slist_iterator_t iterator)
{
	struct node *next_node = NULL;

	assert(NULL != iterator);
	assert(NULL != iterator->next);

	next_node = iterator->next;
	
	if(IsDummyNode(next_node))
	{
		MoveTailToNewNode(next_node, iterator);
	}

	iterator = CopyNode(iterator, next_node);

	FREE_MEMORY(next_node);

	return (iterator);
}

size_t SlinkedListCount(const list_t *list)
{
	int status = 0;
	size_t elements_counter = 0;
	
	assert(NULL != list);
	
	status = 
	SlinkedListForEach(list->head, list->tail, ActionCount, &elements_counter);

	if(status)
	{
		return (BAD_VALUE);
	}
	
	return (elements_counter);
}


slist_iterator_t SLinkedListFind(const slist_iterator_t from, 
    const slist_iterator_t to, is_match_func_t is_match, void *param)
{
	slist_iterator_t cur_node = from;

	assert(NULL != to);
	assert(NULL != from);
	assert(NULL != is_match);

	while(!SlinkedListIsSameIterator(cur_node, to))
	{
		if(is_match(cur_node->data, param))							
		{
			return (cur_node);
		}
		cur_node = cur_node->next;
	}

	return (FindDummyNode(cur_node));
}


int SlinkedListForEach(const slist_iterator_t from, const slist_iterator_t to, 
                        action_func_t action, void *param)
{
	slist_iterator_t cur_node = NULL;
	int status = 0;
	
	assert(NULL != to);
	assert(NULL != from);
	assert(NULL != action);
	
	cur_node = from;
	
	while(!SlinkedListIsSameIterator(cur_node, to) && !status)
	{
		status = action(cur_node->data, param);
		cur_node = cur_node->next;
	}
	
	return (status);
}

slist_iterator_t SlinkedListBegin(const list_t *list)
{
	assert(NULL != list);

	return (list->head);
}

slist_iterator_t SlinkedListEnd(const list_t *list)
{
	assert(NULL != list);

	return (list->tail);
}

slist_iterator_t SlinkedListNext(slist_iterator_t iterator)
{
	assert(NULL != iterator);

	return (iterator->next);
}

slist_iterator_t SlinkedListSetData(slist_iterator_t iterator, void *data)
{
	assert(NULL != iterator);

	iterator->data = data;

	return (iterator);
}

void *SlinkedListGetData(slist_iterator_t iterator)
{
	assert(NULL != iterator);

	return (iterator->data);
}

int SlinkedListIsSameIterator(slist_iterator_t iterator1, 
								slist_iterator_t iterator2)
{
	assert(NULL != iterator1);
	assert(NULL != iterator2);

	return (iterator1 == iterator2);
}

void SlinkedListAppend(list_t *dest, list_t *src)
{
    assert(NULL != dest);
    assert(NULL != src);

    CopyNode(dest -> tail, src -> head);

    src -> tail -> data = dest;
    dest -> tail  = src -> tail;

    src -> head -> data = src;
    src -> head -> next = NULL;

    src -> tail = src -> head; 
}


static struct node *CreateNode(void *data, void *next)
{
	struct node *new_node = (struct node *)malloc(sizeof(struct node));
	if(NULL == new_node)
	{
		return (NULL);
	}

	new_node->data = data;
	new_node->next = next;

	return (new_node);
}

static slist_iterator_t FindDummyNode(slist_iterator_t iterator)
{
	assert(NULL != iterator);

	while(NULL != iterator->next)
	{
		iterator = iterator->next;
	}

	return (iterator);
}

static int IsDummyNode(struct node *node)
{
	assert(NULL != node);

	if(NULL == node->next)
	{
		return (1);
	}

	return (0);
}

static void MoveTailToNewNode(struct node *before, struct node *after)
{
	list_t *list_ptr = NULL;

	assert(NULL != before);
	assert(NULL != after);

	list_ptr = before->data;
	list_ptr->tail = after;
}

static struct node *CopyNode(struct node *dest, const struct node *src)
{
	assert(NULL != dest);
	assert(NULL != src);

	dest->data = src->data;
	dest->next = src->next;

	return (dest);
}

static int ActionCount(void *iterator, void *counter)
{
	assert(NULL != iterator);
	assert(NULL != counter);

	if (NULL != iterator)
	{
		*(size_t*)counter += 1;
	}

	return (0);
}
