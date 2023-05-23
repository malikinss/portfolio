/*
*************************************	
* Title : dlinkedlist header file	*
* Author: Sam Malikin				*
* Reviewer: ...						*
* Date : 22.04.2023					*
*************************************	
*/
#ifndef __DLIST_H_ILRD__
#define __DLIST_H_ILRD__

#include <stddef.h> /* size_t */

typedef struct dlist dlist_t;
typedef struct dlist_node *dlist_iterator_t;


/*
DESCRIPTION:
	User-defined function pointer that performs an operation on data using a
	parameter. The specific action and input types are determined by the user.

RETURN:
	If the operation is successful, a value of 0 will be returned. 
	If the operation fails, a non-zero value will be returned.

INPUT:
	data: a pointer to the data provided by the user.
	param: a pointer to a parameter required for the action.
*/
typedef int (*dlist_action_func_t)(void *data, void *param);


/*
DESCRIPTION:
	User-defined function pointer that takes a parameter and checks whether
	data meets specific criteria. The matching process and input types are 
	determined by the user.

RETURN:
	1 (true) if the conditions are satisfied, and 0 (false) if they are not

INPUT:
	data: a pointer to user's data.
	param: a pointer to a parameter that will be used for comparison.
*/
typedef int (*dlist_is_match_func_t)(const void *data, void *param);


/*
DESCRIPTION:
	This function initializes a new doubly linked list. 
	However, there is a possibility of failure in the creation process due 
	to memory allocation issues. 
	It is the responsibility of the user to free the memory of the doubly 
	linked list once it is no longer needed.

RETURN:
	On successful creation, the function returns a pointer to the newly created
	doubly linked list. 
	In the event of a memory allocation failure, the function returns NULL.

INPUT:
	No input is required for this function.
*/
dlist_t *DListCreate(void); /* O(1) */


/*
DESCRIPTION:
	This function releases the memory allocated for each element of the specified 
	doubly linked list and the list itself. 
	All data inside the list will be lost. 
	The user is responsible for handling any dangling pointers after the list is 
	destroyed.

RETURN:
	This function does not return anything.

INPUT:
	dlist - a pointer to the doubly linked list to be destroyed.
*/
void DListDestroy(dlist_t *dlist); /* O(n) */


/*
DESCRIPTION:
	Count the number of elements in a given doubly linked list.

RETURN:
	The function returns the total number of elements present in the dlist.

INPUT:
	dlist- a pointer to the doubly linked list.
*/
size_t DListSize(const dlist_t *dlist); /* O(n)*/  


/*
DESCRIPTION:
	Determines whether a given doubly linked list is empty or not.

RETURN:
	1 (true) - if the doubly linked list is empty.
	0 (false) - if it is not empty.

INPUT:
	dlist- a pointer to the doubly linked list.
*/
int DListIsEmpty(const dlist_t *dlist); /* O(1) */


/*
DESCRIPTION:
	Find the first occurrence of an element in a given range of a doubly linked
	list that satisfies the criteria specified in the user-provided function 
	'is_match'. 
	The range includes elements starting from the 'from' iterator up to, but not 
	including, the 'to' iterator.

RETURN:
	Returns an iterator representing the first element in the range that matches 
	the 'is_match' function's criteria. 
	If no matches are found, it returns an iterator representing the end of the 
	doubly linked list (a theoretical element).

INPUT:
	'from' - an iterator representing the starting element of the range.
	'to' - an iterator marking the end of the range (not included in the range).
	'is_match' - a user-provided function that checks if the criteria are met.
	'param' - a parameter used by the 'is_match' function.
*/
dlist_iterator_t DListFind(dlist_iterator_t from, dlist_iterator_t to,
    				dlist_is_match_func_t is_match, void *param); /* O(n) */


/*
DESCRIPTION:
	Searches for elements within a specified range in a doubly linked list that 
	satisfy the criteria defined in the user's "is_match" function. 
	The discovered elements are then appended to the end of the "output_list" 
	in the order they were found. 
	The element indicated by "to" is the endpoint of the range but is not 
	included in the search.

RETURN:
	Returns the count of elements that match the criteria defined in the
	"is_match" function.

INPUT:
	from - an iterator pointing to the first element in the search range.
	to - an iterator marking the end of the search range (but not inclusive).
	output_list - a doubly linked list into which the matching elements will 
				  be inserted.
	is_match - a user-defined function that determines whether an element meets
			   the search criteria.
	param - a parameter to be passed into the "is_match" function.
*/
int DListMultiFind(dlist_iterator_t from, dlist_iterator_t to,
	dlist_t *output_list, dlist_is_match_func_t is_match, void *param); 
																/* O(n) */


/*
DESCRIPTION:
	Traverse a specified range of elements in a doubly linked list and execute 
	a user-defined action function on each element's data and parameter input. 
	The range is defined by the starting element, represented by the "from" 
	iterator, and the end element, marked by the "to" iterator (not inclusive). 
	The actions performed may fail.

RETURN:
	The function returns 0 if all actions are successful, and a non-zero value 
	if at least one action fails.

INPUT:
	from - iterator representing the element that starts the range
	to - iterator marking the end of the range (not included)
	action - user's function that executes an action
	param - parameter for the is_match function.
*/
int DListForEach(dlist_iterator_t from, dlist_iterator_t to, 
                       	dlist_action_func_t action, void *param); /* O(n) */


/*
DESCRIPTION:
	Inserts a new element into a dlist before the position of the specified 
	iterator.

RETURN:
	Returns an iterator representing the new element if the insertion is 
	successful, or an iterator representing the theoretical end of the dlist 
	if memory allocation fails.

INPUT:
	iterator - an iterator representing the element before which to insert the 
			   new element.
	data - a pointer to the user's data.
*/
dlist_iterator_t DListInsert(dlist_iterator_t iterator, void *data); /* O(n) */


/*
DESCRIPTION:
	Eliminates the element indicated by the iterator from a dlist.
	Using an iterator obtained from the DListEnd() function could result in
	ambiguous behavior.

RETURN:
	Iterator that denotes the subsequent element.

INPUT:
	iterator - iterator that designates the element to be deleted.
*/
dlist_iterator_t DListRemove(dlist_iterator_t iterator); /* O(1) */


/*
DESCRIPTION:
	Provide an iterator that represents the first element of the given dlist 
	through a pointer.

RETURN:
	Pointer to an iterator representing the first element in the dlist.

INPUT:
	dlist - a pointer to the dlist.
*/
dlist_iterator_t DListBegin(const dlist_t *dlist); /* O(1) */


/*
DESCRIPTION:
	Provide an iterator that represents the theoretical end of the given dlist
	through a pointer.
	The end is a conceptual element that comes after the last element of the 
	list and does not contain any actual data.

RETURN:
	Pointer to an iterator representing the end of a doubly linked list 
	(theoretical element).

INPUT:
	dlist - a pointer to the dlist.
*/
dlist_iterator_t DListEnd(const dlist_t *dlist); /* O(1) */


/*
DESCRIPTION:
	Provide an iterator that represents the next element in the dlist. 
	Using an iterator obtained from the DListEnd() function as input may lead 
	to uncertain behavior.

RETURN:
	Pointer to an iterator representing the next element in the dlist.

INPUT:
	iterator - Pointer to an iterator that represents the element.
*/
dlist_iterator_t DListNext(dlist_iterator_t iterator); /* O(1) */


/*
DESCRIPTION:
	Provide an iterator that represents the previous element in the given dlist. 
	Note that using an iterator obtained from the DListBegin() function may 
	result in undefined behavior.

RETURN:
	Pointer to an iterator representing the previous element in the dlist.

INPUT:
	iterator - Pointer to the iterator that represents the element.
*/
dlist_iterator_t DListPrev(dlist_iterator_t iterator); /* O(1) */


/*
DESCRIPTION:
	Compare two iterators to determine if they refer to the same element.

RETURN:
	1 (true) - if the iterators refer to the same element.
	0 (false) - if they do not refer to the same element.

INPUT:
	iterator1 - representing an element in the dlist.
	iterator2 - representing another element in the dlist.
*/
int DListIsSameIterator(dlist_iterator_t iterator1, 
						dlist_iterator_t iterator2); /* 0(1) */


/*
DESCRIPTION:
	Retrieve the user's data stored in the element represented by the provided 
	iterator, which is referenced in the doubly linked list. 
	Using an iterator obtained from the DListEnd() function may result in 
	unpredictable behavior.

RETURN:
	Return a pointer to the user's data stored in the element.

INPUT:
	iterator - representing an element in the doubly linked list.
*/
void *DListGetData(dlist_iterator_t iterator); /* O(1) */


/*
DESCRIPTION:
	Set the data in the element represented by the provided iterator. 
	The data is stored in the doubly linked list by reference. 
	Using an iterator obtained from the DListEnd() function may result in undefined behavior.

RETURN:
	No return value.

INPUT:
	iterator - representing the element in the doubly linked list.
	data - pointer to the user's data.
*/
void DListSetData(dlist_iterator_t iterator, void *data); /* O(1) */


/*
DESCRIPTION:
	Attempt to insert a new element containing the user's data at the end of the
	given dlist. 
	The insertion may fail if there is insufficient memory.

RETURN:
	Return an iterator representing the newly inserted element if the insertion 
	was successful. 
	Otherwise, return an iterator representing the theoretical end of the dlist.

INPUT:
	dlist - a pointer to the dlist.
	data - a pointer to the user's data.
*/
dlist_iterator_t DListPushBack(dlist_t *dlist, void *data);


/*
DESCRIPTION:
	Remove the last element of the given dlist. 
	Attempting to pop an empty dlist may lead to undefined behavior.

RETURN:
	A pointer to data of deleted element.

INPUT:
	dlist - a pointer to the dlist.
*/
void *DListPopBack(dlist_t *dlist);


/*
DESCRIPTION:
	Insert a new element at the beginning of the given dlist. 
	The insertion process may fail in case of memory allocation failure.

RETURN:
	Return an iterator that represents the newly added element if the insertion
	process is successful. 
	In case of failure, return an iterator that represents the theoretical end 
	of the dlist.

INPUT:
	dlist - a pointer to the dlist.
	data - a pointer to the user's data.
*/
dlist_iterator_t DListPushFront(dlist_t *dlist, void *data);


/*
DESCRIPTION:
	Remove the initial element of the given dlist through a pointer. 
	Caution: Attempting to pop an empty dlist may lead to undefined behavior.

RETURN:
	Pointer to data of deleted element.

INPUT:
	dlist - a pointer to the dlist.
*/
void *DListPopFront(dlist_t *dlist);


/*
DESCRIPTION:
	Take a specific range of elements from a doubly linked list, remove them
	from their current position, and insert them before the specified "where" iterator.

RETURN:
	Provide an iterator that represents the initial element of the spliced subchain. 
	If "from" and "to" iterators are the same, the function will return it and have no effect.

INPUT:
	where - Iterator that represents the element before which the spliced 
			subchain is to be appended.
	from - Iterator that represents the first element of the range to be 
		   spliced.
	to - Iterator that marks the end of the range to be spliced (but is not 
		 part of it).
*/
dlist_iterator_t DListSplice(dlist_iterator_t where, dlist_iterator_t from, 
														dlist_iterator_t to);


#endif  /* __DLIST_H_ILRD__ */

