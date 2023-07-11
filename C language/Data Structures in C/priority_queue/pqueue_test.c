/*
*****************************
* Title : PQ test functions	*
* Author: Sam Malikin		*
* Reviewer: Sergey			*
* Date : 07.05.2023			*
*****************************
*/
#include <assert.h> /* assert */
#include <stdio.h>  /* printf */

#include "pqueue.h"

int CompareTwoIntValues(const void *data1, const void *data2);
int MatchDataGraterThanParam(const void *data, const void *param);

static void PrintTestResult(int expression, char *name);
static void TestFunc(int value_to_compare, int value_to_check, char *name);



int main()
{
    int number1 = 89;
    int number2 = 8;
    int number3 = 9;

    pq_t *test_pqueue_1 = PQCreate(CompareTwoIntValues);
    
    
    TestFunc(1, PQIsEmpty(test_pqueue_1), "PQIsEmpty");
    TestFunc(0, PQEnqueue(test_pqueue_1, &number1), "PQEnqueue");

    PQEnqueue(test_pqueue_1, &number2);
    PQEnqueue(test_pqueue_1, &number3);
    
    TestFunc(3, PQSize(test_pqueue_1), "PQSize");
    TestFunc(number1, *(int *)PQDequeue(test_pqueue_1), "PQDequeue");
    TestFunc(number3, *(int *)PQPeek(test_pqueue_1), "PQPeek");
    TestFunc(0, PQIsEmpty(test_pqueue_1), "PQIsEmpty");
	TestFunc(2, PQSize(test_pqueue_1), "PQSize");

    PQClear(test_pqueue_1);
    
    TestFunc(1, PQIsEmpty(test_pqueue_1), "PQClear");

    PQEnqueue(test_pqueue_1, &number1); /* 89 */
    PQEnqueue(test_pqueue_1, &number2); /*  8 */
    PQEnqueue(test_pqueue_1, &number3); /*  9 */

    /* 8 9 89  -> matching > 8 -> 9, removing 9*/
	
	TestFunc(9, *(int *)PQErase(test_pqueue_1, MatchDataGraterThanParam, &number2), "PQErase");
	
    PQDestroy(test_pqueue_1);
    
    printf("DONE\n");

    return (0);
}


int CompareTwoIntValues(const void *data1, const void *data2)
{
    int data1_value = 0;
    int data2_value = 0;

    assert(NULL != data1);
    assert(NULL != data2);

    data1_value = *(int *)data1;
    data2_value = *(int *)data2;

    if (data1_value > data2_value)
    {
        return 1;
    }
    else if (data1_value < data2_value)
    {
        return -1;
    }
    else
    {
        return 0;
    }
}

int MatchDataGraterThanParam(const void *data, const void *param)
{
    int data_value = 0;
    int param_value = 0;

    assert(NULL != data);
    assert(NULL != param);

    data_value = *(int *)data;
    param_value = *(int *)param;

    if (data_value > param_value)
    {
        return 1;
    }
    else
    {
        return 0;
    }
}

static void PrintTestResult(int expression, char *name)
{
	if (expression)
    {
        printf("%s test is passed\n", name);
    }
    else
    {
        printf("TEST FAILED\n\n");
    }
}

static void TestFunc(int value_to_compare, int value_to_check, char *name)
{
	int expression = 0;
	
	expression = (value_to_compare == value_to_check);
    PrintTestResult(expression, name);
}
