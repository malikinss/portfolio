/*
*****************************************	
* Title : sorted_list implementation	*
* Author: Sam Malikin			*
* Reviewer: ...				*
* Date : 24.04.2023			*
*****************************************	
*/
#include <stdlib.h> /* malloc(), free() */
#include <assert.h> /* assert() */

#include "sorted_list.h"

#define FREE_MEMORY(ptr) {free(ptr); (ptr) = NULL;}
#define DUMMY_TAIL(iterator) (SortedListEnd(iterator.parent_list))
#define FIRST_ELEMENT(iterator) (SortedListBegin(iterator.parent_list))
#define FIND_FIRST (0)
#define FIND_LAST (1)


static dlist_iterator_t SortedListToDListIter(sorted_list_iterator_t iterator);
static sorted_list_iterator_t DListToSortedListIter(dlist_iterator_t iterator,
                                            const sorted_list_t *sorted_list);
static sorted_list_iterator_t UpdateIterator(sorted_list_iterator_t iterator,
                                        dlist_iterator_t new_dlist_iterator);
static dlist_iterator_t FindForInsert(int condition,
                                        sorted_list_t *sorted_list,
                                        dlist_iterator_t from,
                                        void *data);
static int FindFirst(const void *data, void *param);
static int FindLast(const void *data, void *param);
static int FindMatch(const void *data, void *param);


struct sorted_list
{
    dlist_t *dlist;
    sorted_list_compare_func_t compare;
};

struct compare_wrapper
{
    sorted_list_compare_func_t compare;
    void *data;
};



sorted_list_t *SortedListCreate(sorted_list_compare_func_t comp)
{
    sorted_list_t *sorted_list = NULL;
    dlist_t *new_dlist = NULL;

    assert(NULL != comp);

    sorted_list = (sorted_list_t *)malloc(sizeof(sorted_list_t));
    if(NULL == sorted_list)
    {
        return (NULL);
    }

    new_dlist = DListCreate();
    if(NULL == new_dlist)
    {
        FREE_MEMORY(sorted_list);
        
        return (NULL);
    }

    sorted_list->dlist = new_dlist;
    sorted_list->compare = comp;

    return (sorted_list);
}


void SortedListDestroy(sorted_list_t *sorted_list)
{
    assert(NULL != sorted_list);
	assert(NULL != sorted_list->dlist);	
	
    DListDestroy(sorted_list->dlist);
    sorted_list->dlist = NULL;

    FREE_MEMORY(sorted_list);
}


size_t SortedListSize(const sorted_list_t *sorted_list)
{
    assert(NULL != sorted_list);
    assert(NULL != sorted_list->dlist);

    return (DListSize(sorted_list->dlist));
}


int SortedListIsEmpty(const sorted_list_t *sorted_list)
{
    assert(NULL != sorted_list);
    assert(NULL != sorted_list->dlist);

    return (DListIsEmpty(sorted_list->dlist));
}


sorted_list_iterator_t SortedListBegin(const sorted_list_t *sorted_list)
{
    dlist_iterator_t dlist_iterator = NULL;
    sorted_list_iterator_t result = {0};

    assert(NULL != sorted_list);
    assert(NULL != sorted_list->dlist);

    dlist_iterator = DListBegin(sorted_list->dlist);

    result = DListToSortedListIter(dlist_iterator, sorted_list);

    return(result);
}


sorted_list_iterator_t SortedListEnd(const sorted_list_t *sorted_list)
{
    dlist_iterator_t dlist_iterator = NULL;
    sorted_list_iterator_t result = {0};

    assert(NULL != sorted_list);
    assert(NULL != sorted_list->dlist);

    dlist_iterator = DListEnd(sorted_list->dlist);

    result = DListToSortedListIter(dlist_iterator, sorted_list);

    return(result);
}


sorted_list_iterator_t SortedListNext(sorted_list_iterator_t iterator)
{
	dlist_iterator_t dlist_iterator = NULL;

    assert(NULL != iterator.internal_iter);    
    assert(NULL != iterator.parent_list);    
    assert(!DListIsSameIterator(SortedListToDListIter(DUMMY_TAIL(iterator)),
                                SortedListToDListIter(iterator)));


	dlist_iterator = SortedListToDListIter(iterator);
    dlist_iterator = DListNext(dlist_iterator);

    iterator = UpdateIterator(iterator, dlist_iterator);

    return (iterator);

}


sorted_list_iterator_t SortedListPrev(sorted_list_iterator_t iterator)
{
    dlist_iterator_t dlist_iterator = NULL;

    assert(NULL != iterator.internal_iter);
    assert(NULL != iterator.parent_list);
    assert(!DListIsSameIterator(SortedListToDListIter(FIRST_ELEMENT(iterator)),
                                SortedListToDListIter(iterator)));

    dlist_iterator = SortedListToDListIter(iterator);
    dlist_iterator = DListPrev(dlist_iterator);

    iterator = UpdateIterator(iterator, dlist_iterator);

    return (iterator);
}


int SortedListIsSameIterator(sorted_list_iterator_t iterator1, 
                             sorted_list_iterator_t iterator2)
{
    dlist_iterator_t dlist_iterator1 = NULL;
    dlist_iterator_t dlist_iterator2 = NULL;
    int result = 0;
    
    assert(NULL != iterator1.internal_iter);
    assert(NULL != iterator2.internal_iter);
    assert(NULL != iterator1.parent_list);
    assert(NULL != iterator2.parent_list);

    dlist_iterator1 = SortedListToDListIter(iterator1);
    dlist_iterator2 = SortedListToDListIter(iterator2);

    result = DListIsSameIterator(dlist_iterator1, dlist_iterator2);

    return (result); 
}

void *SortedListGetData(sorted_list_iterator_t iterator)
{
    dlist_iterator_t dlist_iterator = NULL;
    void *result = NULL;

    assert(NULL != iterator.internal_iter);
    assert(NULL != iterator.parent_list);
    assert(!SortedListIsSameIterator(DUMMY_TAIL(iterator), iterator));

    dlist_iterator = SortedListToDListIter(iterator);

    result = DListGetData(dlist_iterator);

    return (result);
}


void *SortedListPopBack(sorted_list_t *sorted_list)
{
    void *result = NULL;

    assert(NULL != sorted_list);
    assert(NULL != sorted_list->dlist);

    result = DListPopBack(sorted_list->dlist);

    return (result);
}                  

void *SortedListPopFront(sorted_list_t *sorted_list)
{
    void *result = NULL;

    assert(NULL != sorted_list);
    assert(NULL != sorted_list->dlist);
    
    result = DListPopFront(sorted_list->dlist);

    return (result);
}

int SortedListForEach(sorted_list_iterator_t from,
                        sorted_list_iterator_t to,
                        sorted_list_action_func_t action,
                        void *param)
{
    int result = 0;
    dlist_iterator_t dlist_from = NULL;
    dlist_iterator_t dlist_to = NULL;

    assert(NULL != from.internal_iter);
    assert(NULL != from.parent_list);
    assert(NULL != to.internal_iter);
    assert(NULL != to.parent_list);
    assert(NULL != action);
    assert(from.parent_list == to.parent_list);

    dlist_from = SortedListToDListIter(from);    
    dlist_to = SortedListToDListIter(to);

    result = DListForEach(dlist_from, dlist_to, action, param);

    return (result);
}


sorted_list_iterator_t SortedListFind(sorted_list_t *sorted_list,
                                        sorted_list_iterator_t from,
                                        sorted_list_iterator_t to,
                                        void *data)
{
    struct compare_wrapper wrapper = {0};
    dlist_iterator_t dlist_from = NULL;
    dlist_iterator_t dlist_to = NULL;

    assert(NULL != sorted_list);
    assert(NULL != sorted_list->compare);
    assert(NULL != from.internal_iter);
    assert(NULL != from.parent_list);
    assert(NULL != to.internal_iter);
    assert(NULL != to.parent_list);
    assert(from.parent_list == to.parent_list);

    dlist_from = SortedListToDListIter(from);    
    dlist_to = SortedListToDListIter(to);

    wrapper.compare = sorted_list->compare;
    wrapper.data = data;
    
    dlist_from = DListFind(dlist_from, dlist_to, FindMatch, &wrapper);

    from = UpdateIterator(from, dlist_from);

    return (from);
}


sorted_list_iterator_t SortedListInsert(sorted_list_t *sorted_list, void *data)
{
	dlist_iterator_t runner = NULL;

    assert(NULL != sorted_list);
    assert(NULL != sorted_list -> dlist);

    runner = DListBegin(sorted_list -> dlist);
    runner = FindForInsert(FIND_FIRST, sorted_list, runner, data);

    runner = DListInsert(runner, data);

    return (DListToSortedListIter(runner, sorted_list));
}


sorted_list_iterator_t SortedListRemove(sorted_list_iterator_t iterator)
{
    dlist_iterator_t dlist_iterator = NULL;

    assert(NULL != iterator.internal_iter);
    assert(NULL != iterator.parent_list);
    assert(!DListIsSameIterator(SortedListToDListIter(DUMMY_TAIL(iterator)),
                                SortedListToDListIter(iterator)));

    dlist_iterator = SortedListToDListIter(iterator);
    dlist_iterator = DListRemove(dlist_iterator);

    iterator = UpdateIterator(iterator, dlist_iterator);

    return (iterator);
}


sorted_list_iterator_t SortedListFindIf(sorted_list_iterator_t from, 
                                        sorted_list_iterator_t to,
                                        sorted_list_is_match_func_t is_match,
                                        void *param)
{
    dlist_iterator_t dlist_from = NULL;
    dlist_iterator_t dlist_to = NULL;

    assert(NULL != from.internal_iter);
    assert(NULL != from.parent_list);
    assert(NULL != to.internal_iter);
    assert(NULL != to.parent_list);
    assert(from.parent_list == to.parent_list);

    dlist_from = SortedListToDListIter(from);    
    dlist_to = SortedListToDListIter(to);

    dlist_from = DListFind(dlist_from, dlist_to,
                            (dlist_is_match_func_t)is_match, param);

    from = UpdateIterator(from, dlist_from);

    return (from);
}


sorted_list_t *SortedListMerge(sorted_list_t *sorted_list1,
                                sorted_list_t *sorted_list2)
{
    dlist_iterator_t list1_end = NULL;
    dlist_iterator_t list2_end = NULL;
    dlist_iterator_t where = NULL;
    dlist_iterator_t to = NULL;

    assert(NULL != sorted_list1);
    assert(NULL != sorted_list1->dlist);
    assert(NULL != sorted_list1->compare);
    assert(NULL != sorted_list2);
    assert(NULL != sorted_list2->dlist);
    assert(NULL != sorted_list2->compare);
    assert(sorted_list1 != sorted_list2);

    list1_end = DListEnd(sorted_list1->dlist);
    list2_end = DListEnd(sorted_list2->dlist);
    where = DListBegin(sorted_list1->dlist);
    to = DListBegin(sorted_list2->dlist);

    while(!DListIsSameIterator(to, list2_end))
    {
        dlist_iterator_t from = to;

        void *data = DListGetData(from);
        where = FindForInsert(FIND_FIRST, sorted_list1, where, data);

        if(!DListIsSameIterator(where, list1_end))
        {
            void *data = DListGetData(where);
            to = FindForInsert(FIND_LAST, sorted_list2, to, data);
        }
        else
        {
            to = list2_end;
        }

        DListSplice(where, from, to);
    }

    return (sorted_list1);
}


static sorted_list_iterator_t DListToSortedListIter(dlist_iterator_t iterator,
                                            const sorted_list_t *sorted_list)
{
    sorted_list_iterator_t result = {0};

    assert(NULL != iterator);
    assert(NULL != sorted_list);

    result.internal_iter = iterator;

    #ifndef NDEBUG
    result.parent_list = (sorted_list_t *)sorted_list;
    #endif

    return (result);
    (void)sorted_list;
}


static dlist_iterator_t SortedListToDListIter(sorted_list_iterator_t iterator)
{
    assert(NULL != iterator.internal_iter);
    assert(NULL != iterator.parent_list);

    return (iterator.internal_iter);
}


static sorted_list_iterator_t UpdateIterator(sorted_list_iterator_t iterator,
                                        dlist_iterator_t new_dlist_iterator)
{
    assert(NULL != iterator.internal_iter);
    assert(NULL != iterator.parent_list);
    assert(NULL != new_dlist_iterator);

    iterator.internal_iter = new_dlist_iterator;

    return (iterator);
}

static dlist_iterator_t FindForInsert(int condition,
                                        sorted_list_t *sorted_list,
                                        dlist_iterator_t from,
                                        void *data)
{
    dlist_iterator_t end = NULL;
    struct compare_wrapper wrapper = {0};
    dlist_is_match_func_t compare_func = NULL;

    assert(NULL != sorted_list);
    assert(NULL != sorted_list->dlist);
    assert(NULL != sorted_list->compare);
    assert(NULL != from);

    switch(condition)
    {
        case FIND_FIRST:
            compare_func = FindFirst;
            break;
        case FIND_LAST:
            compare_func = FindLast;
            break;
        default:
            break;
    }

    end = DListEnd(sorted_list->dlist);
    wrapper.compare = sorted_list->compare;
    wrapper.data = data;
    
    from = DListFind(from, end, compare_func, &wrapper);

    return (from);
}

static int FindFirst(const void *data, void *param)
{
    struct compare_wrapper *wrapper = param;

    assert(NULL != param);

    return (0 <= wrapper->compare(data, wrapper->data));
}

static int FindLast(const void *data, void *param)
{
    struct compare_wrapper *wrapper = param;

    assert(NULL != param);

    return (0 < wrapper->compare(data, wrapper->data));
}

static int FindMatch(const void *data, void *param)
{
    struct compare_wrapper *wrapper = param;

    assert(NULL != param);

    return (0 == wrapper->compare(data, wrapper->data));
}
