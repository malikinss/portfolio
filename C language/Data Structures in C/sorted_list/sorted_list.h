/*
*************************************	
* Title : sorted_list header file	*
* Author: Sam Malikin				*
* Reviewer: ...						*
* Date : 24.04.2023					*
*************************************	
*/
#ifndef __SORTED_LIST_H_ILRD__
#define __SORTED_LIST_H_ILRD__

#include <stddef.h> /* size_t */
#include "dlist.h" /* dlist */

typedef struct sorted_list sorted_list_t;
typedef struct sorted_list_iter sorted_list_iterator_t;

/*
return:
1 - data1 larger than data2
-1 - data1 smaller than data2
0 - they are equal
*/
typedef int (*sorted_list_compare_func_t) (const void* data1, const void *data2); 

typedef int (*sorted_list_action_func_t)(void *data, void *param);

typedef int (*sorted_list_is_match_func_t)(const void *data1, const void *data2);

struct sorted_list_iter
{
    dlist_iterator_t internal_iter;
    
    #ifndef NDEBUG
    sorted_list_t *parent_list;
    #endif
};

sorted_list_t *SortedListCreate(sorted_list_compare_func_t comp); 
/* O(1) */


void SortedListDestroy(sorted_list_t *sorted_list); 
/* O(n) */


size_t SortedListSize(const sorted_list_t *sorted_list); 
/* O(n) */


int SortedListIsEmpty(const sorted_list_t *sorted_list); 
/* O(1) */


sorted_list_iterator_t SortedListBegin(const sorted_list_t *sorted_list); 
/* O(1) */


sorted_list_iterator_t SortedListEnd(const sorted_list_t *sorted_list); 
/* O(1) */


sorted_list_iterator_t SortedListNext(sorted_list_iterator_t iterator); 
/* O(1) */


sorted_list_iterator_t SortedListPrev(sorted_list_iterator_t iterator); 
/* O(1) */


int SortedListIsSameIterator(sorted_list_iterator_t iterator1, 
							 sorted_list_iterator_t iterator2); 
/* 0(1) */


void *SortedListGetData(sorted_list_iterator_t iterator); 
/* O(1) */


sorted_list_iterator_t SortedListInsert(sorted_list_t *sorted_list, void *data); 
/* O(n) */ /*retunrs inserted element*/


sorted_list_iterator_t SortedListRemove(sorted_list_iterator_t iterator); 
/* O(0) */  /* returns next element */ 


void *SortedListPopBack(sorted_list_t *sorted_list); 
/* returns data of the removed element */  /* O(1) */                  


void *SortedListPopFront(sorted_list_t *sorted_list); 
/* returns data of the removed element */  /* O(1) */


int SortedListForEach(sorted_list_iterator_t from, sorted_list_iterator_t to, 
                      sorted_list_action_func_t action, void *param); 
/* O(n) */ /* if fails return */


sorted_list_t *SortedListMerge(sorted_list_t *sorted_list1, 
							   sorted_list_t *sorted_list2); 
/* O(n+m) */ /* returns pointer to dest list?  use splice, the second list 
				becomes empty but not destroyed*/  
			/* warn the user to use lists with the same compare func */ 
			/* define for the user which element will go first if they are equal */ 
														

sorted_list_iterator_t SortedListFind(sorted_list_t *sorted_list, 
									  sorted_list_iterator_t from, 
									  sorted_list_iterator_t to, 
									  void *data); 
/* O(n) */ 
    						

sorted_list_iterator_t SortedListFindIf(sorted_list_iterator_t from, 
										sorted_list_iterator_t to,
    						            sorted_list_is_match_func_t is_match, 
    						            void *param); 
/* O(n) */ /* return the first occurence */						


#endif  /* __SORTED_LIST_H_ILRD__ */



