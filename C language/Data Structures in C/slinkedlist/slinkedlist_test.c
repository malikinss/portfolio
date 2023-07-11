/**********************************************
*    THIS FILE CONTAINS A TEST FUNCTIONS      *
*    CUSTOM IMPLEMENTATION OF SINGLY          *
*    LINKED LIST                              *
*    *************************	              *
*    Author: Sam                              *
*    Lab: OL - 142					          *
*    Reviewed by: Sergey Rabinovich           *
***********************************************/
#include <stdio.h> /* printf() */
#include "slinkedlist.h"

static void PrintAllIntValues(list_t *list);
int IsIntMatch(void *data, void *search_for);
int SumTwoInts(void *data, void *add_value);

list_t *TestCreate(list_t *sample, slist_iterator_t *iterator_sample);

void TestInsert(int *arr, list_t *sample);
void TestFind(int *arr, list_t *sample, slist_iterator_t *iterator_sample);
void TestChangeLastElement(int *arr, list_t *sample, slist_iterator_t *iterator_sample);
void TestInsertBetween(int *arr, list_t *sample, slist_iterator_t *iterator_sample);
void TestRemove(list_t *sample, slist_iterator_t *iterator_sample);
void AddTenFromFirst(list_t *sample, slist_iterator_t *iterator_sample);
void TestFind(int *arr, list_t *sample, slist_iterator_t *iterator_sample);

int main()
{
	list_t *sample = NULL;
	slist_iterator_t iterator_sample = NULL;
	int arr[8] = {0, 1, 2, 3, 4, 5, 6, 7};

	sample = TestCreate(sample, &iterator_sample);
	TestInsert(arr, sample);
	TestInsertBetween(arr, sample, &iterator_sample);
	TestChangeLastElement(arr, sample, &iterator_sample);
	TestRemove(sample, &iterator_sample);
	TestFind(arr, sample, &iterator_sample);
	AddTenFromFirst(sample, &iterator_sample);
	SLinkedListDestroy(sample);
	return 0;
}

static void PrintAllIntValues(list_t *list)
{
	slist_iterator_t iterator = SlinkedListBegin(list);
	size_t number_of_elements = SlinkedListCount(list);
	size_t i = 0;

	printf("\nLinked list contains |%ld| elements\n", number_of_elements);
	printf("Printing all int elements:\n");
	for(; i < number_of_elements; ++i)
	{
		printf("|%d|\n", *(int *)SlinkedListGetData(iterator));
		iterator = SlinkedListNext(iterator);
	}
}      

int IsIntMatch(void *data, void *search_for)
{
	return (*(int *)data == *(int *)search_for);
}

int SumTwoInts(void *data, void *add_value)
{
	*(int *)data += *(int *)add_value;

	return  0;
}

list_t *TestCreate(list_t *sample, slist_iterator_t *iterator_sample)
{
	slist_iterator_t iterator_ends = NULL;
	int same = 0;
	void *tmp = NULL;
	
	sample = SLinkedListCreate();
	*iterator_sample = SlinkedListBegin(sample);
	iterator_ends = SlinkedListEnd(sample);
	
	printf("\nCreating Singly Linked list\n");
	
	tmp = SlinkedListGetData(*iterator_sample);
	printf("begin addr = |%p|\n", tmp);
	
	tmp = SlinkedListGetData(iterator_ends);
	printf("end addr = |%p|\n", tmp);
	
	same = SlinkedListIsSameIterator(*iterator_sample, iterator_ends);
	printf("IsSame 1 == |%d|?\n", same);
	PrintAllIntValues(sample);
	
	return sample;
}

void TestInsert(int *arr, list_t *sample)
{
	printf("\nInserting 5 elements: 1, 2, 3, 4, 6");
	SlinkedListInsert(SlinkedListBegin(sample), &arr[2]);
	SlinkedListInsert(SlinkedListBegin(sample), &arr[1]);
	SlinkedListInsert(SlinkedListEnd(sample), &arr[3]);
	SlinkedListInsert(SlinkedListEnd(sample), &arr[4]);
	SlinkedListInsert(SlinkedListEnd(sample), &arr[6]);
	PrintAllIntValues(sample);
}

void TestChangeLastElement(int *arr, list_t *sample, slist_iterator_t *iterator_sample)
{
	printf("\nChange last element - 6 on 7");
	*iterator_sample = SlinkedListNext(*iterator_sample);
	*iterator_sample = SlinkedListSetData(*iterator_sample, &arr[7]);
	PrintAllIntValues(sample);
}

void TestInsertBetween(int *arr, list_t *sample, slist_iterator_t *iterator_sample)
{
	size_t i = 0;
	printf("\nGo to (last - 1) element and insert 5");
	for(i = 0; i < SlinkedListCount(sample) - 1; ++i)
	{
		*iterator_sample = SlinkedListNext(*iterator_sample);		
	}
	*iterator_sample = SlinkedListInsert(*iterator_sample, &arr[5]);
	PrintAllIntValues(sample);
}

void TestRemove(list_t *sample, slist_iterator_t *iterator_sample)
{
	printf("\nGet first element, remove it and get first element");
	*iterator_sample = SlinkedListBegin(sample);
	printf("\n1 == |%d|?\n", *(int *)SlinkedListGetData(*iterator_sample));	
	SlinkedListRemove(*iterator_sample);
	*iterator_sample = SlinkedListBegin(sample);
	printf("2 == |%d|?\n", *(int *)SlinkedListGetData(*iterator_sample));	
	PrintAllIntValues(sample);
}

void AddTenFromFirst(list_t *sample, slist_iterator_t *iterator_sample)
{
	int int_to_add = 10;
	int status = 0;
	
	printf("\nAdd to all (except first) elements 10\n");
	*iterator_sample = SlinkedListBegin(sample);
	*iterator_sample = SlinkedListNext(*iterator_sample);
	status = SlinkedListForEach(*iterator_sample, SlinkedListEnd(sample),
				&SumTwoInts, &int_to_add);
	printf("Status = |%d|", status);
	PrintAllIntValues(sample);
}

void TestFind(int *arr, list_t *sample, slist_iterator_t *iterator_sample)
{
	*iterator_sample = SLinkedListFind(SlinkedListBegin(sample),
	 SlinkedListEnd(sample), &IsIntMatch, &arr[2]);
	printf("Find 2 == |%d|?\n", *(int *)SlinkedListGetData(*iterator_sample));
	*iterator_sample = SLinkedListFind(SlinkedListBegin(sample),
	 SlinkedListEnd(sample), &IsIntMatch, &arr[7]);
	printf("Find 7 == |%d|?\n", *(int *)SlinkedListGetData(*iterator_sample));
	*iterator_sample = SLinkedListFind(SlinkedListBegin(sample),
	 SlinkedListEnd(sample), &IsIntMatch, &arr[1]);
	printf("Find 1(there is no 1) : |%d|\n", 
								*(int *)SlinkedListGetData(*iterator_sample));
	printf("Check if node IsSame with ListEnd: 1 == |%d|?\n", 
		SlinkedListIsSameIterator(*iterator_sample, SlinkedListEnd(sample)));
}
