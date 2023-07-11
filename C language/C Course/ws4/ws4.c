/* Reviewed by Dima */
#include <stdio.h> /* printf() */
#include <assert.h> /* assert() */
#include <stdlib.h> /* free() */
#include <string.h> /* strlen() */
#include <ctype.h> /* tolower() */
#include <stddef.h> /* size_t */

#define NULL_TERMINATOR ('\0')

/*************** Sum of Matrix Rows ***************/
int *SumOfMatrixRows(int **arr, size_t row, size_t col, int *result)
{
    size_t i = 0;
    size_t j = 0;
    int sum = 0;
    int **runner = arr;
    
    assert(NULL != arr);
    assert(NULL != row);
    assert(NULL != col);
    
    if(NULL == runner)
	{
		return NULL;
	}

    for(i = 0; row > i; ++i)
    {	
    	for(j = 0; col > j; ++j)
    	{
    	    sum += runner[i][j];
    	}
    	result[i] = sum;
    	sum = 0;
    }
    return result;
}

void CreateArray(int **arr, size_t row, size_t col)
{
    size_t i = 0;
    size_t j = 0;
    int a = 1;
    
    assert(0 < row);
    assert(0 < col);
    
    for(i = 0; row > i; ++i)
    {
        for(j = 0; col > j; ++j)
        {   
            arr[i][j] = a;
            ++a;
        }
    }
}

void PrintArray(int *result, size_t row)
{
    size_t i = 0;
    
    assert(0 < row);
    assert(NULL != result);
    
    for (i = 0; row > i; ++i)
    {
        printf("%d\n", result[i]);
    } 
}

void FreeAllInt(int **arr, size_t size)
{
    size_t i = 0;
    
    assert(NULL != arr);
    
    for (i = 0; i < size; ++i)
    {
        free(arr[i]);
		arr[i] = NULL;
    }
    free(arr);
    arr = NULL;
}

/*************** Josephus Problem ***************/
void InitSoldiersArray(unsigned int *soldiers, size_t n)
{
    size_t i = 0;
    
    assert(0 < n);
    
    for(i = 0; n - 1 != i; ++i)
    {
		*soldiers = i+1;
		++soldiers;
    }
    *soldiers = 0;	
}

unsigned int FindLastSurvivor(unsigned int *soldiers)
{
    unsigned int survivor = 0;
    
    assert(NULL != soldiers);
    
    while(survivor != soldiers[survivor])
    {	
		soldiers[survivor] = soldiers[soldiers[survivor]];
		survivor = soldiers[survivor];
    }
    return (survivor);
}

unsigned int JosephusProblem(const size_t n)
{
    unsigned int survivor = 0;
    unsigned int *soldiers = NULL;
    
    assert(0 < n);
    
    soldiers = (unsigned int *)malloc(n*sizeof(int));
    if(NULL == soldiers)
    {
        return (-1);
    }
    
    InitSoldiersArray(soldiers, n);
    survivor = FindLastSurvivor(soldiers);
    
    free(soldiers);
    soldiers = NULL;
    
    return (survivor);
}

/*************** Print data types ***************/
void PrintDataTypes()
{
    char *pointer = NULL;
    char array[1] = {0};

    printf("Char size = %ld;\n", sizeof(char));
    printf("Short size = %ld;\n", sizeof(short));
    printf("Int size = %ld;\n", sizeof(int));	
    printf("Long size = %ld;\n", sizeof(long));
    printf("Float size = %ld;\n", sizeof(float));
    printf("Double size = %ld;\n", sizeof(double));
    printf("Pointer size = %ld;\n", sizeof(pointer));
    printf("Array of {char} size = %ld * n (elements);\n", sizeof(array));
}
/*************** Copy of Environment ***************/
size_t EnvLength(char **envp)
{
    size_t length;
    
    assert(NULL != envp);
    
    length = 0;
    
    while(NULL != *envp)
    {
        ++length;
        ++envp;
    }
    return (length);
}

char *StrCpyToLower(char *dest, const char *src)
{
    char *runner = dest;

    assert(NULL != dest);
    assert(NULL != src);

    while(NULL_TERMINATOR != *src)
    {
        *runner = tolower(*src);
        ++runner;
        ++src;
    }
    *runner = NULL_TERMINATOR;
    return (dest);
}

char *DuplicateToLower(const char *s)
{
    size_t len_of_s = 0;
    char *new_array = NULL;

    assert(NULL != s);

    len_of_s = strlen(s);
    new_array = (char *)malloc((len_of_s + 1) * sizeof(*new_array));
    if (NULL == new_array)
	{
		free(new_array);
		new_array = NULL;
		exit(1);
	}
    if(NULL == new_array)
    {

        return (NULL);
    }
    StrCpyToLower(new_array, s);
    return (new_array);
}

void FreeAll(char **buffer, size_t length)
{
    size_t runner = 0;
    
    assert(NULL != length);
    assert(NULL != buffer);
    
    while(length > runner)
    {
        free(buffer[runner]);
        buffer[runner] = NULL;
        ++runner;
    }
    free(buffer);
    buffer = NULL;
}

void CpyEvnpVars(char **buffer, char **envp)
{
	char **envp_runner = envp;

	while (NULL != *envp_runner)
	{
		*buffer = DuplicateToLower(*envp_runner);
		++envp_runner;
		++buffer;
	}
}

void PrintAll(char **buffer, char **envp)
{
	char **envp_runner = envp;
	
	assert(NULL != buffer);
    assert(NULL != envp);
    
	while (NULL != *envp_runner)
	{
		printf("\nbuffer%s\n", *buffer);
		++envp_runner;
		++buffer;
	}
}

void EnvpVar(char **envp)
{
	size_t length_envp = 0;
	char **buffer = NULL;

	assert(NULL != envp);

	length_envp = EnvLength(envp); 
	buffer = (char **)malloc(length_envp * sizeof(char *));
	if (NULL == buffer)
	{
		free(buffer);
		buffer = NULL;
		return;
	}
	CpyEvnpVars(buffer, envp);
	PrintAll(buffer, envp);
	FreeAll(buffer, length_envp);
}


