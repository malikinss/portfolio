#ifndef __SLINKEDLIST_H__
#define __SLINKEDLIST_H__

#include <stddef.h> /* size_t */



typedef struct node node_t;
typedef node_t *slist_iterator_t; 

typedef struct list
{
	node_t *head;
	node_t *tail;
} list_t;

struct node
{
	void *data;
	node_t *next;
};

/*
DESCRIPTION
    A pointer to a function that executes an action on data using the param. 
    The actual action and types of the input are defined by the user.
RETURN
    0 - if success
    non-zero value - if failure
INPUT
    data: a pointer to some value;
    param: a pointer to a parameter.
*/
typedef int (*action_func_t)(void *data, void *param);

/*
DESCRIPTION
    A pointer to a function that validates if the data matches a certain 
    criteria using the param.
    The actual matching and types of the input is defined by the user.
RETURN
    1 true - if the criteria is matched.
    0 false - if it's not
INPUT
    data: a pointer to some value;
    param: a pointer to a parameter.    
*/
typedef int (*is_match_func_t)(void *data, void *param);            



/*
DESCRIPTION
    Creates a singly linked list.
    Creation may fail, due to memory allocation fail. 
    User is responsible for destroying the linked list.
RETURN
    Returns pointer to the created linked list on success.
    Returns NULL on failure.
INPUT
    Doesn't recieve an input from the user.

*/
list_t *SLinkedListCreate(void); /* O(1) */

/*
DESCRIPTION
    Frees the memory allocated for each element of a singly linked list.
RETURN
    There is no return for this function.
INPUT
    list: a pointer to a singly linked list.
*/
void SLinkedListDestroy(list_t *list); /* O(n) */

/*
DESCRIPTION
    Inserts a new element to a singly linked list in a position.
RETURN
    The address of the new iterator if success.
    The iterator corresponding to the last element if insertion failed.
INPUT
    iterator: iterator to the newly inserted data
    data: pointer to the user's data.
*/
slist_iterator_t SlinkedListInsert(slist_iterator_t iterator, void *data); 
                                                        /* O(n) if fails */

/*
DESCRIPTION
    Removes the element represented by iterator from a single linked
    list and returns the iterator representing the next element. 
    Trying to remove from an empty list may cause undefined behaviour
RETURN
    Iterator representing the next element. 
INPUT
    iterator: iterator representing the element to remove
*/
slist_iterator_t SlinkedListRemove(slist_iterator_t iterator); /* O(1) */

/*
DESCRIPTION
    Traverses the singly linked list and returns the amount of elements.
RETURN
    The amount of elements currently in the list. 
INPUT
    list: a pointer to a singly linked list.
*/
size_t SlinkedListCount(const list_t *list); /* O(n) */ 

/*
DESCRIPTION
    Searches in a single linked list in a range for the element that satisfies
    is_match function and returns the first occurance or the iterator 
    representing the "to" element of the list if the elemnt isn't found. 
    The "to" element is marks the end of the searched range 
    but is not included in it.
RETURN
    If found -- the iterator representing the first element in the range that 
    contains the value when it finds the value.
    If not -- the iterator representing the ending element.
INPUT
    from: iterator representing the element that starts the range;
    to: iterator marking the end of the range (isn't a part of the range);
    is_match: a function that checks values
    param: a parameter for the is_match function.
*/
slist_iterator_t SLinkedListFind(const slist_iterator_t from, 
    const slist_iterator_t to, is_match_func_t is_match, void *param); 
                                                                /* O(n) */

/*
DESCRIPTION
    Traverses the linked list from one point to another and performs 
    a specific action specified by the user. The "to" element is marks 
    the end of the searched range but is not included in it.
    Actions performed might fail. 
RETURN
    0: if no actions fail; 
    non-zero value: if an action failed. 
INPUT
    from: iterator representing the element that starts the range;
    to: iterator marking the end of the range (isn't a part of the range);
    action: a pointer to an action function;
    param: a parameter for the action function.
*/
int SlinkedListForEach(const slist_iterator_t from, const slist_iterator_t to, 
                        action_func_t action, void *param); /* O(log n) */

/*
DESCRIPTION
    Receives a pointer to a single linked list and returns an iterator 
    that represents the beginning of the list.                                                  
RETURN
    Iterator that points to the beginning of
    the list.
INPUT
    list: a pointer to a single linked list.
*/
slist_iterator_t SlinkedListBegin(const list_t *list); /* O(1) */

/*
DESCRIPTION
    Recieves a pointer to a singly linked list and returns an iterator
    representing the ending element of that list. The end is 
    theoretical element which follows the last element of the list. 
    It neither contain actual data nor point to any other element.
RETURN
    Returns the iterator representing the ending element of the list.
INPUT
    list: a pointer to a singly linked list.
*/
slist_iterator_t SlinkedListEnd(const list_t *list); /* O(1) */

/*
DESCRIPTION
    Returns an address of the iterator next to the one passed by the user.
    Passing an iterator received from the function SLinkedListEnd may cause
    undefined behavior.
RETURN
    Function returns a pointer to an iterator
INPUT
    iterator: a pointer to an iterator.
*/
slist_iterator_t SlinkedListNext(slist_iterator_t iterator); /* O(1) */

/*
DESCRIPTION
    Set data in an element represented by the given iterator.
    Trying to put data in the element representing the end of the list 
    may result in undefined behavior.
RETURN
    Function returns a pointer to an iterator
INPUT
    iterator: a pointer to an iterator.
*/
slist_iterator_t SlinkedListSetData(slist_iterator_t iterator, void *data); 
                                                                /* O(1) */      

/*
DESCRIPTION
    Get data from an element represented by the given iterator.
RETURN
    Return a generic pointer to data.
INPUT
    iterator: a pointer to an iterator.
*/
void *SlinkedListGetData(slist_iterator_t iterator); /* O(1) */

/*
DESCRIPTION
    Compares two iterators to check if they are the same.
RETURN
    1 if the iterators are the same;
    0 if they are not.
INPUT
    iterator1: an iterator representing an element in the list.
    iterator2: an iterator representing another element in the list.
*/
int SlinkedListIsSameIterator(slist_iterator_t iterator1, 
                            slist_iterator_t iterator2);    /* O(1) */
                            
void SlinkedListAppend(list_t *dest, list_t *src);
#endif  /* __SLINKEDLIST_H__ */

