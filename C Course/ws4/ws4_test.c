/* Reviewed by Dima */
#include <stdio.h> /* printf() */
#include <stdlib.h> /* malloc(), free() */
#include <string.h> /* strlen() */
#include <assert.h> /* assert */
#include "ws4.h"

int TestSumOfMatrixRows();
void TestJosephusProblem();
void TestPrintDataTypes();

int main(int argc, char *argv[], char *envp[])
{
    TestSumOfMatrixRows();
    TestJosephusProblem();
    TestPrintDataTypes();
    EnvpVar(envp);
    
    (void)argc;
    (void)argv;
    return (0);
}

void PrintIntro(const char *name)
{
	printf("*************** %s ***************\n", name);
}

/*************** Sum of Matrix Rows ***************/
int TestSumOfMatrixRows()
{
    size_t row = 4;
    size_t col = 2;
    size_t i = 0;
    int result[4];
    int **arr = (int **)malloc(row * sizeof(*arr));
    
    PrintIntro("Sum of Rows");
    if (NULL == arr)
    {
		free(arr);
		arr = NULL;
		return (1);
    }
    for(i = 0; i < row; ++i)
    {
        arr[i] = (int*)malloc(col * sizeof(int));
        if (NULL == arr[i])
		{
	    	FreeAllInt(arr, col - i);
	    	return (1);
		}
    }
    CreateArray(arr, row, col);
    SumOfMatrixRows(arr, row, col, result);
    PrintArray(result, row);
    FreeAllInt(arr, row);
    printf("\n");
    return (0);
}

/*************** Josephus Problem ***************/
void TestJosephusProblem()
{
	const size_t n = 50;
	int ans = JosephusProblem(n);
	PrintIntro("Josephus Problem");
	printf("survivor = %d\n\n", ans);
}

/*************** Print data types ***************/
void TestPrintDataTypes()
{
    PrintIntro("Data Types");
    PrintDataTypes();
}
