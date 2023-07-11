/*
*********************************	
* Title : dlinkedlist testing	*
* Author: Sam Malikin			*
* Reviewer: ...					*
* Date : 22.04.2023				*
*********************************	
*/

#include <stdio.h>  /* printf */ 
#include <assert.h>	/* assert */

#include "dlist.h"

#define ACTION(func) (printf("%s.\n", func))
#define TEST(name) (printf("%s: ", name))
#define TEST_VALUE(name, value) (printf("%s is %d: ", name, value))

#define DONE (printf("Done!\n\n"))
#define BL (printf("\n"))


static int IsEqualInt(const void *data, void *param);
static int IsDivisible(const void *data, void *param);
static int AddInt(void *data, void *param);
static int SubInt(void *data, void *param);

static void TestSameIntValue(int tested, int control);
static void TestSameIterators(dlist_iterator_t iterator1, 
									  dlist_iterator_t iterator2);										 
static void TestNotSameIterators(dlist_iterator_t iterator1, 
											dlist_iterator_t iterator2);

enum boolean {FALSE, TRUE};


int main()
{
	dlist_t *test_dlist = DListCreate();
	dlist_t *test_dlist2 = DListCreate();	
	dlist_iterator_t test_iterator;
	dlist_iterator_t test_iterator2;
	dlist_iterator_t test_iterator3;	
	int test_data[] = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9};
	int i = 0;
	int param = 2;
	int param2 = 4;
	size_t find_count = 0;


	ACTION("Created a new empty list");
	TEST_VALUE("The list size", 0);
	TestSameIntValue(DListSize(test_dlist), 0);	
	TEST("Begin and End are the same");
	TestSameIterators(DListBegin(test_dlist), DListEnd(test_dlist));
	TEST("The test list is empty");
	TestSameIntValue(DListIsEmpty(test_dlist), TRUE);	
	DONE;
	
	ACTION("Inserting one element");
	test_iterator = DListInsert(DListEnd(test_dlist), &test_data[0]);
	TEST("The test list is not empty");
	TestSameIntValue(DListIsEmpty(test_dlist), FALSE);
	TEST_VALUE("The list size", 1);
	TestSameIntValue(DListSize(test_dlist), 1);	
	TEST("The new node is not the End");
	TestNotSameIterators(test_iterator, DListEnd(test_dlist));
	TEST("The next node is the End");
	TestSameIterators(DListNext(test_iterator), DListEnd(test_dlist));
	TEST("The new node is the Begin");
	TestSameIterators(test_iterator, DListBegin(test_dlist));	
	TEST("The data is correct");
	TestSameIntValue(*(int *)DListGetData(test_iterator), test_data[0]);
	DONE;
	
	ACTION("Setting new data");
	DListSetData(test_iterator, &test_data[1]);
	TEST("The data is correct");
	TestSameIntValue(*(int *)DListGetData(test_iterator), test_data[1]);
	DONE;

	ACTION("Pushing to the back");
	test_iterator = DListPushBack(test_dlist, &test_data[9]);
	TEST_VALUE("The list size", 2);
	TestSameIntValue(DListSize(test_dlist), 2);
	TEST("The data is correct");
	TestSameIntValue(*(int *)DListGetData(test_iterator), test_data[9]);
	TEST("The next node is the End");
	TestSameIterators(DListNext(test_iterator), DListEnd(test_dlist));	
	DONE;

	ACTION("Pushing to the front");
	test_iterator = DListPushFront(test_dlist, &test_data[0]);
	TEST_VALUE("The list size", 3);
	TestSameIntValue(DListSize(test_dlist), 3);	
	TEST("The data is correct");
	TestSameIntValue(*(int *)DListGetData(test_iterator), test_data[0]);		
	TEST("The new node is the Begin");
	TestSameIterators(test_iterator, DListBegin(test_dlist));
	DONE;	
	
	ACTION("Removing an element");	
	test_iterator = DListRemove(DListNext(test_iterator));
	TEST_VALUE("The list size", 2);
	TestSameIntValue(DListSize(test_dlist), 2);		
	TEST("The next node is the End");
	TestSameIterators(DListNext(test_iterator), DListEnd(test_dlist));
	TEST("The prev node is the Begin");
	TestSameIterators(DListPrev(test_iterator), DListBegin(test_dlist));		
	DONE;
	
	ACTION("Popping from the back");
	test_iterator = DListPopBack(test_dlist);
	TEST_VALUE("The list size", 1);
	TestSameIntValue(DListSize(test_dlist), 1);		
	TEST("The current node is the End");
	TestSameIterators(test_iterator, DListEnd(test_dlist));	
	DONE;	
	
	ACTION("Popping from the front");
	test_iterator = DListPopFront(test_dlist);
	TEST_VALUE("The list size", 0);
	TestSameIntValue(DListSize(test_dlist), 0);		
	TEST("The current node is the Begin");
	TestSameIterators(test_iterator, DListBegin(test_dlist));
	TEST("The current node is the End");
	TestSameIterators(test_iterator, DListEnd(test_dlist));	
	TEST("The test list is empty");
	TestSameIntValue(DListIsEmpty(test_dlist), TRUE);	
	DONE;	

	ACTION("Inserting 10 elements into the test list");
	test_iterator = DListBegin(test_dlist);
	for (i = 9; 0 <= i; --i)
	{
		test_iterator = DListInsert(test_iterator, &test_data[i]);
	}
	TEST_VALUE("The list size", 10);
	TestSameIntValue(DListSize(test_dlist), 10);
	BL;
	
	ACTION("Adding 2 to each element with ForEach");	
	DListForEach(DListBegin(test_dlist), 
					DListEnd(test_dlist), AddInt, &param);
	test_iterator = DListBegin(test_dlist);
	for (i = 0; i < 10; ++i)
	{
		printf("Checking element %d: ", i);
		TestSameIntValue(*(int *)DListGetData(test_iterator), i + 2);
		test_iterator = DListNext(test_iterator);
	}
	DONE;
	
	ACTION("Looking for the element with value 4");
	test_iterator = DListFind(DListBegin(test_dlist), DListEnd(test_dlist), 
														IsEqualInt, &param2);
	TEST("Found it");
	TestSameIntValue(*(int *)DListGetData(test_iterator), param2);
	DONE;
	
	ACTION("Looking for all even elements");
	find_count = DListMultiFind(DListBegin(test_dlist), DListEnd(test_dlist), 
											test_dlist2, IsDivisible, &param);
	TEST("Found 5 of them and put to List 2");
	TestSameIntValue(find_count, 5);
	TEST_VALUE("The List 2 size", 5);
	TestSameIntValue(DListSize(test_dlist2), 5);		
	test_iterator2 = DListBegin(test_dlist2);
	for (i = 0; i < 5; ++i)
	{
		printf("Checking element %d: ", i);
		TestSameIntValue(*(int *)DListGetData(test_iterator2) % 2, 0);
		test_iterator2 = DListNext(test_iterator2);
	}
	TEST("List 1 and List 2 are different lists");
	TestNotSameIterators(DListBegin(test_dlist), DListBegin(test_dlist2));		
	DONE;

	ACTION("Subtracting 2 from each element of List 1");
	DListForEach(DListBegin(test_dlist), 
					DListEnd(test_dlist), SubInt, &param);	
	test_iterator = DListBegin(test_dlist);
	test_iterator = DListNext(test_iterator);
	test_iterator = DListNext(test_iterator);
	TEST("Node #2 of List 1 is 2");
	TestSameIntValue(*(int *)DListGetData(test_iterator), 2);
	test_iterator2 = DListNext(test_iterator);
	test_iterator2 = DListNext(test_iterator2);
	TEST("Node #4 of List 1 is 4");
	TestSameIntValue(*(int *)DListGetData(test_iterator2), 4);	
	test_iterator2 = DListNext(test_iterator2);
	test_iterator3 = DListBegin(test_dlist2);
	test_iterator3 = DListNext(test_iterator3);	
	test_iterator3 = DListNext(test_iterator3);
	TEST("Node #2 of List 2 is 4");
	TestSameIntValue(*(int *)DListGetData(test_iterator3), 4);	

	ACTION("Splicing nodes 2 to 4 from List 1 before node 2 of List 2");
	DListSplice(test_iterator3, test_iterator, test_iterator2); 
	TEST_VALUE("The List 1 size", 7);
	TestSameIntValue(DListSize(test_dlist), 7);
	TEST_VALUE("The List 2 size", 8);
	TestSameIntValue(DListSize(test_dlist2), 8);
	TEST("Elements of the List 1");
	BL;
	test_iterator = DListBegin(test_dlist);
	for (i = 0; i < 7; ++i)
	{
		printf("%d ", *(int *)DListGetData(test_iterator));
		test_iterator = DListNext(test_iterator);
	}
	BL;
	TEST("Elements of the List 2");
	BL;
	test_iterator3 = DListBegin(test_dlist2);
	for (i = 0; i < 8; ++i)
	{
		printf("%d ", *(int *)DListGetData(test_iterator3));
		test_iterator3 = DListNext(test_iterator3);
	}
	BL;
	DONE;	

	DListDestroy(test_dlist);
	test_dlist = NULL;
	test_iterator = NULL;
	DListDestroy(test_dlist2);
	test_dlist2 = NULL;
	test_iterator2 = NULL;	
	printf("The dlists are gone! Check for leaks with Valgrind :)\n\n");	

	
	return (0);
}


static int IsEqualInt(const void *data, void *param)
{
	assert(NULL != data);
	assert(NULL != param);
	
	return (*(int *)data == *(int *)param);
}


static int IsDivisible(const void *data, void *param)
{
	assert(NULL != data);
	assert(NULL != param);
	
	return (0 == *(int *)data % *(int *)param);
}


static int AddInt(void *data, void *param)
{
	assert(NULL != data);
	assert(NULL != param);
	
	*(int *)data += *(int *)param;
	
	return (0);
}

static int SubInt(void *data, void *param)
{
	assert(NULL != data);
	assert(NULL != param);
	
	*(int *)data -= *(int *)param;
	
	return (0);
}

static void TestSameIntValue(int tested, int control)
{
	if (control != tested)
	{
		printf("FAILED :(\n");
	}
	else
	{
		printf("ok.\n");
	}	
}

static void TestSameIterators(dlist_iterator_t iterator1, 
											dlist_iterator_t iterator2)
{
	if (!DListIsSameIterator(iterator1, iterator2))
	{
		printf("FAILED :(\n");
	}
	else
	{
		printf("ok.\n");
	}
}


static void TestNotSameIterators(dlist_iterator_t iterator1, 
										   dlist_iterator_t iterator2)
{
	if (DListIsSameIterator(iterator1, iterator2))
	{
		printf("FAILED :(\n");
	}
	else
	{
		printf("ok.\n");
	}
}

