/*
*********************************	
* Title : sorted_list testing	*
* Author: Sam Malikin			*
* Reviewer: ...					*
* Date : 24.04.2023				*
*********************************	
*/

#include <stdio.h>  /* printf */
#include <assert.h> /* assert */

#include "sorted_list.h"

#define ACTION(func) (printf("*** %s. ***\n", func))
#define ACTION_VALUE(func, val) (printf("%s %d.\n", func, val))

#define TEST(name) (printf("%s: ", name))
#define TEST_VALUE(name, value) (printf("%s is %d: ", name, value))

#define DONE (printf("Done!\n\n"))
#define BL (printf("\n"))

enum boolean
{
    FALSE,
    TRUE
};
enum compare
{
    EQUAL,
    MORE,
    LESS = -1
};

static int CompareInts(const void *data1, const void *data2);

static int AddInt(void *data, void *param);
static int IsDivisible(const void *data, const void *param);

static void TestSameIntValue(int tested, int control);
static void TestSameIterators(sorted_list_iterator_t iterator1,
                              sorted_list_iterator_t iterator2);
static void TestNotSameIterators(sorted_list_iterator_t iterator1,
                                 sorted_list_iterator_t iterator2);
static void TestCompareInts(const void *data1, const void *data2, int control);
static void TestFound(sorted_list_iterator_t iterator,
                      sorted_list_iterator_t to, int param);

static void PrintResult(int result);
static void PrintListElements(sorted_list_t *test_list);

int main()
{
    sorted_list_t *test_list = SortedListCreate(CompareInts);
    sorted_list_t *test_list2 = SortedListCreate(CompareInts);
    sorted_list_t *test_list3 = SortedListCreate(CompareInts);
    sorted_list_iterator_t test_iterator;
    int test_data[] = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9};
    int test_data2[] = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9};
    int i = 0;
    int size = 10;
    int param = 5;
    int param2 = 7;
    int param3 = 3;
    int param4 = 4;

    ACTION("Created a new empty list");
    TEST_VALUE("The list size", 0);
    TestSameIntValue(SortedListSize(test_list), 0);
    TEST("Begin and End are the same");
    TestSameIterators(SortedListBegin(test_list), SortedListEnd(test_list));
    TEST("The test list is empty");
    TestSameIntValue(SortedListIsEmpty(test_list), TRUE);
    DONE;

    ACTION("Inserting one element");
    test_iterator = SortedListInsert(test_list, &test_data[1]);
    TEST("The data is correct");
    TestSameIntValue(*(int *)SortedListGetData(test_iterator), test_data[1]);
    TEST("The test list is not empty");
    TestSameIntValue(SortedListIsEmpty(test_list), FALSE);
    TEST_VALUE("The list size", 1);
    TestSameIntValue(SortedListSize(test_list), 1);
    TEST("The new node is not the End");
    TestNotSameIterators(test_iterator, SortedListEnd(test_list));
    TEST("The next node is the End");
    TestSameIterators(SortedListNext(test_iterator), SortedListEnd(test_list));
    TEST("The new node is the Begin");
    TestSameIterators(test_iterator, SortedListBegin(test_list));

    DONE;

    ACTION("Inserting another element, it's larger");
    test_iterator = SortedListInsert(test_list, &test_data[2]);
    TEST("The data is correct");
    TestSameIntValue(*(int *)SortedListGetData(test_iterator), test_data[2]);
    TEST_VALUE("The list size", 2);
    TestSameIntValue(SortedListSize(test_list), 2);
    TEST("The new node is not the Begin");
    TestNotSameIterators(test_iterator, SortedListBegin(test_list));
    TEST("The next node is the End");
    TestSameIterators(SortedListNext(test_iterator), SortedListEnd(test_list));
    TEST("The previous node is less");
    TestCompareInts(SortedListGetData(SortedListPrev(test_iterator)),
                    SortedListGetData(test_iterator), LESS);
    DONE;

    ACTION("Inserting one more element, it's smaller");
    test_iterator = SortedListInsert(test_list, &test_data[0]);
    TEST("The data is correct");
    TestSameIntValue(*(int *)SortedListGetData(test_iterator), test_data[0]);
    TEST_VALUE("The list size", 3);
    TestSameIntValue(SortedListSize(test_list), 3);
    TEST("The new node is the Begin");
    TestSameIterators(test_iterator, SortedListBegin(test_list));
    TEST("The next node is more");
    TestCompareInts(SortedListGetData(SortedListNext(test_iterator)),
                    SortedListGetData(test_iterator), MORE);
    DONE;

    ACTION("Removing an element");
    test_iterator = SortedListRemove(SortedListNext(test_iterator));
    TEST_VALUE("The list size", 2);
    TestSameIntValue(SortedListSize(test_list), 2);
    TEST("The next node is the End");
    TestSameIterators(SortedListNext(test_iterator), SortedListEnd(test_list));
    TEST("The prev node is the Begin");
    TestSameIterators(SortedListPrev(test_iterator), SortedListBegin(test_list));
    DONE;

    ACTION("Popping from the back");
    TEST("Returned data is correct");
    TestSameIntValue(*(int *)SortedListPopBack(test_list), test_data[2]);
    TEST_VALUE("The list size", 1);
    TestSameIntValue(SortedListSize(test_list), 1);
    DONE;

    ACTION("Popping from the front");
    TEST("Returned data is correct");
    TestSameIntValue(*(int *)SortedListPopFront(test_list), test_data[0]);
    TEST_VALUE("The list size", 0);
    TestSameIntValue(SortedListSize(test_list), 0);
    TEST("The test list is empty");
    TestSameIntValue(SortedListIsEmpty(test_list), TRUE);
    DONE;

    ACTION("Inserting 10 elements into the test list");
    for (i = (size - 1); 0 <= i; --i)
    {
        SortedListInsert(test_list, &test_data[i]);
    }
    TEST_VALUE("The list size", size);
    TestSameIntValue(SortedListSize(test_list), size);
    BL;

    ACTION("Adding to each element with ForEach");
    SortedListForEach(SortedListBegin(test_list),
                      SortedListEnd(test_list), AddInt, &param);
    test_iterator = SortedListBegin(test_list);
    for (i = 0; i < size; ++i)
    {
        printf("Checking element %d: ", i);
        TestSameIntValue(*(int *)SortedListGetData(test_iterator), i + param);
        test_iterator = SortedListNext(test_iterator);
    }
    BL;

    TEST("Here're the elements of the list");
    BL;
    PrintListElements(test_list);
    DONE;

    ACTION("Testing Find functions");
    ACTION_VALUE("Looking for the element with value", param4);
    test_iterator = SortedListFind(test_list, SortedListBegin(test_list),
                                   SortedListEnd(test_list), &param4);
    TestFound(test_iterator, SortedListEnd(test_list), param4);
    BL;
    ACTION_VALUE("Looking for the element with value", param2);
    test_iterator = SortedListFind(test_list, SortedListBegin(test_list),
                                   SortedListEnd(test_list), &param2);
    TestFound(test_iterator, SortedListEnd(test_list), param2);
    BL;
    ACTION_VALUE("Looking for the next element divisible by", param3);
    test_iterator = SortedListFindIf(test_iterator, SortedListEnd(test_list),
                                     IsDivisible, &param3);
    TestFound(test_iterator, SortedListEnd(test_list), 9);
    DONE;

    ACTION("Creating a new list with 10 elements");
    for (i = (size - 1); 0 <= i; --i)
    {
        SortedListInsert(test_list2, &test_data[i]);
    }
    TEST_VALUE("The list size", size);
    TestSameIntValue(SortedListSize(test_list2), size);
    TEST("Here're the elements of the new list");
    BL;
    PrintListElements(test_list2);

    BL;



    ACTION("Merging the lists");
    PrintListElements(test_list);
    PrintListElements(test_list2);

    SortedListMerge(test_list, test_list2);
    TEST_VALUE("The list 1 size", size * 2);
    TestSameIntValue(SortedListSize(test_list), size * 2);
    TEST_VALUE("The list 2 size", 0);
    TestSameIntValue(SortedListSize(test_list2), 0);
    TEST("Here're the elements of the merged list");
    BL;
    PrintListElements(test_list);
    BL;

    ACTION("Merging them again, just to see what happens");
    SortedListMerge(test_list, test_list2);
    TEST_VALUE("The list 1 size", size * 2);
    TestSameIntValue(SortedListSize(test_list), size * 2);
    TEST_VALUE("The list 2 size", 0);
    TestSameIntValue(SortedListSize(test_list2), 0);
    TEST("Here're the elements of the merged list");
    BL;
    PrintListElements(test_list);
    DONE;

    ACTION("Creating another list with 10 elements");
    for (i = (size - 1); 0 <= i; --i)
    {
        SortedListInsert(test_list3, &test_data2[i]);
    }
    TEST_VALUE("The list size", size);
    TestSameIntValue(SortedListSize(test_list3), size);
    TEST("Here're the elements of the new list");
    BL;
    PrintListElements(test_list3);
    BL;
    ACTION("Merging the lists");
    SortedListMerge(test_list, test_list3);
    TEST_VALUE("The list 1 size", size * 3);
    TestSameIntValue(SortedListSize(test_list), size * 3);
    TEST_VALUE("The list 3 size", 0);
    TestSameIntValue(SortedListSize(test_list3), 0);
    TEST("Here're the elements of the merged list");
    BL;
    PrintListElements(test_list);
    DONE;

    ACTION("Merging empty lists, just to see what happens");
    SortedListMerge(test_list2, test_list3);
    TEST_VALUE("The list 2 size", 0);
    TestSameIntValue(SortedListSize(test_list2), 0);
    TEST_VALUE("The list 3 size", 0);
    TestSameIntValue(SortedListSize(test_list3), 0);
    TEST("Here're the elements of the merged list");
    BL;
    PrintListElements(test_list2);
    DONE;

    SortedListDestroy(test_list);
    test_list = NULL;
    SortedListDestroy(test_list2);
    test_list2 = NULL;
    SortedListDestroy(test_list3);
    test_list2 = NULL;

    printf("The sorted lists are gone! Check for leaks with Valgrind :)\n\n");

    return (0);
}

static int CompareInts(const void *data1, const void *data2)
{
    return (*(int *)data1 - *(int *)data2);
}

static int AddInt(void *data, void *param)
{
    assert(NULL != data);
    assert(NULL != param);

    *(int *)data += *(int *)param;

    return (0);
}

static int IsDivisible(const void *data, const void *param)
{
    assert(NULL != data);
    assert(NULL != param);

    return (0 == *(int *)data % *(int *)param);
}

static void TestSameIntValue(int tested, int control)
{
    PrintResult(control == tested);
}

static void TestSameIterators(sorted_list_iterator_t iterator1,
                              sorted_list_iterator_t iterator2)
{
    PrintResult(SortedListIsSameIterator(iterator1, iterator2));
}

static void TestNotSameIterators(sorted_list_iterator_t iterator1,
                                 sorted_list_iterator_t iterator2)
{
    PrintResult(!SortedListIsSameIterator(iterator1, iterator2));
}

static void TestCompareInts(const void *data1, const void *data2, int control)
{
    PrintResult(CompareInts(data1, data2) == control);
}

static void TestFound(sorted_list_iterator_t iterator,
                      sorted_list_iterator_t to, int param)
{
    if (SortedListIsSameIterator(iterator, to))
    {
        printf("Haven't found it.\n");
    }
    else
    {
        TEST("Found it");
        TestSameIntValue(*(int *)SortedListGetData(iterator), param);
    }
}

static void PrintResult(int result)
{
    if (!result)
    {
        printf("FAILED :(\n");
    }
    else
    {
        printf("ok.\n");
    }
}

static void PrintListElements(sorted_list_t *test_list)
{
    sorted_list_iterator_t test_iterator = SortedListBegin(test_list);
    sorted_list_iterator_t list_end = SortedListEnd(test_list);

    while (!SortedListIsSameIterator(test_iterator, list_end))
    {
        printf("%d ", *(int *)SortedListGetData(test_iterator));
        test_iterator = SortedListNext(test_iterator);
    }
    BL;
}
