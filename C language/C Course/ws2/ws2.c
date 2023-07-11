#include <assert.h>
#include <stdio.h>
#include <stdlib.h>
#include "ws2.h"

/******************* Swap Functions ************************/

void Swap(int *a, int *b)
{        
    int tmp = *a;
    *a = *b;
    *b = tmp;
}

void SwapSizeT(size_t *first, size_t *second)
{
    size_t tmp = *first;
    *first = *second;
    *second = tmp;
}
    
void SwapSizeTPtr1(size_t **first, size_t **second)
{
    size_t *tmp = *first;
    *first = *second;
    *second = tmp;
}
    
void SwapSizeTPtr2(size_t **first, size_t **second)
{
     SwapSizeT((size_t *)first, (size_t *)second);
}

/******************* Copy of Array ************************/

void CopyIntArray(int *array, int *new_array, size_t size)
{   
    size_t i = 0;
    
    assert(NULL != array);
    assert(NULL != new_array);
        
    for(i = 0; size > i; ++i )
    {
        new_array[i] = array[i];
    }
}

/******************* Print Addresses ************************/

void PrintAddresses()
{
	static int s_i = 7;
	int i = 7;
	int *ptr = &i;
	int *ptr2 = (int *)malloc(sizeof(int));
	
	printf("Address of s_i = %p\n", (void *)&s_i);
	printf("Address of i = %p\n", (void *)&i);
	printf("Address of ptr = %p\n", (void *)ptr);
	printf("Address of ptr2 = %p\n", (void *)ptr2);

	if (ptr)
	{
		int **ptr3 = &ptr;
		printf("Address of ptr3 = %p\n", (void *)ptr3);
	}
	free(ptr2);
}

/******************* Length of the String ************************/

size_t StrLen(const char *s)
{   
    const char *runner = s;
    
    assert(NULL != s);
        
    while('\0' != *runner)
    {
		++runner;
    }

    return (runner - s);
}

/******************* Compare of the Strings ************************/

int StrCmp(const char *first_str, const char *second_str)
{
    assert(NULL != first_str);
    assert(NULL != second_str);
        
    while(*first_str && (*first_str == *second_str))
    {
        ++first_str;
        ++second_str;
    }
        
    return ((int)*first_str - *second_str);
}
